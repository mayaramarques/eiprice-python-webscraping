from datetime import date, time


class Assortment:

    def __init__(self, name: str, sku: str, department: str, category: str, url: str, image: str,
                 price_to: float, discount: str, available: str, stock_qty: int, store: str, created_at: date,
                 hour: time):
        self.__name = name.replace('\'', '')
        self.__sku = sku
        self.__department = department
        self.__category = category
        self.__url = url
        self.__image = image
        self.__price_to = price_to
        self.__discount = discount
        if available:
            self.__available = 'S'
        else:
            self.__available = 'N'
        self.__stock_qty = stock_qty
        if len(store) > 0:
            self.__store = store[0]['name']
        else:
            self.__store = ''
        self.__created_at = created_at
        self.__hour = hour

    @property
    def name(self):
        return self.__name

    @property
    def sku(self):
        return self.__sku

    @property
    def department(self):
        return self.__department

    @property
    def category(self):
        return self.__category

    @property
    def url(self):
        return self.__url

    @property
    def image(self):
        return self.__image

    @property
    def price_to(self):
        return self.__price_to

    @property
    def discount(self):
        return self.__discount

    @property
    def available(self):
        return self.__available

    @property
    def stock_qty(self):
        return self.__stock_qty

    @property
    def store(self):
        return self.__store

    @property
    def created_at(self):
        return self.__created_at

    @property
    def hour(self):
        return self.__hour
