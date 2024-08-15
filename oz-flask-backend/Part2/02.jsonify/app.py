from flask import Flask, jsonify, request

app = Flask(__name__)

# GET
# (1) 전체 게시글을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result':'success','data':{'feed1':'data1','feed2':'data2'}}

    return data  # jsonify(data)이렇게 써야하지만 이미 딕셔너리 형태기 떄문에 사용안해도 자동으로 변환

# (2) 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result':'success','data':{'feed1':'data1'}}

    return data

# POST
# (2) 게시글을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']

    print(name, age)

    return jsonify({'result':'success'})

datas = [{"items": [{"name": "item1", "price": 10}]}]

@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return {"datas":datas}

@app.route('/api/v1/datas', methods=['POST'])
def create_data():
    request_data = request.get_json()

    new_data = {'items': request_data.get("items",[])}
    datas.append(new_data)

    return new_data, 201