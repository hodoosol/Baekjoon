# 1712
a, b, c = map(int, input().split())

while True :
    if b >= c :
        print(-1)
        break
    else :
        print(a // (c - b) + 1)
        break





# 2292
n = int(input())
chk = 1
i = 1
while True :
    if chk >= n :
        print(i)
        break
    else :
        chk += 6 * i
        i += 1





# 1193
n = int(input())
d = 1
temp = 1
while True :
    temp += d
    d += 1
    if n < temp :
        break

for i in range(n - (temp - d + 1) + 1) :
        x = d - 1 - i
        y = 1 + i

if d % 2 == 0 :
    print("{0}/{1}".format(x, y))
else :
    print("{0}/{1}".format(y, x))





# 2869 _ 시간 초과
a, b, v = map(int, input().split())
temp = 0
res = 1
while True :
    temp += a
    if temp >= v :
       print(res)
       break
    temp -= b
    res += 1





# 2869
import math
a, b, v = map(int, input().split())
res = (v - b) / (a - b)
print(math.ceil(res))





# 10250
for i in range(int(input())) :
    h, w, n = map(int, input().split())
    if n % h == 0 :
        x = n // h
    else :
        x = n // h + 1
    y = n - (x - 1) * h
    print(100 * y + x)





# 2775
for i in range(int(input())) :
    k = int(input())
    n = int(input())
    apt = [j for j in range(1, n + 1)]
    for x in range(k) :
        for y in range(n - 1) :
            apt[y + 1] = apt[y] + apt[y + 1]
    print(apt[n - 1])





