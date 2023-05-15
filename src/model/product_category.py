from sqlalchemy import Column, Integer, String
from ..model.base import Base


class ProductCategory(Base):
    __tablename__ = "products_category"

    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    def to_json(self):
        return{
            "id": self.id,
            "description": self.description
        }
