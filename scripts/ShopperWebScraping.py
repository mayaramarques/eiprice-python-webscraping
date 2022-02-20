import configparser

import requests
from datetime import datetime

from scripts.model.Assortment import Assortment


class ShopperWebScraping:
    def __init__(self):
        self._bearer = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0b21lcklkIjo3OTI5ODQsIm' \
                       'RldmljZVVVSUQiOiI4MWQyYzkxNy0xMDI5LTRmYTctYmNkNS0wOTllYWYzY2Y4OTUiLCJpYXQi' \
                       'OjE2NDUzNjU2MDd9.uiI_gZpRryOJ3gElVwvz0Tfencs9gUlWBNvM2vx4dBA'
        return

    def __get_config(self):
        config = configparser.ConfigParser()
        config.read('application.properties')
        return config

    def __authenticate(self):
        config = self.__get_config()
        login = config.get('login')
        password = config.get('password')
        url = config.get('auth_url')
        method = config.get('method')
        body = {
            'login': login,
            'password': password,
            'method': method
        }
        response = requests.post(url=url, data=body)
        self._bearer = response.headers.get('authorization')

    def __get_auth_header(self):
        header = {
            'Authorization': self._bearer
        }
        return header

    def __search_departments(self):
        url = 'https://siteapi.shopper.com.br/catalog/departments'
        response = requests.get(url=url, headers=self.__get_auth_header())
        data = response.json()
        return data

    def __search_sub_departments(self, departments: dict):
        sub_departments = departments['departments']
        for department in sub_departments:
            if department['name'] == 'Alimentos':
                departments_id = department['id']
                sub_departments = department['subdepartments']
                break
        return departments_id, sub_departments

    def __search_products(self, id_department: int, sub_department_list: dict):
        page = 0
        url = f'https://siteapi.shopper.com.br/catalog/products?department={id_department}'
        products = []
        for sub_department in sub_department_list:
            last = False
            while not last:
                page += 1
                sub_id_department = sub_department['id']
                product_url = f'{url}&subdepartment={sub_id_department}&page={page}&size=20&'
                response = requests.get(url=product_url, headers=self.__get_auth_header()).json()
                products.extend(response['products'])
                last = response['last']

        return products

    def __structure_product(self, product: any) -> Assortment:
        return Assortment(product.get('name'),
                          product.get('id'),
                          product.get('metadata')['department_url'],
                          product.get('metadata')['subdepartment_url'],
                          product.get('url'),
                          product.get('image'),
                          str(product.get('price')).replace('R$ ', '').replace(',', '.'),
                          product.get('savingPercentage'),
                          (str(product.get('pause')) == 'false' if 'S' else 'N'),
                          product.get('maxCartQuantity'),
                          product.get('merchants'),
                          datetime.today(),
                          datetime.now())

    def __save_product(self, products: dict):
        for product in products:
            structured_product = self.__structure_product(product)
            # save in postgre
        return

    def start_collect(self):
        # self.__authenticate()
        departments = self.__search_departments()
        id_department, sub_departments = self.__search_sub_departments(departments)
        products = self.__search_products(id_department, sub_departments)
        self.__save_product(products)
        return


teste = ShopperWebScraping()
teste.start_collect()
