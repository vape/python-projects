from collections import defaultdict, OrderedDict
from Classes.utils import initializer


class NoSuchProductException(BaseException):
    @initializer(private=True)
    def __init__(self, product):
        pass

    @property
    def product(self):
        return self._product


class NotEnoughInventoryException(BaseException):
    @initializer(private=True)
    def __init__(self, product, current_stock):
        pass

    @property
    def product(self):
        return self._product

    @property
    def current_stock(self):
        return self._current_stock


class Product(object):
    @initializer(private=True)
    def __init__(self, prod_id, name, price):
        pass

    @property
    def prod_id(self):
        return self._prod_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price


class Inventory(object):
    def __init__(self):
        self._products = dict()
        self._inventory = defaultdict(int)

    def add_product(self, product, quantity):
        self._products.setdefault(product.prod_id, product)
        self._inventory[product.prod_id] += quantity

    def remove_product(self, product, quantity):
        if product not in self:
            raise NoSuchProductException(product)
        if self.product_inventory_count(product) < quantity:
            raise NotEnoughInventoryException(product, self.product_inventory_count(product))
        self._inventory[product.prod_id] -= quantity

    def product_inventory_count(self, product):
        return self._inventory.get(product.prod_id, 0)

    def total_inventory_count(self):
        return sum(self._inventory.values())

    def total_inventory_value(self):
        quantities = [q for q in OrderedDict(sorted(self._inventory.items(), key=lambda t: t[0])).values()]
        prices = [prod.price for prod in OrderedDict(sorted(self._products.items(), key=lambda t: t[0])).values()]
        return sum([i[0]*i[1] for i in zip(quantities, prices)])

    def clear(self):
        self._products.clear()
        self._inventory.clear()

    @property
    def is_empty(self):
        return self.total_inventory_count() == 0

    def exists(self, product):
        return product in self

    def __contains__(self, item):
        return self._inventory.get(item.prod_id, 0) > 0


