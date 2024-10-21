# 입력 받기
a, b = map(int, input().split())

# 몫과 나머지 계산
quotient = a // b
remainder = a % b

# 출력
print(f"{quotient}...{remainder}")