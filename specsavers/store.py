from datetime import datetime
import requests
import maya
import specsavers

from specsavers.api import Api
from specsavers.appointment import Appointment
from specsavers.appointment import AppointmentType


class Store:
    api = Api

    def __init__(self, store_name, from_search=False):
        self.api = self.api()
        self.url_name = store_name.lower()
        self.json = {}

        if not from_search:
            if not self.api.store_exists(self.url_name):
                raise LookupError(f"The store '{self.url_name}' is not valid.")
            self.json = self.__fetch_store_details()

    def __getattr__(self, attr):
        if not self.json:
            self.json = self.__fetch_store_details()
        return object.__getattribute__(self, attr)

    def appointments(self, date=None, kind=AppointmentType.AdultEyeTest):
        date = self.__to_maya(date)

        appointments = self.api.fetch_appointments(
            store=self, date=date, kind=kind)

        slots = appointments.get("content", {}).get("slots", [])

        return [
            Appointment(
                slot["id"],
                maya.parse(slot["date"]["start"]),
                maya.parse(slot["date"]["end"]))
            for slot in slots
            if maya.parse(slot["date"]["start"]).day == date.day]

    @staticmethod
    def __to_maya(date):
        mapping = {
            str: lambda date: maya.when(date),
            int: lambda date: maya.MayaDT(epoch=date),
            maya.MayaDT: lambda date: data,
            datetime: lambda date: maya.MayaDT.from_datetime(date)
        }

        try:
            return mapping[type(date)](date)
        except KeyError:
            return maya.now()

    def __fetch_store_details(self):
        details = self.api.fetch_store_details(self.url_name)

        stores = details.get("content", {}).get("stores", [])

        if not stores:
            return {}

        store = stores[0]

        for key, value in store.items():
            setattr(self, key, value)

        return store

    def __repr__(self):
        return f"<Store name='{self.url_name}'>"


class StoreList:
    api = Api

    def __init__(self, stores):
        try:
            store = stores[0]
        except IndexError:
            store = None

        if isinstance(store, Store):
            self.__stores = stores

        elif isinstance(store, str):
            self.__stores = [
                Store(name, from_search=True)
                for name in stores]

        else:
            raise ValueError("'stores' must be a list of 'str' or 'Store'")

    @classmethod
    def from_search(cls, latitude=None, longitude=None):
        if latitude is None or longitude is None:
            raise ValueError("Both 'latitude' and 'longitude' are required")

        stores = cls.api().list_of_store_names(latitude, longitude)

        if not stores:
            raise LookupError(
                    f"Unable to locate any stores at {latitude}, {longitude}")

        return cls(stores)

    def __getitem__(self, item):
        if isinstance(item, slice):
            stores = self.__stores[item]
            return self.__class__(stores)

        if isinstance(item, int):
            return self.__stores[item]

        if isinstance(item, str):
            for store in self.__stores:
                if item == store.url_name:
                    return store

    def __repr__(self):
        stores = str(
            [repr(store) for store
             in self.__stores]
            ).replace("'", "")

        return f"<{self.__class__.__name__}({stores})>"
