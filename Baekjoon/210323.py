# 10172
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\__|')





# 1330
a, b = map(int, input().split())
if a > b :
    print('>')
elif a < b :
    print('<')
else :
    print('==')





# 14681
x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print(1)
elif x < 0 and y > 0 :
    print(2)
elif x < 0 and y < 0 :
    print(3)
else :
    print(4)





# 15552
import sys
for i in range(int(input())) :
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)





# 10952
while True :
    a, b = map(int, input().split())
    if a == b == 0 :
        break
    print(a + b)





# 10951
while True :
    try :
        a, b = map(int, input().split())
        print(a + b)
    except :
        break





# 1110
org_n = int(input())
n, cnt = org_n, 0

while True :
    if n < 10 :
        n = '0' + str(n)
    n = list(str(n))
    temp = list(str(int(n[0]) + int(n[-1])))
    n = int(n[-1] + temp[-1])
    cnt += 1
    if org_n == n :
        print(cnt)
        break





# 4344
for i in range(int(input())) :
    grade = list(map(int, input().split()))
    avg = sum(grade[1:]) / grade[0]
    grade.pop(0)
    cnt = 0
    for j in grade :
        if j > avg :
            cnt += 1
    print('{:.3f}%'.format(cnt / len(grade) * 100))





