# 2501
n, k = map(int, input().split())
factor = []
for i in range(1, n + 1) :
    if n % i == 0 :
        factor.append(i)

if len(factor) < k :
    print(0)
else :
    print(factor[k - 1])





# 2562
num = []
for i in range (9) :
    num.append(int(input()))

print(max(num))
print(num.index(max(num)) + 1)





# 2475 _ 람다로 풀기
verif = list(map(int, input().split()))
verif = list(map(lambda x : x ** 2, verif))
print(sum(verif) % 10)





# 2475 _ for문으로 풀기
verif = list(map(int, input().split()))
sum = 0
for i in verif :
    sum += i ** 2
print(sum % 10)





# 2747
n = int(input())
fib = [0, 1]
for i in range(n - 1) :
    fib.append(fib[i] + fib[i + 1])

print(fib[n])





# 2576
num = []
for i in range(7) :
    n = int(input())
    if n % 2 == 1:
        num.append(n)

if not num :
    print(-1)
else :
    print(sum(num))
    print(min(num))




