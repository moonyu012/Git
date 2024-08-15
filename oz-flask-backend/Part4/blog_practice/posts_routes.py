from flask import request, jsonify
from flask_smorest import Blueprint, abort


# API CRUD

def create_posts_blueprint(mysql):
    posts_blp = Blueprint("posts",__name__,description="posts api",url_prefix="/posts",)


    @posts_blp.route("/", methods=["GET", "POST"])
    def posts():
        cursor = mysql.connection.cursor()

        # 게시글 조회
        if request.method == 'GET':
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            posts = cursor.fetchall()
            cursor.close()

            post_list = []

            for post in posts:
                post_list.append(
                    {
                        "id": post[0],
                        "title": post[1],
                        "content": post[2],
                    }
                )
            return jsonify(post_list)
        
        # 게시글 생성
        elif request.method =='POST':
            title = request.json.get("title")
            content = request.json.get("content")

            if not title or not content:
                abort(400, message="title 또는 content가 없습니다.")

            sql = "INSERT INTO posts(title, content) VALUES(%s, %s)"
            cursor.execute(sql, (title, content))
            mysql.connection.commit()

            return jsonify({"message": "successfully created post data","title": title,"content":content}), 201
        
    # 1번 게시글만 조회하고 싶은 경우
    # 게시글 수정 및 삭제

    @posts_blp.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
    def post(id):
        cursor = mysql.connection.cursor() # 커서 변수를 전역으로 만들어둠
        sql = f"SELECT * FROM posts WHERE id={id}" # 만약 아이디 값을 유저가 1번으로 보냈으면 1번 유저의 게시글이 보임
        cursor.execute(sql) # 실행
        post = cursor.fetchone() # 값을 데이터 하나만 받아옴

        if request.method == 'GET':
            
            if not post:  # 만약 비어있으면 404 발생
                abort(404, message="해당 게시글이 없습니다.")
            return {   # 포스트가 존재하는 경우 리턴
                "id": post[0],
                "title": post[1],
                "content": post[2],
            }

        elif request.method =='PUT': # 유저로 부터 받아온 데이터를 넘겨줌
            title = request.json.get("title")  # 유저가 json 형태로 data를 보냄
            content = request.json.get("content")

            if not title or not content: # 유저가 데이터가 빈 값을 보냈을 경우
                abort(400, message="title 또는 content가 없습니다.") # 에러와 메세지를 띄움

            if not post:
                abort(404, "NOT found post")

            sql = f"UPDATE posts SET title={title}, content={content} WHERE id = {id}"  # 쿼리를 작성해서 데이터 베이스에 업데이트 요청
            cursor.execute(sql) # sql문 실행해주세요
            mysql.connection.commit() # 실제로 업데이트

            return jsonify({"message": "Successfully updated title & content"})

        elif request.method == 'DELETE':
            if not post:
                 abort(400, message="title 또는 content가 없습니다.")

            sql = f"DELETE FROM posts WHERE id={id}" 
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({"message": "Successfully deleted post"})
    
    return posts_blp  # create_posts_blueprint 함수안의 posts_blp 리턴

            




