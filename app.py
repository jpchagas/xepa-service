from flask import Flask
from .src.controller.price_controller import price_bp

app = Flask(__name__)
app.register_blueprint(price_bp)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
