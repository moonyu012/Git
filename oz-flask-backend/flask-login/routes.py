from flask import render_template, request, redirect, url_for, flash
from models import User, users
from flask_login import login_user, logout_user, login_required

def configure_route(app): # app 객체를 받음
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login', methods=['GET','POST'])
    def login():
        if request.method == 'POST':  # 매소드가 포스트인 경우에
            username = request.form['username'] # 유저이름과 패스워드를 받아옴
            password = request.form['password']

            user = User.get(username)  # 유저네임을 넘겨주면 유저 정보가 넘어옴 (models.py)

            if user and users[username]['password'] == password: # 유저데이터의 비밀번호와 실제 유저가 보낸 비밀번호가 일치하면
                login_user(user)  # 로그인 성공

                return redirect(url_for('index'))
            else:
                flash('Invalid username or password')

        return render_template('login.html')
    
    @app.route('/logout')
    def logout():
        logout_user() # 플라스크 제공 함수
        return redirect(url_for('index')) # 로그인이 성공하면 인덱스 페이즈로

    @app.route('/protected')
    @login_required # 로그인이 필요합니다.
    def protected():
        return "<h1>Protected area</h1> <a href='/logout'>Logout</a>"