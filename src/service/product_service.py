from ..repository.product_repository import ProductRepository


class ProductService:

    def __init__(self):
        self.product_repository = ProductRepository()

    def get_all(self):
        return self.product_repository.get_all()

    def get_one(self, description):
        return self.product_repository.get_one(description)

    def add(self, body):
        return self.product_repository.insert(body['Product'], body['Categoria'])

    def update(self):
        self.product_repository.update()

    def remove(self, description):
        self.product_repository.delete(description)
