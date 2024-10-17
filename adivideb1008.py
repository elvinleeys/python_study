# 서식 지정자 사용
# 실수 표현시 %f 사용
# 소수점 이하 자릿수를 지정한다면?
# '%.자릿수f' % 숫자
# A, B = map(int, input().split())
# print('%0.9f'%(A/B))

# round()함수 사용
# python 기본 내장 함수로 round() 함수는 주어진 숫자를 지정한 소수점 자릿수에 맞춰 반올림하는 역할을 한다.
# 이 함수는 실수, 정수, 복소수 등 모든 숫자에 적용가능
# 기본형: round(number, ndigits)
# number: 반올림할 숫자
# ndigits: 소수점 이하 자릿수(몇자리까지 표현하고 반올림할 것인지)
# A, B = map(int, input().split())
# print(round(A/B, 9))

# 상대오차가 10⁻⁹ 이내여야 한다는 단서가 있지만, 
# Python3는 나누기 연산 시 기본적으로 소수점 16번째자리까지 표현하는 실수를 리턴하므로 
# 그대로 출력합니다.
A, B = map(int, input().split())
print(A/B)