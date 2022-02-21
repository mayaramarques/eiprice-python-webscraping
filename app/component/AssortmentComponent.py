from app.config.PostgreConfig import PostgreConfig
from app.model.Assortment import Assortment


class AssortmentComponent:
    def __init__(self):
        host = "postgres"
        db = "shopper"
        username = "shopper"
        password = "shopper"
        self._postgre_conn = PostgreConfig(host, db, username, password)

    def save_assortment(self, assortment: Assortment):
        sql = f"insert into assortment (name, sku, department, category, url, image, " \
              f"price_to, discount, available, stock_qty, store, created_at, hour) " \
              f"values ('{assortment.name}', '{assortment.sku}', '{assortment.department}', " \
              f"'{assortment.category}', '{assortment.url}', '{assortment.image}', '{assortment.price_to}', " \
              f"'{assortment.discount}', '{assortment.available}', '{assortment.stock_qty}', '{assortment.store}', " \
              f"'{assortment.created_at}','{assortment.hour}')".encode("UTF-8")
        self._postgre_conn.save(sql)

    def get_assortment_by_product_name(self, product_name: str) -> dict[Assortment]:
        sql = f"select * from assortment where name like '%{product_name}%'"
        return self._postgre_conn.get(sql)

    def get_assortment_by_department_name(self, department_name: str) -> dict[Assortment]:
        sql = f"select * from assortment where department like '%{department_name}%'"
        return self._postgre_conn.get(sql)

    def get_assortments(self) -> dict[Assortment]:
        sql = "select * from assortment"
        return self._postgre_conn.get(sql)

    def close_db(self):
        self._postgre_conn.close()
