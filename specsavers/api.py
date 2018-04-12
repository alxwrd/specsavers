from requests_html import HTMLSession


class Api:
    base_url = "http://www.specsavers.co.uk"

    def __init__(self):
        self.__token = ""

    @property
    def token(self):
        if not self.__token:
            self.__token = self.__fetch_token()
        return self.__token

    def __fetch_token(self):
        page = HTMLSession().get(f"{self.base_url}/book/nottingham")

        script_tags = page.html.find("script")

        token_script = [
                element for element in script_tags
                if "data-integrity" in element.attrs]

        if not token_script:
            return ""
        return token_script[0].attrs["data-integrity"]
