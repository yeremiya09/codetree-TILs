# 두 정수 입력 받기
a, b = map(int, input().split())

# 곱 계산
product = int(a * b)
# 몫 계산
quotient = int(a / b)

# 출력 형식에 맞춰 결과 출력
print(f"{a} * {b} = {product}")
print(f"{a} / {b} = {quotient}")