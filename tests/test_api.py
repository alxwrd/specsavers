
import unittest

from requests_html import HTML


class TestApi(unittest.TestCase):

    def setUp(self):
        from specsavers.api import Api

        self.test_token = (
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
            "eyJuYW1lIjoiU1NFUkVnRUhKMmtKVHNldUtDI"
            "iwiZXhwIjoxNTIzNzA4MDU5fQ.2U5GYS_SbZq"
            "4bEUpTA6Em0l4XF3jrMtjBOZyCxZMe3Q")

        Api._Api__token = self.test_token

        with open("tests/page_book.html", "r") as book:
            self.booking_page = book.read()

        with open("tests/page_store_select.html", "r") as store_select:
            self.store_select_page = store_select.read()

        Api.fetch_booking_page = lambda *_: HTML(html=self.booking_page)
        Api.fetch_store_select_page = \
            lambda *_: HTML(html=self.store_select_page)

        self.api = Api()

    def test_getting_token_from_html(self):
        token = self.api.fetch_token()

        self.assertEqual(token, self.test_token)

    def test_parsing_for_store_names(self):
        store_names = self.api.list_of_store_names(1234, 5678)

        self.assertEqual(store_names, ["woolwich", "barking", "eastham"])

    def test_(self):
        ...
