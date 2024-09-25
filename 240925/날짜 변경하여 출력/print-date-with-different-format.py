# 날짜를 입력받음
date_input = input()

# yyyy, mm, dd로 나누기
yyyy, mm, dd = date_input.split('.')

# mm-dd-yyyy 형식으로 출력
result = f"{mm}-{dd}-{yyyy}"
print(result)