from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from marshmallow import Schema, fields
from models import User


# User 모델에 대한 스키마 정의
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        # SQLAlchemy 모델 지정
        model = User
        # 직렬화된 데이터를 모델 인스턴스로 로드
        load_instance = True
        # 스키마 이름 설정
        name = "UserSchema"

    # Nested 필드를 사용하여 관련된 모델을 포함
    carts = Nested("CartSchema", many=True, exclude=("user",))
    orders = Nested("OrderSchema", many=True, exclude=("user",))


class RegisterSchema(Schema):
    username = fields.String(required=True, description="사용자의 유저네임")
    password = fields.String(required=True, description="사용자의 비밀번호")


class LoginSchema(Schema):
    username = fields.String(required=True, description="사용자의 유저네임")
    password = fields.String(required=True, description="사용자의 비밀번호")
