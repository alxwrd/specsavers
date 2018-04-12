from requests_html import HTMLSession

from specsavers.store import Store
from specsavers.store import StoreList


def locate(coords):
    return StoreList(coords)


def find(store_name):
    return Store(store_name)
