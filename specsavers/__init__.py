from requests_html import HTMLSession

from specsavers.store import Store
from specsavers.store import StoreList


def __get_token():
    page = HTMLSession().get("https://www.specsavers.co.uk/book/nottingham")

    script_tags = page.html.find("script")

    token_script = [
            element for element in script_tags
            if "data-integrity" in element.attrs]

    if token_script:
        return token_script[0].attrs["data-integrity"]


def locate(coords):
    return StoreList(coords)


def find(store_name):
    return Store(store_name)


TOKEN = __get_token()
