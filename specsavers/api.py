import requests
from requests_html import HTMLSession


def retry_on_token_failure(func):
    def wrapper(*args):
        try:
            result = func(*args)
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
        page = HTMLSession().get(f"{self.base_url}/book/nottingham")

        script_tags = page.html.find("script")

        token_script = [
            element for element in script_tags
            if "data-integrity" in element.attrs]

        if not token_script:
            return ""
        return token_script[0].attrs["data-integrity"]

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

        store_details = requests.get(
                url, headers={"X-Access-Token": self.__token})

        if store_details.status_code == 401:
            raise AuthenticationError("Unable to authenticate.")
        try:
            return store_details.json()
        except json.decoder.JSONDecodeError:
            return {}
