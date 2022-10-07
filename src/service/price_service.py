from ..repository.price_repository import PriceRepository


class PriceService:

    def __init__(self):
        self.price_repository = PriceRepository()

    def list_all(self):
        self.price_repository.get_all()

    def get_one(self):
        self.price_repository.get_one()

    def add(self, body):
        self.price_repository.insert(body)

    def change(self):
        self.price_repository.update()

    def remove(self):
        self.price_repository.delete()
