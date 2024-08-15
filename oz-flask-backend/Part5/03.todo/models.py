from db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable = False)
    password_hash = db.Column(db.String(128)) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  # 비밀번호를 해시화 해서 불러옴

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) # 유저가 입력해준 비밀번호를 가지고 해시번호와 일치한지 확인
    
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) # 어떤 유저가 작성했는지