from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

# API List      
# /board/
# 전체 게시글을 가져오는 API (GET)
# 게시글 작성 (POST)
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()

        # for board in boards:
        #     print('id',board.id)
        #     print('title',board.title)
        #     print('content',board.content)
        #     print('user_id',board.user_id)
        #     print('author_name',board.author.name) # User
        #     print('author_email',board.author.email)  # User

        return jsonify([{"id":board.id, 
                         'title':board.title,
                         'content':board.content,
                         'user_id': board.author.id, 
                         'author_name': board.author.name,
                         'author_email': board.author.email} 
                         for board in boards])

    
    def post(self):
        data = request.json # 유저한테 데이터 받아옴
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id']) # 새 객체가 만들어짐
        db.session.add(new_board) # 여기다가 추가
        db.session.commit() # 최종 db 추가

        return jsonify({'msg': 'success create board'}), 201



#/board/<int: board_id>
# 하나의 게시글 불러오기 (GET)
# 특정 게시글 수정하기 (PUT)
# 특정 게시글 삭제하기 (DELETE)
@board_blp.route("/<int:board_id>")
class BoardResource(MethodView):
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)  # 보드에서 특정한 아이디를 가진 그 게시글 데이터를 불러옴

        return jsonify({'id':board.id, 
                        'title':board.title,
                        'content':board.content, 
                        'author_name': board.author.name
                         })

    def put(self, board_id):
        board = Board.query.get_or_404(board_id)
        data = request.json

        board.title = data['title']  # 유저가 보낸 값으로 키 값이 title인것을 덮어쓰기
        board.content = data['content']

        db.session.commit()

        return jsonify({'msg':'Successfully updated board data'}), 201


    
    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()

        return jsonify({"msg":"Successfully deleted board data"}), 204