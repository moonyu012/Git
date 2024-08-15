# blocklist.py
# 이 파일은 JWT 토큰을 블록리스트 관리하는데 사용됩니다.

# BLOCKLIST 세트를 정의합니다. 이 세트는 폐기된 JWT 토큰의 'jti' (JWT ID)를 저장합니다.
BLOCKLIST = set()


def add_to_blocklist(jti):
    """블록리스트에 JWT ID(jti)를 추가하는 함수입니다."""
    BLOCKLIST.add(jti)


def remove_from_blocklist(jti):
    """블록리스트에서 JWT ID(jti)를 제거하는 함수입니다."""
    BLOCKLIST.discard(jti)
