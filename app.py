from flask import Flask
from src.controller.price_controller import price_bp
from src.controller.product_controller import product_bp
from src.controller.product_unit_controller import product_unit_bp
from src.controller.product_category_controller import product_category_bp

app = Flask(__name__)
app.register_blueprint(price_bp)
app.register_blueprint(product_bp)
app.register_blueprint(product_unit_bp)
app.register_blueprint(product_category_bp)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run()
