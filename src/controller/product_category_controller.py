from flask import Blueprint, request
from ..service.product_category_service import ProductCategoryService
import json

product_category_bp = Blueprint('product_category', __name__, url_prefix="/product_category")
pcs = ProductCategoryService()


@product_category_bp.route("/", methods=["GET"])
def get_all():
    return pcs.get_all()


@product_category_bp.route("/<string:description>", methods=["GET"])
def get_one(description):
    return pcs.get_one(description)


@product_category_bp.route("/", methods=["POST"])
def create():
    body = json.loads(request.data)
    return pcs.add(body)


@product_category_bp.route("/", methods=["PUT"])
def update():
    body = json.loads(request.data)
    return pcs.update(body)


@product_category_bp.route("/<string:description>", methods=["DELETE"])
def remove(description):
    return pcs.delete(description)
