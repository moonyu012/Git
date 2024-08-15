# jwtutils.py
# 이 파일은 JWT 관련 설정 및 콜백 함수들을 정의합니다.

from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST
from flask import jsonify

# JWTManager 인스턴스를 생성합니다.
jwt = JWTManager()


def configure_jwt(app):
    """JWT를 구성하는 함수입니다."""
    # JWT 비밀키 설정
    app.config["JWT_SECRET_KEY"] = "your-secret-key"
    # JWTManager를 Flask 앱에 초기화
    jwt.init_app(app)

    # 토큰 만료 시간 설정
    freshness_in_minutes = 60
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = freshness_in_minutes * 60  # 1시간

    # 추가적인 정보를 JWT 토큰에 포함시키고 싶을 때 사용하는 함수
    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    # 토큰이 블록리스트에 있는지 확인하는 함수
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    # 만료된 토큰을 사용할 경우 실행되는 콜백 함수
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"msg": "Token expired", "error": "token_expired"}), 401

    # 유효하지 않은 토큰을 사용할 경우 실행되는 콜백 함수
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"message": "Invalid token", "error": "invalid_token"}), 401

    # 인증되지 않은 토큰을 사용할 경우 실행되는 콜백 함수
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Access token required",
                    "error": "access_token_required",
                }
            ),
            401,
        )

    # fresh 토큰이 필요한 상황에서 fresh하지 않은 토큰을 사용할 경우 실행되는 콜백 함수
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "Token is not fresh.", "error": "fresh_token_required"}
            ),
            401,
        )

    # 폐기된 토큰을 사용할 경우 실행되는 콜백 함수
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "Token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )
