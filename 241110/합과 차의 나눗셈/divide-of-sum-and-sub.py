# 두 정수를 입력받습니다.
a, b = map(int, input().split())

# (a+b) / (a-b)의 값을 계산하여 소수점 둘째 자리까지 반올림한 결과를 출력합니다.
result = (a + b) / (a - b)
print(f"{result:.2f}")