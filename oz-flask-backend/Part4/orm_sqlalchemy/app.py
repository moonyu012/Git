from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:20153681@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


db.init_app(app)
migrate = Migrate(app, db)

# bluepring 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

# api.register_blueprint()
from routes.board import board_blp
from routes.user import user_blp
api.register_blueprint(board_blp)
api.register_blueprint(user_blp)

from flask import render_template
@app.route('/manage-boards')   # get으로 접근이 가능한 두개의 라우터 /manage-boards 들어가면 borads.html 실행이 됨
def manage_boards():
    return render_template('boards.html')   

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

if __name__=='__main__':
    with app.app_context():  # db가 생성되어있고 원하는대로 모델이 반영이되어 있으면 그대로 가고 아니면 패스한다.
        db.create_all() # 모델스에 만들어둔 두 테이블이 만들어 진다
    
    app.run(debug=True)
