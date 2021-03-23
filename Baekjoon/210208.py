# 2557
print('Hello World!')



# 1000
a, b = map(int, input().split())
print(a + b)



# 10998
a, b = map(int, input().split())
print(a * b)



# 1001
a, b = map(int, input().split())
print(a - b)



# 1008
a, b = map(int, input().split())
print(a / b)



# 10869
a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(int(a / b))
print(a % b)



# 10430
a, b, c = map(int, input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)



# 2558
a = int(input())
b = int(input())
print(a + b)



# 2588
a, b, c = map(int, input())
d, e, f = map(int, input())

A = ((100 * a) + (10 * b) + c)
B = ((100 * d) + (10 * e) + f)

print(A * f)
print(A * e)
print(A * d)
print(A * B)



# 2588 _ 다슬이 꺼
a = int(input())
b = list(map(int, input()))
ab = [0, 0, 0]

for i in range(2, -1, -1) :
    ab[i] = a * int(b[i])
    print(ab[i])

print(ab[2] + ab[1]*10 + ab[0]*100)



# 3046
R1, S = map(int, input().split())
print((S * 2) - R1)





