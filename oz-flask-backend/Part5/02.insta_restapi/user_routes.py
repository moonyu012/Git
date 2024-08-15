from flask import request
from user_model import users, add_user, add_post_to_user, get_user_posts, like_user_post, delete_user

def register_routes(app):
    @app.route("/users", methods=["GET","POST"])
    def users_route():
        if request.method == "GET":
            return{"users": users}
        elif request.method == "POST":
            request_data = request.get_json()
            return add_user(request_data)
        
    @app.route("/users/post/<string:username>", methods=["POST"])
    def add_post(username):
        request_data = request.get_json()
        return add_post_to_user(username, request_data)
    
    @app.route("/users/post/<string:username>", methods=["GET"])
    def get_posts(username):
        return get_user_posts(username)
    
    @app.route("/users/post/like/<string:username>/<string:title>", methods=["PUT"])
    def like_post(username, title):
        return like_user_post(username, title)
    
    @app.route("/users/<string:username>", methods=["DELETE"])
    def delete(username):
        return delete_user(username)