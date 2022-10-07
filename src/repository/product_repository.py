from ..model.product import Product
from ..config.db import Database
from ..utils.date_helper import convert_to_string


class ProductRepository:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        pass

    def get_one(self):
        query = self.db.session.query(Product).filter_by(name='John')

    def insert(self, body):
        print(body)
        print(body['Product'])
        print(body['Categoria'])
        product = Product(description=body['Product'],
                          category=body['Categoria'])
        self.db.session.add(product)

        new_product = self.db.session.commit()
        print(new_product)

    def update(self):
        pass

    def delete(self):
        pass
