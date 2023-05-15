from flask import Blueprint, request
from ..service.product_unit_service import ProductUnitService
import json

product_unit_bp = Blueprint('product_unit', __name__, url_prefix="/product_unit")
pus = ProductUnitService()


@product_unit_bp.route("/", methods=["GET"])
def get_all():
    return pus.get_all()


@product_unit_bp.route("/<string:description>", methods=["GET"])
def get_one(description):
    return pus.get_one(description)


@product_unit_bp.route("/", methods=["POST"])
def create():
    body = json.loads(request.data)
    return pus.add(body)


@product_unit_bp.route("/", methods=["PUT"])
def update():
    body = json.loads(request.data)
    return pus.update(body)


@product_unit_bp.route("/<string:description>", methods=["DELETE"])
def remove(description):
    return pus.delete(description)
