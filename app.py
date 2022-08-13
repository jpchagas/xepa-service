from flask import Flask

import sqlalchemy as sq

from .src.model.base import Base
from .src.model.product import Product
from .src.model.price import Price
from .src.model.harvest import Harvest

from .src.controller.price_controller import price_bp


engine = sq.create_engine("mysql+pymysql://dba:J10p02c9315.@localhost/xepa", echo=True)

Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.register_blueprint(price_bp)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
