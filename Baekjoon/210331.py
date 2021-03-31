# 2839
sugar = int(input())
res = 0
i = 0
while True :
    temp = sugar - (i * 3)
    if temp % 5 == 0 :
        res += temp // 5
        break
    if temp < 0 :
        res = -1
        break
    i += 1
    res += 1
print(res)





# 3009
xs = []
ys = []
for i in range(3) :
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

if xs[0] == xs[1] :
    print(xs[2], end=' ')
else :
    print(xs[0], end=' ')

if ys[0] == ys[1] :
    print(ys[2], end=' ')
else :
    print(ys[0], end=' ')





# 4153 _ 1
while True :
    tri = sorted(list(map(int, input().split())))
    if tri[0] == tri[1] == tri[2] == 0 :
        break
    if (tri[0] ** 2) + (tri[1] ** 2) == tri[2] ** 2 :
        print('right')
    else :
        print('wrong')





# 4153 _ 2
while True :
    a, b, c = sorted(list(map(int, input().split())))
    if a == b == c == 0 :
        break
    print('right' if a * a + b * b == c * c else 'wrong')





# 3053
import math
r = int(input())
print(round(r * r * math.pi, 6))

taxi = abs(-r) + abs(-r)
print(round(taxi * taxi * 0.5, 6))





# 1085
x, y, w, h = map(int, input().split())

print(min(w - x, h - y, x, y))




