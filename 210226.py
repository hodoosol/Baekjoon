# 1408
# 1 = now, 2 = start, r = result
h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

now = (h1 * 3600) + (m1 * 60) + s1
start = (h2 * 3600) + (m2 * 60) + s2

if start - now > 0 :
    result = start - now
elif start - now <= 0 :
    result = 86400 + (start - now)

rh = result // 3600
result %= 3600
rm = result // 60
rs = result % 60

print('{:02d}:{:02d}:{:02d}'.format(rh, rm, rs))





# 2741
n = int(input())
for i in range(1, n + 1) :
    print(i)





# 2742
n = int(input())
for i in range(n, 0, -1) :
    print(i)





# 2739
n = int(input())
for i in range(1, 10) :
    print('{0} * {1} = {2}'.format(n, i, n * i))





# 2438 _ 굳이 star 안써도 되는구나
n = int(input())
star = '*'
for i in range(1, n + 1) :
    print(star * i)





# 2439
n = int(input())
for i in range(1, n + 1) :
    print(' ' * (n - i) + '*' * (i))





# 2440
n = int(input())
for i in range(n, 0, -1) :
    print('*' * i)





# 2441
n = int(input())
for i in range(n, 0 , -1) :
    print(' ' * (n - i) + '*' * i)



