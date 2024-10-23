N = int(input())

NumList = list(map(int, input().split()))

v = int(input())

x = 0

for i in range(N) : 
    if(NumList[i] == v ) :
        x += 1
print(x)