from sqlalchemy import Column, Integer, String, ForeignKey
from ..model.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    description = Column(String(50))
    category = Column(Integer, ForeignKey('products_category.id'))

    def to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "category": self.category
        }
