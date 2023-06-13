from model.product import Products

class ProductRepository:
    def save(self, product_name, price, description, quantity):
        return Products(product_name, price, description, quantity)
    def find_all(self):
        return Products.query.all()