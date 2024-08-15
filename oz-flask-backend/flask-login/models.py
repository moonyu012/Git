from flask_login import UserMixin # 플라스크로그인 모듈에서 유저믹스인 객체를 불러옴

users = {'admin': {'password':'pw123'}}

class User(UserMixin): # 불러온 객체를 상속 받음
    def __init__(self, username):
        self.id = username
    
    @staticmethod
    def get(user_id): # 유저 아이디를 받아와서 유저아이디가 유저에 존재하면
        if user_id in users:
            return User(user_id) # 유저아이디 값을 가지고 유저아이디에 해당하는 유저데이터를 넘겨줘라
        
        return None