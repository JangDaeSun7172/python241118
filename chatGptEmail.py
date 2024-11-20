import re

def is_valid_email(email):
    # 이메일 주소 패턴 (간단한 검증용)
    #raw string notation: 소문자 r을 붙이는 표현식
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# 샘플 이메일 리스트
emails = [
    "example@example.com",  # 유효
    "user.name+tag@sub.domain.com",  # 유효
    "user123@domain.io",  # 유효
    "user@domain",  # 유효하지 않음 (도메인 형식이 아님)
    "user@.com",  # 유효하지 않음 (잘못된 도메인)
    "@example.com",  # 유효하지 않음 (사용자 이름 없음)
    "user@domain.c",  # 유효하지 않음 (도메인 이름 너무 짧음)
    "user@domain.com.",  # 유효하지 않음 (마침표로 끝남)
    "plainaddress",  # 유효하지 않음 (이메일 형식 아님)
    "user@domain...com",  # 유효하지 않음 (연속된 점)
]

# 이메일 유효성 검사
for email in emails:
    print(f"{email}: {'유효함' if is_valid_email(email) else '유효하지 않음'}")

