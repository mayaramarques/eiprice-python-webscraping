from threading import Thread

from fastapi import FastAPI

from app.model import Assortment
from scripts.ShopperWebScraping import ShopperWebScraping
from app.component.AssortmentComponent import AssortmentComponent

app = FastAPI()


@app.post("/scripts/shopper/start")
def start_shopper():
    process = ShopperWebScraping()
    process.start_collect()


@app.get("/api/assortment")
def get_assortments() -> dict[Assortment]:
    component = AssortmentComponent()
    result = component.get_assortments()
    return result


@app.get("/api/assortment/product/{product_name}")
def get_assortment_by_product_name(product_name: str) -> dict[Assortment]:
    component = AssortmentComponent()
    result = component.get_assortment_by_product_name(product_name)
    return result


@app.get("/api/assortment/department/{department_name}")
def get_assortment_by_department_name(department_name: str) -> dict[Assortment]:
    component = AssortmentComponent()
    result = component.get_assortment_by_department_name(department_name)
    return result
