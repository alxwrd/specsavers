import requests
import specsavers

from specsavers.api import Api


class Store:
    api = Api

    def __init__(self, store_name, from_search=False):
        self.api = self.api()

        store_name = store_name.lower()

        if not from_search:
            if not self.api.store_exists(store_name):
                raise LookupError(f"The store '{store_name}' is not valid.")

        self.name = store_name

        self.json = self.__fetch_store_details() if not from_search else {}

    def __getattr__(self, attr):
        if not self.json:
            self.json = self.__fetch_store_details()

        try:
            return self.json[attr]
        except KeyError:
            raise AttributeError(
                    (f"{self.__class__.__name__} object "
                     f"has no attribute '{attr}'"))

    def __fetch_store_details(self):
        details = self.api.fetch_store_details(self.name)

        stores = details.get("content", {}).get("stores", [])

        if not stores:
            return {}

        return stores[0]


class StoreList:
    api = Api

    def __init__(self, store_names): ...

    @classmethod
    def from_search(cls, latitude=None, longitude=None):
        if latitude is None or longitude is None:
            raise ValueError("")

        stores = cls.api().list_of_store_names(latitude, longitude)

        return cls(stores)
