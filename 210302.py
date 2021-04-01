# 2010
import sys
n = int(sys.stdin.readline())
multi = 1

for i in range(n) :
    multi = multi + int(sys.stdin.readline()) - 1
print(multi)





# 5522
score = 0
for i in range(5) :
    score += int(input())
print(score)





# 10178
case = int(input())

for i in range(case) :
    candy, kid = map(int, input().split())
    print('You get {0} piece(s) and your dad gets {1} piece(s).'
          .format(candy // kid, candy % kid))





# 9295
case = int(input())

for i in range(1, case + 1) :
    a, b = map(int, input().split())
    print("Case {0}: {1}".format(i, a + b))





# 10569
t = int(input())
for i in range(t) :
    face = 0
    v, e = map(int, input().split())
    face = (2 - v + e)
    print(face)





# 2921
n = int(input())
total = 0
for i in range(n + 1) :
    total += i * (n + 2)
print(total)





# 10995
n = int(input())
for i in range(1, n + 1) :
    if i % 2 != 0 :
            print('* ' * n)
    else :
            print(' *' * n)




