from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from ..model.base import Base

class Price(Base):
    __tablename__ = 'prices'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    data = Column(Date)
    unit = Column(String(5))
    maximum = Column(Numeric)
    frequent = Column(Numeric)
    minimum = Column(Numeric)