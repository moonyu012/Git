from flask_smorest import Blueprint, abort
from flask import request

def create_user_blueprint(mysql):
    user_blp = Blueprint("user_routes", __name__, url_prefix='/users') # 1.별칭, 2, 모듈명이 인수로 전달 3. url앞에 기본으로 붙일 접두어 url


    # 전체 유저 데이터를 불러오는 코드
    @user_blp.route('/', methods=['GET'])
    def get_users():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall() # return 결과 타입은 => 튜플
        cursor.close()


        

        users_list = []
        for user in users:  # REST API => {}
            users_list.append({
                'id' : user[0],
                'name' : user[1],
                'email' : user[2]
            })

        return users_list

        
    # 유저를 생성하는 함수
    @user_blp.route("/", methods=['POST'])
    def add_user():
        user_data = request.get_json() # 유저가 보낸 데이터를 받아오게 된다.

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users(name, email) VALUES(%s, %s)",
                   (user_data['name'], user_data['email'])) # users라는 테이블에 데이터를 담아주세요
        mysql.connection.commit()
        cursor.close()
        
        return {"msg":"successfully added user"}, 201
   

    # 유저를 업데이트하는 함수 (UPDATE)
    @user_blp.route('/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user_data = request.get_json()

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s",
                       (user_data['name'], user_data['email'], user_id))
        
        mysql.connection.commit()
        cursor.close()

        return {"msg":"successfully updated user"}, 201
    
    # 유저를 삭제하는 함수 (DELETE)
    @user_blp.route('/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id, ))
        mysql.connection.commit()
        cursor.close()

        return {"msg":"successfully deleted user"}, 201
    return user_blp
