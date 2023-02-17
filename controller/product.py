from flask import Blueprint, request
from service.product import ProductService

products = Blueprint("products", __name__, url_prefix="/api/v1/products")
product_service = ProductService()

# Add a new product
@products.post("/")
def add_product():
    data = request.get_json()
    return product_service.save(data)
    
# Get all products
@products.get("/")
def get_products():
    # Order products based on query string parameters
    if request.query_string:
        params = request.args.get("orderBy")
        return product_service.order_by_params(params)
    else:
        # Get all products
        return product_service.find_all()
    