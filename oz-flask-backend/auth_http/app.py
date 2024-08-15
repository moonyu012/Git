from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth # pip install flask-httpauth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'admin':'secret',
    'guest':'pw123'
}

@auth.verify_password # 인증모듈 사용
def verify_password(username, password):
    if username in users and users[username] == password: # 유저이름이 유저스에 있으면 유저스에서의 유저이름의 비밀번호가 일치한다면 
        return username
    return None

    

@app.route('/protected') # 로그인이 안된 유저가 들어오면 로그인을 요청함
@auth.login_required
def protected():
    return render_template('secret.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)