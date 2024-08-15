from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt,
    get_jwt_identity,
)
from models import User, db
from blocklist import BLOCKLIST
from schemas import user_schema

# 사용자 관련 라우트를 정의하는 블루프린트 생성
user_blp = Blueprint("users", "users", url_prefix="/users/", description="사용자 관리")


# 회원가입을 처리하는 클래스
@user_blp.route("/register/", methods=["POST"])
class Register(MethodView):
    @user_blp.arguments(user_schema.RegisterSchema)
    def post(self, args):
        pass



# 로그인을 처리하는 클래스
@user_blp.route("/login/", methods=["POST"])
class Login(MethodView):
    @user_blp.arguments(user_schema.LoginSchema)
    def post(self, args):
        pass



# 로그아웃을 처리하는 클래스
@user_blp.route("/logout/", methods=["POST"])
class Logout(MethodView):
    @jwt_required()
    def post(self):
        pass



# 회원 탈퇴를 처리하는 클래스
@user_blp.route("/delete-account/", methods=["DELETE"])
class DeleteAccount(MethodView):
    @jwt_required()
    def delete(self):
        pass



# 마이페이지 정보를 보여주는 클래스
@user_blp.route("/my-page/", methods=["GET"])
class MyPage(MethodView):
    @jwt_required()
    def get(self):
        pass

