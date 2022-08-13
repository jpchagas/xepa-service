from ..model.price import Price
from ..config.db import Database


class PriceRepository:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        pass

    def get_one(self):
        query = self.db.session.query(Price).filter_by(name='John')

    def insert(self):
        user = Price(name='John Snow', password='johnspassword')
        self.db.session.add(user)

    def update(self):
        pass

    def delete(self):
        pass
