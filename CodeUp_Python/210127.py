# 1088
a = int(input())

for i in range(1, a+1) :
    if i % 3 == 0 :
        pass
    else :
        print(i, end=' ')





# 1089
a, d, n = map(int, input().split())

for i in range(n-1) :
    a += d

print(a)





# 1090
a, r, n = map(int, input().split())

for i in range(n-1) :
    a = a * r

print(a)





# 1091
a, m, d, n = map(int, input().split())
for i in range(n-1) :
    a = (a*m) + d

print(a)





# 1092
x, y, z = map(int, input().split())
day = 1

while (day%x != 0 or day%y != 0 or day%z != 0) :
    day += 1

print(day)





# 1093
n = int(input())
check = map(int, input().split())
student = [0 for i in range(23)]

for i in check :
        student[int(i-1)] += 1

for i in range(23) :
    print(student[i], end=' ')
