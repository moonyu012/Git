from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, request
from database import db
from models import Order, Cart, OrderDetail
from flask_jwt_extended import jwt_required, get_jwt_identity

cart_blp = Blueprint("carts", "carts", url_prefix="/carts/", description="장바구니 관리")


@cart_blp.route("", methods=["GET", "POST"])
class CreateOrder(MethodView):
    @jwt_required()
    def get(self):
        pass   

    @jwt_required()
    def post(self):
        pass


@cart_blp.route("<int:product_id>/", methods=["PUT", "DELETE"])
class CartManagement(MethodView):
    @jwt_required()
    def put(self, product_id):
        pass
    @jwt_required()
    def delete(self, product_id):
        pass