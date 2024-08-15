from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True)  # 서버에서 직접 관리 할거야
    title = fields.String(required=True)  # 데이터를 반드시 받을 수 있게함
    author = fields.String(required=True)