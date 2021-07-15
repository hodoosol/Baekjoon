# 5086
while True :
    a, b = map(int, input().split())
    if a == b == 0 :
        break
    elif b % a == 0 :
        print('factor')
    elif a % b == 0 :
        print('multiple')
    else :
        print('neither')





# 5717
while True :
    a, b = map(int, input().split())
    if a == b == 0 :
        break
    print(a + b)





# 9610
n = int(input())
Q1 = Q2 = Q3 = Q4 = AXIS = 0

for i in range(n) :
    x, y = map(int, input().split())
    if x > 0 and y > 0 :
        Q1 += 1
    elif x < 0 and y > 0 :
        Q2 += 1
    elif x < 0 and y < 0 :
        Q3 += 1
    elif x > 0 and y < 0 :
        Q4 += 1
    elif x == 0 or y == 0 :
        AXIS += 1

print('Q1: {0}\nQ2: {1}\nQ3: {2}\nQ4: {3}\nAXIS: {4}\n'.format(Q1, Q2, Q3, Q4, AXIS))





# 8958
case = int(input())

for i in range(case) :
    score = list(input())
    result = 0
    k = 1
    for j in score :
        if j == 'O' :
            result += k
            k += 1
        else :
            k = 1
    print(result)





# 9506
while True :
    n = int(input())
    if n == -1 :
        break
    factor = []

    for j in range(1, n) :
        if n % j == 0 :
            factor.append(j)

    if sum(factor) == n :
        print(n, '=', end=' ')
        for l in factor[:-1] :
            print(l, end=' + ')
        print(factor[-1], end='\n')
    else :
        print(n, 'is NOT perfect.')



