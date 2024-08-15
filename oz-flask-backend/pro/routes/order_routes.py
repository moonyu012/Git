from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request, jsonify
from database import db
from models import Order, OrderDetail, Cart
from flask_jwt_extended import jwt_required, get_jwt_identity

order_blp = Blueprint("orders", "orders", url_prefix="/orders/")


@order_blp.route("<int:order_id>", methods=["GET", "POST"])
class OrderList(MethodView):
    @jwt_required()
    def get(self, order_id):  # order_id를 메소드 인자로 추가
        pass

    @jwt_required()
    def post(self, order_id):
        pass

