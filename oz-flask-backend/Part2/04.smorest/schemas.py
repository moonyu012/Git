
from marshmallow import Schema, fields

class ItemSchema(Schema):
		# id 필드가 직렬화(즉, Python 객체에서 JSON으로 변환) 과정에서만 사용되고, (서버->클라)
		# 역직렬화(즉, JSON에서 Python 객체로 변환) 과정에서는 무시된다 (클라->서버)
		# 즉, id 값은 서버에서 관리하겠다는 뜻
    id = fields.Int(dump_only=True) # 스키마는 이름을 필수로 받기로 했는데 빠드린다거나
    name = fields.Str(required=True) # 문자열을 받기로했는데 다르게 넘어오는 그런 예외의 경우를 방지해줌
    description = fields.Str()