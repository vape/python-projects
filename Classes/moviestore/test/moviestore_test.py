from unittest import TestCase
from Classes.moviestore.store import MovieStore, Customer, Video, Transaction
from uuid import uuid4
from datetime import datetime, timedelta

class MovieStoreTests(TestCase):
    def setUp(self):
        self.s = MovieStore()
        self.s.add_customer('Douglas Adams')
        self.s.add_customer('Stephen Fry')
        self.s.add_customer('Hugh Laurie')
        self.s.add_customer('Stephen Merchant')

        self.s.add_video(Video(1, 'v1'))
        self.s.add_video(Video(2, 'v2'))
        self.s.add_video(Video(3, 'v3'))

    def test_add_customer(self):
        cust = self.s.add_customer('c1')
        self.assertIsNotNone(cust)
        self.assertIsInstance(cust, Customer)

    def test_get_customer_with_id(self):
        cust = self.s.add_customer('c1')
        retr_cust = self.s.get_customer(cust.uid)

        self.assertIsNotNone(retr_cust)
        self.assertIsInstance(retr_cust, Customer)
        self.assertEqual(retr_cust.name, 'c1')

    def test_get_non_existent_customer(self):
        self.s.add_customer('c1')
        retr_cust = self.s.get_customer(uuid4())

        self.assertIsNone(retr_cust)

    def test_find_customer_returns_existing_customer(self):
        search_results = self.s.find_customer('doug')
        self.assertIsInstance(search_results, list)
        self.assertEqual(len(search_results), 1)

        search_results = self.s.find_customer('stephen')
        self.assertIsInstance(search_results, list)
        self.assertEqual(len(search_results), 2)

    def test_find_customer_returns_empty_list_for_nonexistent_customer(self):
        search_results = self.s.find_customer('asdasd')
        self.assertIsInstance(search_results, list)
        self.assertEqual(len(search_results), 0)

    def test_checkout_video(self):
        cust = self.s.find_customer('Hugh Laurie')[0]
        exp_return_date = datetime.now() + timedelta(days=3)
        trx = self.s.checkout_video(1, cust, exp_return_date)

        self.assertIsInstance(trx, Transaction)
        self.assertEqual(trx.video_id, 1)
        self.assertEqual(trx.customer_id, cust.uid)
        self.assertEqual(trx.expected_return_date, exp_return_date)

    def test_checkout_already_checked_out_video(self):
        cust1 = self.s.find_customer('Hugh Laurie')[0]
        exp_return_date = datetime.now() + timedelta(days=3)
        trx = self.s.checkout_video(1, cust1, exp_return_date)

        cust2 = self.s.find_customer('Douglas Adams')[0]

        with self.assertRaises(ValueError):
            self.s.checkout_video(1, cust2, exp_return_date)

    def test_return_video_which_is_not_checked_out(self):
        with self.assertRaises(ValueError):
            self.s.return_video(1, datetime.now())

    def test_return_video_on_time(self):
        cust1 = self.s.find_customer('Hugh Laurie')[0]
        exp_return_date = datetime.now() + timedelta(days=3)
        trx = self.s.checkout_video(1, cust1, exp_return_date)

        actual_return_date = datetime.now() + timedelta(days=2)
        ret_result = self.s.return_video(1, actual_return_date)
        self.assertEqual(ret_result, 0)








