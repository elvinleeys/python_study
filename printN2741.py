N = int(input())
number = range(1, N+1)
for i in number:
    print(i)
# comprehension 표현식
# 기본형: [ (출력 표현식) for (iterable자료 요소) in (iterable자료형)]
# [print(i) for i in range(1, int(input())+1)]