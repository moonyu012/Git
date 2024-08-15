from flask import Flask
from flask_restful import Api
from resources.item import Item  # 리소스 폴더 아이템파일에서 아이템 클래스를 불러 와줘

app = Flask(__name__)


api = Api(app)

    
api.add_resource(Item,'/item/<string:name>') # 경로 추가
