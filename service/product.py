from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy import asc, desc
from config.database import db
from model.product import Products, ProductSchema
from repository.product import ProductRepository


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.product_schema = ProductSchema()
        self.products_schema  = ProductSchema(many = True)
    def save(self, data):
        try:
            self.product_schema.load(data)
            new_product = self.product_repository.save(data["product_name"], data["price"], data["description"], data["quantity"])
            db.session.add(new_product)
            db.session.commit()
            
            response_message = {
                "code": 201,
                "status": "Created",
                "message": "New product added"
            }
            return jsonify(response_message), 201
        except ValidationError as err:
            response_message = {
                "code": 400,
                "status": "Bad Request",
                "errorField": err.messages
            }
            return jsonify(response_message), 400
    def find_all(self):
        products = self.product_repository.find_all()
        result = self.products_schema.dump(products)
        return jsonify(result), 200
    def order_by_params(self, params: str):
        if params == "asc":
            data = Products.query.order_by(asc(Products.product_name))
            res = self.products_schema.dump(data)
            return jsonify(res), 200
        elif params == "desc":
            data = Products.query.order_by(desc(Products.product_name))
            res = self.products_schema.dump(data)
            return jsonify(res), 200
        elif params == "latest":
            data = Products.query.order_by(desc(Products.product_id))
            res = self.products_schema.dump(data)
            return jsonify(res), 200
        elif params == "max":
            data = Products.query.order_by(desc(Products.price))
            res = self.products_schema.dump(data)
            return jsonify(res), 200
        elif params == "min":
            data = Products.query.order_by(asc(Products.price))
            res = self.products_schema.dump(data)
            return jsonify(res), 200