import unittest

from tests import MockApi


class TestStore(unittest.TestCase):

    def setUp(self):
        import specsavers

        self.specsavers = specsavers

        self.specsavers.Store.api = MockApi
        self.specsavers.StoreList.api = MockApi

    def test_no_fetching_details_on_search(self):
        store = self.specsavers.Store("nottingham", from_search=True)

        self.assertEqual(store.json, {})

    def test_details_fetched_once_attr_accessed(self):
        store = self.specsavers.Store("nottingham", from_search=True)

        store.business_type

        self.assertEqual(store.business_type, "opticians")

    def test_find_gets_store(self):
        store = self.specsavers.find("nottingham")

        self.assertIsInstance(store, self.specsavers.Store)

    def test_locate_gets_store_list(self):
        store_list = self.specsavers.locate(
                latitude=51.507879, longitude=0.087732)

        self.assertIsInstance(store_list, self.specsavers.StoreList)

    def test_store_list_indexable(self):
        store_list = self.specsavers.locate(
                latitude=51.507879, longitude=0.087732)

        store = store_list[0]

        self.assertIsInstance(store, self.specsavers.Store)

    def test_store_list_sliceable(self):
        store_list = self.specsavers.locate(
                latitude=51.507879, longitude=0.087732)

        store_slice = store_list[0:1]

        self.assertIsInstance(store_slice, self.specsavers.StoreList)

    def test_store_list_lookupable(self):
        store_list = self.specsavers.locate(
                latitude=51.507879, longitude=0.087732)

        store = store_list["woolwich"]

        self.assertIsInstance(store, self.specsavers.Store)

    def test_store_list_iterable(self):
        store_list = self.specsavers.locate(
                latitude=51.507879, longitude=0.087732)

        for store in store_list:
            self.assertTrue(True)

    def test_store_iterating_no_details(self):
        store_list = self.specsavers.locate(
                latitude=51.507879, longitude=0.087732)

        for store in store_list:
            self.assertEqual(store.json, {})
