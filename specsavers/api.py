import requests
from requests_html import HTMLSession


def retry_on_token_failure(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except AuthenticationError:
            api = args[0]
            api.__class__.__token = api.fetch_token()
            result = func(*args)
        return result
    return wrapper


class AuthenticationError(Exception):
    ...


class Api:
    base_url = "https://www.specsavers.co.uk"
    __token = ""

    def __init__(self):
        if not self.__class__.__token:
            self.__class__.__token = self.fetch_token()

    def fetch_token(self):
        html = self.fetch_booking_page()

        script_tags = html.find("script")

        token_script = [
            element for element in script_tags
            if "data-integrity" in element.attrs]

        if not token_script:
            return ""
        return token_script[0].attrs["data-integrity"]

    def fetch_booking_page(self):
        page = HTMLSession().get(f"{self.base_url}/book/nottingham")

        return page.html

    def store_exists(self, store_name):
        store_page = requests.head(f"{self.base_url}/book/{store_name}")

        if store_page.status_code == 200:
            return True
        else:
            return False

    @retry_on_token_failure
    def fetch_store_details(self, store_name):
        url = (f"{self.base_url}/appointment/api/v1/store"
               f"?url-name={store_name}")

        store_details = self.__make_request(url)

        try:
            return store_details.json()
        except json.decoder.JSONDecodeError:
            return {}

    @retry_on_token_failure
    def fetch_appointments(self, store, date, kind):
        url = (f"{self.base_url}/appointment/api/v1/appointment/"
               f"slot?epos={store.epos}&business-type=opticians&"
               f"appointment-type={kind}"
               f"&date-from={date.iso8601().split('T')[0]}")

        appointment_details = self.__make_request(url)

        try:
            return appointment_details.json()
        except json.decoder.JSONDecodeError:
            return {}

    def __make_request(self, url):
        request = requests.get(
            url, headers={"X-Access-Token": self.__token})

        if request.status_code == 401:
            raise AuthenticationError("Unable to authenticate.")

        return request

    def list_of_store_names(self, latitude, longitude):
        html = self.fetch_store_select_page(latitude, longitude)

        store_divs = html.find(".store-name")

        return [
            div.find("a", first=True).attrs["href"].replace("/stores/", "")
            for div in store_divs]

    def fetch_store_select_page(self, latitude, longitude):
        page = HTMLSession().get(
                f"{self.base_url}/stores/select-a-store/x"
                f"/{latitude},{longitude}")

        return page.html
