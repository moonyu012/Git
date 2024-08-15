# Model -> Table 생성
# 게시글 - board
# 유저 - user

# 각각의 모델이 하나의 테이블
from db import db

class User(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable= False) # 널 값은 안됨
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy = 'dynamic') # 역참조 boards 는 author를 참조하고 author는 boards를 참고

class Board(db.Model):
    __tablename__="boards"

    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship('User', back_populates='boards') # 유저를 참조를 해줘 저 boards를 가진 녀석을