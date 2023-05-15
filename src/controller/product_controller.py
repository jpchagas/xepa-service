from flask import Blueprint, request
from ..service.product_service import ProductService
import json

product_bp = Blueprint('product', __name__, url_prefix="/product")
ps = ProductService()


@product_bp.route("/", methods=["GET"])
def get_all():
    return ps.get_all()


@product_bp.route("/<string:description>", methods=["GET"])
def get_one(description):
    return ps.get_one(description)


@product_bp.route("/", methods=["POST"])
def create():
    body = json.loads(request.data)
    return ps.add(body)


@product_bp.route("/", methods=["PUT"])
def update():
    return ps.update()


@product_bp.route("/<string:description>", methods=["DELETE"])
def remove(description):
    return ps.remove(description)
