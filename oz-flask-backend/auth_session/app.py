from flask import Flask, render_template, request, redirect, session, flash
# html,  유저가 보낸 데이터, 로그인 후 메인페이지로 가기 위함 , flask에서 제공하는 모듈, redirect 하기전에 안내 메세지 띄워주는 모듈
from datetime import timedelta
app = Flask(__name__)

app.secret_key = 'flask-secret-key' # 실제로 배포시에는 .env or yaml
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) # 로그인한번하고 지속되는 시간 설정
# admin user
users = {
    'john':'pw123',
    'leo': 'pw123'
}

@app.route('/')  # 로그인하는 api
def index():
    return render_template("login.html") # 로그인 화면을 띄우줌

@app.route('/login', methods=['POST'])  # 유저 인증을 위한 api
def login():
    username = request.form['username']  # 유저 이름과 비밀번호
    password = request.form['password']

    if username in users and users[username] == password:  # 로그인 로직 구현 
        session['username'] = username # 만약 유저 이름이 이중에 포함이 되어 있는지 유저가 보낸 아이디가 비밀번호랑 일치 한지
        # 이사람의 유저이름을 가지고 세션이름을 만들어줌
        session.permanent = True # 세션 유지 기간을 활성화
        return redirect('/secret')
    else:  # 존재하지 않으면
        flash("Invalid username or password") # 로그인을 다시 하세요
        return redirect('/')
    
@app.route('/secret') # 인증된 유저가 떨어지는 페이지에 대한 라우터 작업
def secret():
    if 'username' in session: # 유저이름이 세션데이터 안에 존재하면 secret.html 이동시켜준다
        return render_template('secret.html')
    else:
        return redirect('/')  # 아닌데 들어올려고 하면 여기로 이동
    
# 로그아웃
@app.route('/logout')
def logout():
    session.pop('username', None)  # 유저이름을 None으로 비워줌
    return redirect('/') # 로그아웃시 로그인 페이지로 넘겨줌

if __name__=="__main__":
    app.run(debug=True)