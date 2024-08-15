from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Todo, User, db

todo_blp = Blueprint('todo', 'todo', url_prefix='/todo', description='Operations on todos')

@todo_blp.route('/', methods= ['POST'])
@jwt_required()
def create_todo():
    if not request.is_json: # 요청이 JSON 형식인지 확인 아닐시 400애러를 띄워줌
        return jsonify({"msg": "Missing JSON in request"}), 400
    
    title = request.json.get('title', None)
    if not title:
        return jsonify({"msg": "Missing title"}), 400
    
    username = get_jwt_identity() # 현재 인증된 사용자의 식별자를 가져옴
    user = User.query.filter_by(username=username).first() # db에서 유저네임을 기준으로 사용자 조회 쿼리의 첫번째 결과 반환

    new_todo = Todo(title=title, user_id=user.id)
    db.session.add(new_todo) #세션에 추가하고
    db.session.commit() # 변경사항을 커밋하여 데이터베이스애 저장

    return jsonify({"msg": "Todo created", "id": new_todo.id}), 201


# Todo 조회 (GET)
@todo_blp.route('/', methods=['GET'])
@jwt_required()
def get_todos():
    username = get_jwt_identity() # 토큰을 베이스로 유저 정보를가져오고
    user = User.query.filter_by(username=username).first()
    todos = Todo.query.filter_by(user_id=user.id).all() # 그 사람의 전체데이터를 볼 수 있음
    return jsonify([{"id": todo.id, "title": todo.title, "completed": todo.completed} for todo in todos])

# Todo 수정 (PUT)
@todo_blp.route('/<int:todo_id>', methods = ['PUT'])
@jwt_required()
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if 'title' in request.json:
        todo.title = request.json['title']
    if 'completed' in request.json:
        todo.completed = request.json['completed']
    db.session.commit()
    return jsonify({"msg": "Todo updated", "id": todo.id})

# Todo 삭제 (DELETE)
@todo_blp.route('/<int:todo_id>', methods=['DELETE'])
@jwt_required() # 인증된 유저만 접근
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"msg": "Todo deleted", "id": todo_id})