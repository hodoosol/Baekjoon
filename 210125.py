# 1078
n = int(input())
result = 0

for i in range(1, n+1) :
    if i % 2 == 0 :
        result += i

print(result)




# 1079
str = input().split()
for i in str :
    print(i)
    if i == 'q' :
        break




# 1080
num = int(input())
m = 1
for i in range(0, 1001) :
    m += i
    if m > num :
        print(i)
        break




# 1081
x, y = map(int, input().split())
for i in range(1, x+1) :
    for j in range(1, y+1) :
        print(i, j)




# 1082
z = int(input(), 16)

for i in range(1, 16) :
    print('%X*%X=%X' %(z, i, z*i))