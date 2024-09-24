# 날짜 정보를 mm-dd-yyyy 형태로 입력받음
date_input = input()

# 입력된 날짜를 '-'를 기준으로 나눔
mm, dd, yyyy = date_input.split("-")

# 결과를 yyyy.mm.dd 형식으로 출력
print(f'{yyyy}.{mm}.{dd}')