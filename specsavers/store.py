import requests
import specsavers

from specsavers.api import Api


class Store:
    api = Api

    def __init__(self, store_name, from_search=False):
        self.api = self.api()
        self.name = store_name.lower()
        self.json = {}

        if not from_search:
            if not self.api.store_exists(self.name):
                raise LookupError(f"The store '{self.name}' is not valid.")
            self.json = self.__fetch_store_details()

    def __getattr__(self, attr):
        if not self.json:
            self.json = self.__fetch_store_details()

        try:
            return self.json[attr]
        except KeyError:
            raise AttributeError(
                    (f"{self.__class__.__name__} object "
                     f"has no attribute '{attr}'")) from None

    def __fetch_store_details(self):
        details = self.api.fetch_store_details(self.name)

        stores = details.get("content", {}).get("stores", [])

        if not stores:
            return {}

        return stores[0]


class StoreList:
    api = Api

    def __init__(self, stores):
        try:
            store = stores[0]
        except IndexError:
            raise ValueError(
                "'stores' must be a list of 'str' or 'Store'") from None

        if isinstance(store, self.__class__):
            self.__stores = stores

        elif isinstance(store, str):
            self.__stores = [
                Store(name, from_search=True)
                for name in stores]

    @classmethod
    def from_search(cls, latitude=None, longitude=None):
        if latitude is None or longitude is None:
            raise ValueError("Both 'latitude' and 'longitude' are required")

        stores = cls.api().list_of_store_names(latitude, longitude)

        return cls(stores)

    def __getitem__(self, item):
        if isinstance(item, slice):
            stores = self.__stores[item]
            return self.__class__(stores)

        if isinstance(item, int):
            return self.__stores[item]

        if isinstance(item, str):
            for store in self.__stores:
                if item == store.name:
                    return store
