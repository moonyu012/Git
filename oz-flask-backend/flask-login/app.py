from flask import Flask
from flask_login import LoginManager # pip install flask-login
from models import User


app = Flask(__name__)
app.secret_key = 'flask-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader # 로그인 할떄 실행됨
def load_user(user_id): # 유저 데이터를 가져와서 넘겨줌
    return User.get(user_id)

from routes import configure_route
configure_route(app)

if __name__=="__main__":
    app.run(debug=True)