from sqlalchemy import select, update, delete
from ..model.product_category import ProductCategory
from ..config.db import Database


class ProductCategoryRepository:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        statement = select(ProductCategory)
        product_list = self.db.session.execute(statement).scalars().all()
        return product_list

    def get_one(self, description):
        statement = select(ProductCategory).filter_by(description=description)
        product = self.db.session.execute(statement).scalars().first()
        return product

    def insert(self, description):
        try:
            product = ProductCategory(description=description)
            self.db.session.add(product)
            self.db.session.commit()
            return product
        except:
            self.db.session.rollback()

    def update(self, old_description, new_description):
        stmt = (
            update(ProductCategory)
                .where(ProductCategory.description == old_description)
                .values(description=new_description)
                .execution_options(synchronize_session="fetch")
        )

        self.db.session.execute(stmt)
        self.db.session.commit()
        product = self.get_one(new_description)
        return product

    def delete(self, description):
        try:
            product = self.get_one(description)
            self.db.session.delete(product)
            self.db.session.commit()
            return product
        except:
            return {
                "description": "Fail to delete product_unit because not exists"
            }