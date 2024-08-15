from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')  # 블루프린트를 사용하여 api를 기능 단위로 묶어주기 위함

books = []

@book_blp.route('/')
class BookList(MethodView):
    @book_blp.response(200, BookSchema(many=True))  # 뷱스에 저장돼어 있는 여러 데이터를 보여줘도 된다
    def get(self):
        return books

    @book_blp.arguments(BookSchema)
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id'] = len(books) + 1
        books.append(new_data)  # 유저가 보낸 데이터를 담기
        return new_data

@book_blp.route('/<int:book_id>')
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        return book

    @book_blp.arguments(BookSchema)  # 검증
    @book_blp.response(200, BookSchema) # 검증
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        book.update(new_data)
        return book

    @book_blp.response(204)
    def delete(self, book_id):
        global books
        book = next((book for book in books if book['id'] == book_id), None)  # 북스안에 아이디 값이 존재하면 그 값을 삭제
        if book is None:
            abort(404, message="Book not found.")
        books = [book for book in books if book['id'] != book_id]
        return ''