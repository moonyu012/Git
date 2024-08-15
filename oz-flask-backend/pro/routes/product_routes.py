from flask_smorest import Blueprint
from flask.views import MethodView
from schemas.product_schema import (
    ProductSchema,
    AddToCartSchema,
    AddProductSchema,
    ResponseMessageSchema,
)
from flask import request, jsonify
from models import Product
from models import Cart, db
from flask_jwt_extended import jwt_required, get_jwt_identity


product_blp = Blueprint(
    "products", "products", url_prefix="/products/", description="상품 관리"
)


@product_blp.route("list/", methods=["GET"])
class ProductList(MethodView):
    def get(self, *args):
        pass




@product_blp.route("list/<int:product_id>/", methods=["GET"])
class ProductDetail(MethodView):
    @product_blp.response(200, ProductSchema())
    def get(self, product_id):
        pass


@product_blp.route("add/", methods=["POST"])
class AddProduct(MethodView):
    @product_blp.arguments(AddProductSchema)
    @product_blp.response(201, ResponseMessageSchema)
    def post(self, args):
        pass


@product_blp.route("add-to-cart/", methods=["POST"])
class AddToCart(MethodView):
    @jwt_required()
    @product_blp.arguments(AddToCartSchema)
    def post(self, args):
         pass

