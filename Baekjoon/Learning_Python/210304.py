# 10991
n = int(input())
for i in range(1, n + 1) :
    print(' ' * (n - i), end='')
    print('* ' * i)





# 10871
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a :
    if i < x :
        print(i, end=' ')





# 10872
n = int(input())
result = 1
for i in range(1, n + 1) :
    result *= i

print(result)





# 1978
import copy
n = int(input())
prime = list(map(int, input().split()))
temp = copy.deepcopy(prime)

for i in temp :
    if i == 1 :
        prime.remove(i)
        pass
    else :
        for j in range(2, i) :
            if i % j == 0 :
                prime.remove(i)
                break

print(len(prime))





# 2581
m = int(input())
n = int(input())
result = []

for i in range(m, n + 1) :
    if i == 1 :
        pass
    elif i == 2:
        result.append(i)
    else :
        for j in range(2, i) :
            if i % j == 0 :
                break
            if j == i - 1 :
                result.append(i)

if len(result) == 0 :
    print(-1)
else :
    print(sum(result))
    print(min(result))




