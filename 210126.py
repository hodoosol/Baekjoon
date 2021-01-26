# 1083
x = int(input())

for i in range (1, x+1) :
    if i % 3 == 0 :
        print('X', end=' ')
    else :
        print(i, end=' ')





# 1084
r, g, b = map(int, input().split())
cnt = 0

for i in range (0, r) :
    for j in range (0, g) :
        for k in range (0, b) :
            print(i, j , k)
            cnt += 1
print(cnt)





# 1085
h, b, c, s = map(int, input().split())
print('%.1f MB' %((h*b*s*c)/(2**23)))





# 1086
w, h, b = map(int, input().split())
print('%.2f MB' %((w*h*b)/(2**23)))





# 1087
n = int(input())
result = 0
for i in range(1, n+1) :
    result += i
    if result >= n :
        print(result)
        break