from fastapi import FastAPI
from ..scripts import ShopperWebScraping

app = FastAPI()

@app.post("/scripts/shooper/start")
def start_shopper():
  script = ShopperWebScraping.Coleta()

@app.get("/scripts/shopper/status")
def check_shopper_status():
  return

@app.get("/api/assortment")
def get_assortment():
  return

@app.get("/api/assortment/product/{product_name}")
def get_assortment_by_procuct_name(product_name: str):
  return

@app.get("/api/assortment/department/{department_name}")
def get_assortment_by_department_name(department_name: str):
  return

@app.get("/api/seller")
def get_seller():
  return

@app.get("/api/seller/product/{product_name}")
def get_seller_by_procuct_name(product_name: str):
  return

@app.get("/api/seller/department/{department_name}")
def get_seller_by_department_name(department_name: str):
  return
