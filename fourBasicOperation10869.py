A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
# 파이썬의 경우 정수 둘을 나누고 떨어지지 않을 때 자동으로 float형으로 출력하여 줍니다.
# 예시 결과에 따라서 정수형으로 표현해 주어야 하기때문에
# int 함수로 묶어준다.
print(int(A / B))
print(int(A % B))
# 개행 문자(\n)를 활용하여 print를 한줄로 표현할 시
# 파이썬 또한 C언어처럼 개행문자와 함께 수를 표현할 수 있는데, 대신 변수를 나타내기 전 %() 로 묶어 표현해주셔야 합니다.
#print("%d\n%d\n%d\n%d\n%d"%(a+b, a-b, a*b, a/b, a%b))