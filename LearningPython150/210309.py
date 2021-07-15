# 2908 _ 1
n, m = input().split()
n = list(n)
m = list(m)
N = M = 0

for i in range(2, -1, -1) :
    N += (10 ** i) * int(n[i])
    M += (10 ** i) * int(m[i])

print(max(N, M))





# 2908 _ 2
n, m = input().split()
# list[::-1] => 리스트 요소를 거꾸로 뒤집기
n = int(n[: : -1])
m = int(m[: : -1])
print(max(n, m))





# 2460
people = 0
train = []
for i in range(10) :
    off, on = map(int, input().split())
    people -= off
    people += on
    train.append(people)
print(max(train))





# 2577
a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))
for i in range(10) :
    print(result.count(str(i)))





# 2592
num = []
for i in range(10) :
    num.append(int(input()))
many = []
for i in num :
    many.append(num.count(i))
print(sum(num) // 10)
print(num[many.index(max(many))])





# 2711 _ 1
case = int(input())

for i in range(case) :
    n, error = input().split()
    n = int(n)
    error = list(error)
    del error[n - 1]
    print(''.join(error))





# 2711 _ 2
case = int(input())
for i in range(case) :
    n, error = input().split()
    n = int(n)
    print(error[:n-1] + error[n:])





# 1026
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
for i in range(n) :
    s += min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))

print(s)





