from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token #JWT 토큰을 생성하는 함수
from models import User
from werkzeug.security import check_password_hash

auth_blp = Blueprint('auth', 'auth',
                     url_prefix='/login', description='Operations on todos')

@auth_blp.route('/', methods=['POST'])
def login():
    if not request.is_json: # JSON 형식인지 확인 아닐시 400 에러 반환
        print('if not request.is_json')
        return jsonify({"msg": "Missing JSON in request"}), 400
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        print('if not username or not password')
        return jsonify({"msg":"Missing username or password"}), 400
    

    user = User.query.filter_by(username=username).first() # 데이터베이스에서 유저네임과 일치하는 사용자 객체 조회
    print('user 여기는오나', user)
    print('user 여기는오나', check_password_hash(user.password_hash, password))
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=username) # 실제로 비민번호가 일치하면 토큰발급
        print('access_token', access_token)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Bad username or password"}), 401