# list comprehension을 이용하여 1부터 30까지의 출석번호를
# list 자료형에 담는다.
# 기본형: [표현식 for 항목 in 반복_가능_객체 if 조건문]
students = [i for i in range(1,31)]

# 과제를 제출한 출석번호를 28번 반복하여 입력받기 위해
# for문(반복문 사용)
for _ in range(28):
    # input()함수를 통해 입력 받은 후 int()함수를 통해 정수화
    applied = int(input())
    # 해당 applied번호, 즉 과제를 제출한 출석번호는
    # students list자료형에서 제거한다.
    students.remove(applied) #소거

# 위 반복문에 따라 과제를 제출한 사람은 모두 소거했고
# list 자료형에 남아있는 숫자는 과제를 제출하지 않은 학생이다.
# 오름차순으로 출력하라고 했으므로 
# 최소값부터 출력
print(min(students))
print(max(students))

