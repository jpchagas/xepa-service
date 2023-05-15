from ..repository.product_category_repository import ProductCategoryRepository


class ProductCategoryService:

    def __init__(self):
        self.product_category_repository = ProductCategoryRepository()

    def get_all(self):
        product_unity_list = self.product_category_repository.get_all()
        return [product_unity.to_json() for product_unity in product_unity_list]

    def get_one(self, description):
        product_unity = self.product_category_repository.get_one(description)
        return product_unity.to_json()

    def add(self, body):
        # TODO verificar se já existe se sim retornar e não adicionar
        product_unity = self.product_category_repository.insert(body['description'])
        return product_unity.to_json()

    def update(self, body):
        product_unity = self.product_category_repository.update(body['old_description'], body['new_description'])
        return product_unity.to_json()

    def delete(self, description):
        if self.product_category_repository.get_one(description) is not None:
            product_unity = self.product_category_repository.delete(description)
            return product_unity.to_json()
        else:
            return "This product_unit doesn't exists"