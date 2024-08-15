from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from models import Cart


# Cart 모델에 대한 스키마 정의
class CartSchema(SQLAlchemyAutoSchema):
    pass

