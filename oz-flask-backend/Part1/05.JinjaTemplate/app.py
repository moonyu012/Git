from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        'title': 'Flask Jinja Template',
        'user': 'yujin',
        'is_admin': True,
        'item_list': ["Item1", "Item2", "Item3"]
    }

    # 템플릿 파일과 전달할 데이터 설정
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
