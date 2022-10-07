from ..model.price import Price
from ..config.db import Database
from ..utils.date_helper import convert_to_string


class PriceRepository:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        pass

    def get_one(self):
        query = self.db.session.query(Price).filter_by(name='John')

    def insert(self, body):
        print(int(body['Product']))
        print(convert_to_string(body['Data']))
        print(body['Unidade'])
        print(float(body['Maximo'].replace(",", ".")))
        print(float(body['Frequente'].replace(",", ".")))
        print(float(body['Minimo'].replace(",", ".")))
        price = Price(product_id=int(body['Product']),
                      publish_date=convert_to_string(body['Data']),
                      unit=body['Unidade'],
                      maximum=float(body['Maximo'].replace(",", ".")),
                      frequent=float(body['Frequente'].replace(",", ".")),
                      minimum=float(body['Minimo'].replace(",", ".")))
        self.db.session.add(price)
        self.db.session.commit()

    def update(self):
        pass

    def delete(self):
        pass
