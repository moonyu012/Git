# schemas/product_schema.py
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from models import Product
from schemas.cart_schema import CartSchema
from marshmallow import Schema, fields


# Product 모델에 대한 스키마 정의
class ProductSchema(SQLAlchemyAutoSchema):
    pass




# swagger에서 사용할 스키마 정의
class AddProductSchema(Schema):
    pass

class AddToCartSchema(Schema):
    pass

# 응답 메시지 스키마
    pass

# 에러 응답 스키마
    pass
