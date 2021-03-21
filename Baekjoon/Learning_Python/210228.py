# 8393
n = int(input())
result = 0
for i in range(1, n + 1) :
    result += i

print(result)





# 2609 _ 1번째 시도
a, b = map(int, input().split())
gcd = 0
temp_a, temp_b = a, b

if a < b:
    a, b = b, a
while True :
    if a % b == 0 :
        gcd = b
        break
    elif a % b != 0 :
        temp = b
        b = a % b
        a = temp

lcm = int((temp_a * temp_b) / gcd)
print(gcd, lcm, sep='\n')





# 2609 _ 2번째 시도
a, b = map(int, input().split())
temp_a, temp_b = a, b

while b != 0 :
    a = a % b
    a, b = b, a

print(a)
print((temp_a * temp_b) // a)





# 2748
n = int(input())
fib = [0, 1]
for i in range(1, n) :
    fib.append(fib[i] + fib[i - 1])

print(fib[-1])





# 5565
total = int(input())
list = []
for i in range(9) :
    list.append(int(input()))

print(total - sum(list))





# 10950
case = int(input())

for i in range(case) :
    a, b = map(int, input().split())
    print(a + b)





# 10952
while True :
    a, b = map(int, input().split())
    if a == b == 0 :
        break
    print(a + b)





# 10984
t = int(input())

for i in range(t) :
    n = int(input())
    credit = grade = 0

    for j in range(n) :
        c, g = map(float, input().split())
        credit += c
        grade += g * c

    print('{0} {1:0.1f}'.format(int(credit), grade / credit))





# 10833
school = int(input())
left = 0
for i in range(school) :
    student, apple = map(int, input().split())
    left += apple % student

print(left)





# 2442
n = int(input())
for i in range(1, n + 1) :
    print(' ' * (n - i) + '*' * (i * 2 - 1))





# 2443
n = int(input())
for i in range(n, 0, -1) :
    print(' ' * (n - i) + '*' * (i * 2 - 1))





# 2444
n = int(input())
for i in range(1, n + 1) :
    print(' ' * (n - i) + '*' * (i * 2 - 1))
for i in range(n - 1, 0, -1) :
    print(' ' * (n - i) + '*' * (i * 2 - 1))





# 2522
n = int(input())
for i in range(1, (n * 2)) :
    a = abs(n - i)
    print(' ' * a + '*' * (n - a))





# 2523
n = int(input())
for i in range(1, (n * 2)) :
    a = abs(i - n)
    print('*' * (n - a))





# 9325
t = int(input())
for i in range(t) :
    s = int(input())
    for j in range(int(input())) :
        q, p = map(int, input().split())
        s += q * p
    print(s)





# 2445
n = int(input())
for i in range(1, n * 2) :
    a = abs(n - i)
    b = abs((n * 2) - (i * 2))
    print('*' * (n - a) + ' ' * b + '*' * (n - a))





# 2446
n = int(input())

for i in range(1, n) :
    print(' ' * (i - 1) + '*' * (2 * (n - i) + 1))
for i in range(n - 1, -1, -1) :
    print(' ' * (i) + '*' * (2 * (n - i) - 1))




