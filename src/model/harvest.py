from sqlalchemy import Column, Integer, String, ForeignKey
from ..model.base import Base

class Harvest(Base):
    __tablename__ = 'harvest'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    jan = Column(String(1))
    fev = Column(String(1))
    mar = Column(String(1))
    abr = Column(String(1))
    mai = Column(String(1))
    jun = Column(String(1))
    jul = Column(String(1))
    ago = Column(String(1))
    sep = Column(String(1))
    out = Column(String(1))
    nov = Column(String(1))
    dez = Column(String(1))