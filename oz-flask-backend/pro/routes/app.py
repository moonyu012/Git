# 필요한 라이브러리와 모듈들을 임포트
from flask import Flask
from database import db
from flask_smorest import Api
from routes.product_routes import product_blp
from routes.cart_routes import cart_blp
from routes.order_routes import order_blp
from routes.user_routes import user_blp
from flask_migrate import Migrate
from jwt_utils import configure_jwt
import warnings

# 경고 메시지를 필터링하여 무시
# 특정 경고 메시지를 숨김 (여기서는 'Multiple schemas resolved to the name' 경고)
# 만약 경고 메시지를 숨기지 않으면 Swagger UI에 경고 메시지가 표시됨
warnings.filterwarnings("ignore", message="Multiple schemas resolved to the name ")

# Flask 앱 생성
app = Flask(__name__)

# 데이터베이스 설정
# MySQL 데이터베이스에 연결하기 위한 URI 설정
app.config["SQLALCHEMY_DATABASE_URI"] = "DB 주소"
# SQLAlchemy의 객체 추적 기능 비활성화
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# API와 관련된 설정
# API의 제목 설정
app.config["API_TITLE"] = "Shopping Mall API"
# API의 버전 설정
app.config["API_VERSION"] = "v1"
# OpenAPI 문서의 버전 설정
app.config["OPENAPI_VERSION"] = "3.0.2"
# Swagger UI 경로 설정
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# JWT 관련 설정을 앱에 적용
configure_jwt(app)

# 데이터베이스 초기화 및 마이그레이션 설정
db.init_app(app)
migrate = Migrate(app, db)

# Flask-Smorest API 초기화
# API 문서의 제목과 버전을 명시적으로 설정
api = Api(app, spec_kwargs={"title": "원하는 제목", "version": "v1"})


# 스키마 이름 해결 함수 정의
# 스키마 이름 충돌 문제를 해결하기 위해 각 스키마의 클래스 이름을 반환하는 함수
def schema_name_resolver(schema):
    return type(schema).__name__


api.spec.components.schema_name_resolver = schema_name_resolver

# 블루프린트 등록
# 각 기능별로 정의된 블루프린트를 Flask 앱에 등록
api.register_blueprint(product_blp)
api.register_blueprint(cart_blp)
api.register_blueprint(order_blp)
api.register_blueprint(user_blp)

# 메인 실행 블록
if __name__ == "__main__":
    # 앱 컨텍스트 내에서 데이터베이스 테이블 생성
    with app.app_context():
        db.create_all()
    # 앱을 디버그 모드로 실행
    app.run(debug=True)
