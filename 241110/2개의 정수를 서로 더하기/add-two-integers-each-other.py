a, b = map(int, input().split())  # 정수 a, b를 입력받아 각각 저장
a += b  # b를 a에 더하여 a를 업데이트
b += a  # a를 b에 더하여 b를 업데이트
print(a, b)  # 최종적으로 업데이트된 a와 b를 출력