import json
from sqlalchemy import select, update
from ..model.product import Product
from ..config.db import Database
from flask import jsonify


class ProductRepository:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        """

        """
        statement = select(Product)
        result = self.db.session.execute(statement).scalars().all()
        return jsonify([r.to_json() for r in result])

    def get_one(self, description):
        """

        """
        statement = select(Product).filter_by(description=description)
        result = self.db.session.execute(statement).scalars().first()
        if result is None:
            return "Product with this description not found", 404
        else:
            return result.to_json(), 200

    def insert(self, description, category):
        # Search if product exist on database
        statement = select(Product).filter_by(description=description)
        product = self.db.session.execute(statement).scalars().first()
        if product is not None:
            return "Product already existed"
        else:
            product = Product(description=description,
                              category=category)
            try:
                self.db.session.add(product)
            except:
                self.db.session.rollback()
                raise
            else:
                self.db.session.commit()
                return json.dumps({
                    "description": description,
                    "category": category
                })

    def update(self, description, category):
        # Search if product exist on database
        statement = select(Product).filter_by(description=description)
        product = self.db.session.execute(statement).scalars().first()
        if product is None:
            return "Product not found"
        else:
            # Update product
            stmt = (
                update(Product)
                    .where(Product.name == "squidward")
                    .values(name="spongebob")
                    .execution_options(synchronize_session="fetch")
            )

            result = self.db.session.execute(stmt)

    def delete(self, description):
        # Search if product exist on database
        product = self.get_one(description)
        if product is None:
            return "Product doesn't exist"
        else:
            # Delete product
            result = self.db.session.delete(product)
            self.db.session.commit()
            return result
