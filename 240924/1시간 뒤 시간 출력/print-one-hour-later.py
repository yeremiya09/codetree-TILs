# 시간과 분을 h:m 형태로 입력받음
time_input = input()

# 입력된 시간을 ':'를 기준으로 나눔
h, m = map(int, time_input.split(':'))

# 1시간을 더해줌
h += 1

# 시간은 23을 넘을 수 없으므로 23 이하로 유지
if h > 23:
    h = 0

# 결과 출력
print(f"{h}:{m}")