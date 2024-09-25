# 주민번호를 입력받음
id_number = input()

# '-'를 제외한 상태로 출력
result = id_number.replace('-', '')
print(result)