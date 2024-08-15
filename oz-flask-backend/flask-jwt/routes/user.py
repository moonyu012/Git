from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from models.user import User

User_bp = Blueprint('user', __name__)

# 데이터베이스 연동을 하지 않아서 임시 사용자 데이터
users = {
    'user1': User('1', 'user1', 'pw123'),
    'user2': User('2', 'user2', 'pw123')
}

@User_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':  # 유저가 보내준 유저이름과 패스워드를 가져와서 
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = users.get(username) # 이걸 기반으로 유저 데이터 값을 가져옴
        if user and user.password == password:  # 유저데이터 안에서 패스워드가 동일하다고 하면
            access_token = create_access_token(identity=username) # 두가지 토큰을 발급을 해줌 처음 발급 만료 전까지
            refresh_token = create_refresh_token(identity=username) # 만료 후 재발급을 도와주는 토큰
            return jsonify(access_token=access_token, refresh_token=refresh_token) # 일치시 토큰을 내려줌
        else:
            return jsonify({"msg": "Bad username or password"}), 401 # 없으면 에러띄움
    else:
        return render_template('login.html') # get으로 접근시 띄워줌
    
@User_bp.route('/protected', methods=['GET'])
@jwt_required() # 인증되지 않은 사용자가 보호된 페이지로 들어갈려고 하면 막아줘야함
def protected(): # 인증된 유저인지 아닌지 판별
    current_user = get_jwt_identity()  # 이 사람의 현재 정보를 알 수 있음
    return jsonify(logged_in_as=current_user), 200 # 이 유저가 현재 접속을 했다

@User_bp.route('/protected_page')
def protected_page(): # 프로텍트 페이지 랜더링
    return render_template('protected.html')

from flask_jwt_extended import get_jwt
from blocklist import add_to_blocklist # 블랙리스트 관리 모듈 임포트
@User_bp.route('/logout', methods=['POST']) 
@jwt_required()    # 로그아웃을 할때 토큰값을 가져와서
def logout():       
    jti = get_jwt()["jti"]  # 여러가지 토큰 리스트 중에서 내가 원하는 토큰을 가져와서 로그아웃시 블랙리스트에 추가
    add_to_blocklist(jti) # jti를 블랙리스트에 추가
    return jsonify({"msg": "Successfully logged out"}), 200 # 이 토큰은 만료가 되었다를 알려줌