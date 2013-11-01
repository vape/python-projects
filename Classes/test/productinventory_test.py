from Classes.productinventory.inventory import Product, Inventory
from Classes.productinventory.inventory import NoSuchProductException, NotEnoughInventoryException
from unittest import TestCase


class InventoryTests(TestCase):
    def setUp(self):
        self.i = Inventory()
        self.p1 = Product(1, 'p1', 1)
        self.p2 = Product(2, 'p2', 2)

    def test_initialize(self):
        self.assertIsNotNone(self.i._inventory)
        self.assertIsNotNone(self.i._products)

    def test_add_product(self):
        self.i.add_product(self.p1, 1)

        self.assertIn(self.p1.prod_id, self.i._inventory)
        self.assertIn(self.p1.prod_id, self.i._products)
        self.assertEqual(self.i._inventory[self.p1.prod_id], 1)

    def test_add_same_product(self):
        self.i.add_product(self.p1, 1)
        self.i.add_product(self.p1, 3)

        self.assertIn(self.p1.prod_id, self.i._inventory)
        self.assertIn(self.p1.prod_id, self.i._products)
        self.assertEqual(self.i._inventory[self.p1.prod_id], 4)

    def test_add_multiple_products(self):
        self.i.add_product(self.p1, 1)
        self.i.add_product(self.p2, 5)

        self.assertIn(self.p1.prod_id, self.i._inventory)
        self.assertIn(self.p1.prod_id, self.i._products)
        self.assertIn(self.p2.prod_id, self.i._inventory)
        self.assertIn(self.p2.prod_id, self.i._products)

        self.assertEqual(self.i._inventory[self.p1.prod_id], 1)
        self.assertEqual(self.i._inventory[self.p2.prod_id], 5)

    def test_total_inventory_count(self):
        self.i.add_product(self.p1, 10)
        self.i.add_product(self.p2, 15)

        self.assertEqual(self.i.total_inventory_count(), 25)

    def test_total_inventory_value(self):
        self.i.add_product(self.p1, 1)
        self.i.add_product(self.p2, 5)

        self.assertEqual(self.i.total_inventory_value(), 11)

    def test_inventory_is_empty(self):
        self.assertTrue(self.i.is_empty)

        self.i.add_product(self.p1, 1)

        self.assertFalse(self.i.is_empty)

    def test_inventory_clear(self):
        self.i.add_product(self.p1, 3)
        self.i.add_product(self.p2, 5)

        self.assertFalse(self.i.is_empty)

        self.i.clear()

        self.assertTrue(self.i.is_empty)

    def test_product_exists(self):
        self.assertFalse(self.i.exists(self.p1))
        self.assertFalse(self.p1 in self.i)

        self.i.add_product(self.p1, 20)
        self.assertTrue(self.p1 in self.i)

    def test_product_inventory_count(self):
        self.assertEqual(self.i.product_inventory_count(self.p1), 0)

        self.i.add_product(self.p1, 100)
        self.assertEqual(self.i.product_inventory_count(self.p1), 100)

    def test_remove_product(self):
        self.assertFalse(self.p1 in self.i)

        self.i.add_product(self.p1, 5)
        self.assertTrue(self.p1 in self.i)

        self.i.remove_product(self.p1, 3)
        self.assertTrue(self.p1 in self.i)
        self.assertEqual(self.i.product_inventory_count(self.p1), 2)

    def test_remove_non_existent_product(self):
        self.assertRaises(NoSuchProductException, self.i.remove_product, self.p1, 1)

    def test_remove_not_enough_inventory(self):
        self.i.add_product(self.p1, 10)
        self.assertRaises(NotEnoughInventoryException, self.i.remove_product, self.p1, 11)

