from datetime import date, time


class Assortment:

    def __init__(self, name: str, sku: str, department: str, category: str, url: str, image: str,
                 price_to: float, discount: str, available: str, stock_qty: int, store: str, created_at: date,
                 hour: time):
        self._name = name
        self._sku = sku
        self._department = department
        self._category = category
        self._url = url
        self._image = image
        self._price_to = price_to
        self._discount = discount
        self._available = available
        self._stock_qty = stock_qty
        self._store = store
        self._created_at = created_at
        self._hour = hour

    @property
    def name(self):
        return self._name

    @property
    def sku(self):
        return self._sku

    @property
    def department(self):
        return self._department

    @property
    def category(self):
        return self._category

    @property
    def url(self):
        return self._url

    @property
    def image(self):
        return self._image

    @property
    def price_to(self):
        return self._price_to

    @property
    def discount(self):
        return self._discount

    @property
    def available(self):
        return self._available

    @property
    def stock_qty(self):
        return self._stock_qty

    @property
    def store(self):
        return self._store

    @property
    def created_at(self):
        return self._created_at

    @property
    def hour(self):
        return self._hour
