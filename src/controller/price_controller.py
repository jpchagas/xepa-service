from flask import Blueprint, request
from ..service.price_service import PriceService
import json

price_bp = Blueprint('price', __name__, url_prefix="/price")


@price_bp.route("/", methods=["GET"])
def get_all():
    ps = PriceService()
    return ps.list_all()


@price_bp.route("/", methods=["GET"])
def get_one():
    return PriceService.get_one()


@price_bp.route("/", methods=["POST"])
def create():
    body = json.loads(request.data)
    ps = PriceService()
    ps.add(body)
    return "Adding price"


@price_bp.route("/", methods=["PUT"])
def update():
    return PriceService.change()


@price_bp.route("/", methods=["DELETE"])
def remove():
    return PriceService.remove()
