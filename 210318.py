# 11047
n, k = map(int, input().split())
coin = []
for i in range(n) :
    coin.append(int(input()))

cnt = 0
for j in range(n) :
    cnt += k // coin[-1 - j]
    k %= coin[-1 - j]

print(cnt)





# 2743
print(len(input()))





# 2744 _ 1
word = input()
result = ''
for i in word :
    if ord(i) >= 65 and ord(i) <= 90 :
        result += chr(ord(i) + 32)
    elif ord(i) >= 97 and ord(i) <= 122 :
        result += chr(ord(i) - 32)
print(result)





# 2744 _ 2
word = input()
result = ''
for i in word :
    if i.isupper() :
        result += i.lower()
    elif i.islower() :
        result += i.upper()
print(result)





# 2744 _ 3
print(input().swapcase())





# # 10953
for i in range(int(input())) :
    a, b = map(int, input().split(','))
    print(a + b)





# 2902
names = list(input().split('-'))
for i in names :
    print(i[0], end='')




