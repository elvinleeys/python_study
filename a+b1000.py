# 여러 변수 동시에 선언
# in Java
# Java에서는 콤마( , )를 이용해 여러 개의 변수를 동시에 선언
# ex) int a = 1, b = 2, c = 3;
# in python
# a, b, c = 1, 2, 3
# input() 함수
# 사용자로부터 문자열을 입력받을 때 사용
# split() 함수
# 입력받는 문자를 나눌 때 사용하는 함수
# 괄호 안에 아무것도 넣지 않으면 공백(띄어쓰기, 탭 등)을 기준으로 문자열을 나눈다.
# int() 함수
# 문자형을 숫자형으로 변형할 수 있다. 이때 int는 숫자 중에서도 정수를 의미
# 단, int 함수는 리스트를 정수형으로 바꾸어줄 수 없다.
# 즉, int(input().split())은 불가
# 1단계 풀이
# A, B = input().split()
# print(int(A) + int(B))
# 다른 풀이
# map함수
# 기본형: map(function, iterable)
# function: 각 요소에 적용할 함수입니다.
# iterable: 함수를 적용할 데이터 집합입니다.
A, B = map(int, input().split())
print(A + B)