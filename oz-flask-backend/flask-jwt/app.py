from flask import Flask, render_template  # pip install flask-jwt-extended
from jwt_utils import configure_jwt
from routes.user import User_bp

app = Flask(__name__)
configure_jwt(app)

app.register_blueprint(User_bp, url_prefix='/user')

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)