# 블록라스트 관리 파일  토큰 관리해주는 파이

BLCOKLIST = set()

def add_to_blocklist(jti):  # jti jwt의 교유한 값들을 의미 jwt를 관리할 수 있게해주는 고유 넘버
    BLCOKLIST.add(jti)

def remove_from_blocklist(jti):
    BLCOKLIST.discard(jti)