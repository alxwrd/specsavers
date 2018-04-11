from requests_html import HTMLSession


def __get_token():
    page = HTMLSession().get("https://www.specsavers.co.uk/book/nottingham")

    script_tags = page.html.find("script")

    token_script = [
            element for element in script_tags
            if "data-integrity" in element.attrs]

    if token_script:
        return token_script[0].attrs["data-integrity"]


TOKEN = __get_token()
