from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy #ORM(Object-Relational Mapping) 라이브러리
from flask_jwt_extended import JWTManager # JWT(Json Web Token)를 사용하여 인증 및 권한 부여를 관리할 수 있도록 도와줌
from flask_smorest import Api #RESTful API를 설계하고 구현하는 데 도움을 주는 도구
from db import db # SQLAlchemy 인스턴스를 포함하는 객체 / db = SQLAlchemy()와 같은 형태로 초기화되며, 이를 통해 모델 클래스와 데이터베이스 작업을 설정하고 관리
from flask_migrate import Migrate # 데이터베이스를 마이그레이션하는 작업을 수월하게 수행

app = Flask(__name__)

# 데이터베이스 밒 JWT 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' # local sb => 파일 형태의 간단한 데이터 베이스
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['API_TITLE'] = 'Todo API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'

# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
api = Api(app)

# 모델 및 리소스 불러오기 (이후에 정의)
from models import User, Todo
from routes.auth import auth_blp
from routes.todo import todo_blp

# API에 Blueprint 등록
api.register_blueprint(auth_blp)
api.register_blueprint(todo_blp)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)