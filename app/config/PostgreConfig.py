import logging
import psycopg2


class PostgreConfig:
    _db = None

    def __init__(self, host, db, usr, pwd):
        self._db = psycopg2.connect(host=host, database=db, user=usr, password=pwd)

    def save(self, sql):
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()

        except Exception as e:
            logging.error(e)
            return False
        return True

    def get(self, sql):
        rs = None
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            rs = cur.fetchall()

        except Exception as e:
            logging.error(e)
            return None
        return rs

    def next_pk(self, table, key):
        sql = 'select max(' + key + ') from ' + table
        rs = self.get(sql)
        pk = rs[0][0]
        return pk + 1

    def close(self):
        self._db.close()
