from ..repository.product_repository import ProductRepository


class ProductService:

    def __init__(self):
        self.product_repository = ProductRepository()

    def list_all(self):
        self.product_repository.get_all()

    def get_one(self):
        self.product_repository.get_one()

    def add(self, body):
        self.product_repository.insert(body)

    def change(self):
        self.product_repository.update()

    def remove(self):
        self.product_repository.delete()
