# 2차원 행렬
# 표의 행과 열의 구분

# 행렬의 크기 N(행의 크기), M(열의 크기)을 입력받기 위해
# input함수를 통해 입력받고 공백을 기준으로 자른다.
# map함수를 통해 각 값을 int()를 사용하여 정수화시킨다.
N, M = map(int, input().split())

# A 행렬과 B 행렬에 빈 배열[]을 할당함으로써
# 초기화 선언
A, B = [], []

# 행렬 A 구성
# 각 행렬은 N개의 줄이 있기에 N번 반복 시행
for i in range(N):
    # 해당 행을 입력 받기 위해 input()을 통해 입력받고
    # 각 값들을 정수화시킨뒤 row라는 변수에 담아준다.
    row = list(map(int, input().split()))
    # 해당 row 값을 A 리스트에 추가한다.
    A.append(row)

# B 행렬의 구성
for i in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 A의 특정 행과 특정 열에 해당하는 값과 
# 행렬 B의 특정 행과 특정 열에 해당하는 값을 더해주기 위한 반복문
# 중첩 반복문 사용
for row in range(N):
    for col in range(M):
        # 2차원 행렬이기에 특정 값을 더해주기 위해서는
        # 해당 list 변수명[행][열]을 사용하여 더해주고
        # 그렇게 더해준 값을 구분짓기 위해 공백도 함께 출력해준다.
        print(A[row][col] + B[row][col], end=' ')
    # 각 줄마다 값을 구분하기 위해 
    # 행이 끝날 때마다 print()함수를 통해 
    # 줄로써 구분지어준다.
    print()

