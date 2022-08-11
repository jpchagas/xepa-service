from sqlalchemy import Column, Integer, String, Numeric, Date
from ..model.base import Base

class Price(Base):
    __tablename__ = 'prices'

    id = Column(Integer, primary_key=True)
    product = Column(Integer)
    data = Column(Date)
    unit = Column(String(5))
    maximum = Column(Numeric)
    frequent = Column(Numeric)
    minimum = Column(Numeric)