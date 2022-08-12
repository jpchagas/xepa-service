from sqlalchemy import Column, Integer, String
from ..model.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    description = Column(String(50))
    category = Column(String(15))

    def __repr__(self):
        return f"User {self.name}"
