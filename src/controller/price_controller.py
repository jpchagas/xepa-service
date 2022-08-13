from flask import Blueprint
from ..service.price_service import PriceService

price_bp = Blueprint('price', __name__, url_prefix="/price")


@price_bp.route("/", methods=["GET"])
def get_all():
    return PriceService.list_all()


@price_bp.route("/", methods=["GET"])
def get_one():
    return PriceService.get_one()


@price_bp.route("/", methods=["POST"])
def create():
    return PriceService.add()


@price_bp.route("/", methods=["PUT"])
def update():
    return PriceService.change()


@price_bp.route("/", methods=["DELETE"])
def remove():
    return PriceService.remove()
