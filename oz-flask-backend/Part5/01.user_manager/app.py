from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # app 모듈을 불러옴

# 임시 사용자 데이터
user = [
    {"username": "traveler", "name":"Alex"},
    {"username": "photographer", "name":"Sam"},
    {"username": "gourmet", "name":"Chris"}
]

@app.route('/')
def index():
    # 사용자 목록을 보여주는 루트 뷰
    return render_template('index.html', users = users)

@app.route('/add', methods=['GET','POST'])
def add_user():
    # 사용자 추가 뷰
    if request.method == 'POST':
        username = request.form['username']  # 유저가 보낸 유저네임과 네임 데이터를 받고
        name = request.form['name']
        users.append({'username': username, 'name': name}) # 추가
        return redirect(url_for('index')) # 인덱스 페이지 띄워줌
    return render_template('add_user.html') # get시 add_user 페이지 띄워줌

@app.route('/edit/<username>', methods=['GET','POST']) # 에딕하고 유저이름을 보내면
def edit_user(username):
    # 사용자 수정 뷰    # 그 값을 가지고 유저를 찾음 next함수: 이 안에서 값이 존재하면 반복문 멈추고 값을 가지고 오고 아닌 경우 None 리턴
    user = next((user for user in users if user['username'] == username), None) 
    if not user:
        return redirect(url_for('index'))
    
    if request.method == 'POST':  # 이 사람이 데이터를 변경하고 싶은걸 인지
        user['name'] = request.form['name']  # 그 값을 받아와서 그 유저에다가 덮어쓰기 해줌
        return redirect(url_for('index'))
    
    return render_template('edit_user.html', user=user)

@app.route('/delete/<username>')  # 유저네임 값을 받아옴
def delete_user(username):
    # 사용자 삭제 뷰
    global users  # 전체 영역에서 관리가 됨
    users = [user for user in users if user['username'] != username] # 실제 존재하는지 확인 있으면 삭제
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)