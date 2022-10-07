from flask import Blueprint, request
from ..service.product_service import ProductService
import json

product_bp = Blueprint('product', __name__, url_prefix="/product")


@product_bp.route("/", methods=["GET"])
def get_all():
    ps = ProductService()
    return ps.list_all()


@product_bp.route("/", methods=["GET"])
def get_one():
    return ProductService.get_one()


@product_bp.route("/", methods=["POST"])
def create():
    body = json.loads(request.data)
    ps = ProductService()
    ps.add(body)
    return "Adding price"


@product_bp.route("/", methods=["PUT"])
def update():
    return ProductService.change()


@product_bp.route("/", methods=["DELETE"])
def remove():
    return ProductService.remove()