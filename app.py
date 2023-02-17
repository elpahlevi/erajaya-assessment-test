import os
from flask import Flask
from config.database import db
from config.marshmallow import ma
from controller.product import products

# Initialize Flask
app = Flask(__name__)
# Prevent JSON keys sorting
app.config["JSON_SORT_KEYS"] = False
# Set Database URI
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("PGSQL_URI")

# Initialize database & marshmallow
db.init_app(app)
ma.init_app(app)

# Create table if not exists
with app.app_context():
    db.create_all()

# Register products controller
app.register_blueprint(products)