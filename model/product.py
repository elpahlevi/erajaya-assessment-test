from config.database import db
from config.marshmallow import ma
from marshmallow import fields, validate

# Define table
class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, product_name: str, price: int, description: str, quantity: str):
        self.product_name = product_name
        self.price = price
        self.description = description
        self.quantity = quantity

# Product Schema
class ProductSchema(ma.Schema):
    product_name = fields.Str(required=True, validate=[validate.Length(min=2, max=128)])
    price = fields.Int(required=True)
    description = fields.Str(required=True, validate=[validate.Length(min=10)])
    quantity = fields.Int(required=True)

    class Meta:
        # Fields to expose
        fields = ("product_id", "product_name", "price", "description", "quantity")
        # keep the position
        ordered = True