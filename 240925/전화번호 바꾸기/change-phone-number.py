# 전화번호를 입력받음
phone_number = input()

# '-'을 기준으로 분리
parts = phone_number.split('-')

# 앞과 뒤 자리를 바꾸어 출력
result = f"{parts[0]}-{parts[2]}-{parts[1]}"
print(result)