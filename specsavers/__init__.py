from requests_html import HTMLSession

from specsavers.store import Store
from specsavers.store import StoreList


def locate(latitude=None, longitude=None):
    return StoreList.from_search(latitude, longitude)


def find(store_name):
    return Store(store_name)
