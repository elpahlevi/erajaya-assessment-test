from flask import Blueprint, request
from service.product import ProductService

products = Blueprint("products", __name__, url_prefix="/api/v1/products")
product_service = ProductService()

@products.post("/")
def add_product():
    data = request.get_json()
    return product_service.save(data)
    
@products.get("/")
def get_products():
    if request.query_string:
        params = request.args.get("orderBy")
        return product_service.order_by_params(params)
    else:
        return product_service.find_all()
    