from flask import Blueprint

price_bp = Blueprint('price', __name__,url_prefix="/price")


@price_bp.route("/", methods=["GET"])
def get_all():
    return '<h1>Hello Price</h1>'
