# 1094
n = int(input())
student = list(map(int, input().split()))

for i in range(n-1, -1, -1) :
    print(student[i], end=' ')





# 1095
n = int(input())
student = list(map(int, input().split()))

print(min(student))





# 1096
baduk = [[0]*19 for i in range (19)]

n = int(input())
for j in range(n) :
    x, y = map(int, input().split())
    baduk[x-1][y-1] = 1

for i in range(19) :
    for j in range(19) :
        print(baduk[i][j], end=' ')
    print()





# 1097 _ 내 풀이
baduk = [0]*19
for i in range(19) :
    baduk[i] = list(map(int, input().split()))

n = int(input())

for i in range(n) :
    x, y = map(int, input().split())
    for j in range(19) :
        baduk[x-1][j] = not baduk[x-1][j]
        for k in range(19) :
            baduk[k][y-1] = not baduk[k][y-1]

for i in range(19) :
    for j in range(19) :
        print(int(baduk[i][j]), end=' ')
    print()





# 1097 - 고치다가 체온 2도 상승한 다슬이 풀이
m = [0]*19
for i in range(19):
    m[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
    x , y = map(int, input().split())
    for i in range(19):
        if m[x-1][i] == 0 :
            m[x-1][i] = 1
        else :
            m[x-1][i] = 0

        for j in range(19):
            if m[j][y-1] == 0 :
                m[j][y-1] = 1
            else:
                m[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(m[i][j], end=' ')
    print()
