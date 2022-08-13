import sqlalchemy as sq
import os
from ..model.base import Base
from ..model.product import Product
from ..model.price import Price
from ..model.harvest import Harvest


class Database:
    def __init__(self):
        self.engine = sq.crecreate_engine(os.getenv('DB_URL') + "xepa" , echo=True)
        Session = sq.orm.sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(bind=self.engine)

    def get_engine(self):
        return self.engine

    def get_session(self):
        return self.session
