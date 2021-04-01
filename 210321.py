# 10808 _ 1
alpha = []
for i in range(ord('a'), ord('z') + 1) :
    alpha.append(chr(i))

word = input()
for j in range(len(alpha)) :
    if alpha[j] in word :
        alpha[j] = word.count(alpha[j])
    else :
        alpha[j] = 0

print(*alpha)





# 10808 _ 2
alpha = [0] * 26
word = input()
for i in word :
    alpha[ord(i) - 97]  = word.count(i)
print(*alpha)





# 1157 _ 1
word = input().upper()
alpha = [0] * 26
for i in word :
    alpha[ord(i) - 65] += 1
if alpha.count(max(alpha)) > 1 :
    print('?')
else :
    res = alpha.index(max(alpha))
    print(chr(res + 65))





# 1157 _ 2
word = input().upper()
temp = sorted(list(set(word)))
res = []
for i in temp :
    cnt = word.count(i)
    res.append(cnt)
if res.count(max(res)) > 1 :
    print('?')
else :
    print(temp[res.index(max(res))])





# 5218
for i in range(int(input())) :
    res = []
    a, b = input().split()
    for j in range(len(a)) :
        if ord(a[j]) > ord(b[j]) :
            res.append(ord(b[j]) - ord(a[j]) + 26)
        else :
            res.append(ord(b[j]) - ord(a[j]))
    print('Distances:', *res)





# 9086
for i in range(int(input())) :
    word = input()
    print(word[0] + word[-1])





# 11365
while True :
    sent = str(input())
    if sent == 'END' :
        break
    print(sent[::-1])





# 11170
for i in range(int(input())) :
    res = []
    n, m = map(str, input().split())
    for j in range(int(n), int(m) + 1) :
        res += list(str(j))
    print(res.count('0'))





# 11655 _ 1
code = list(input())
for i in range(len(code)) :
    if code[i].isupper() :
        if ord(code[i]) + 13 > 90 :
            code[i] = chr(ord(code[i]) - 13)
        else :
            code[i] = chr(ord(code[i]) + 13)
    elif code[i].islower() :
        if ord(code[i]) + 13 > 122 :
            code[i] = chr(ord(code[i]) - 13)
        else :
            code[i] = chr(ord(code[i]) + 13)
print(''.join(code))





# 11655 _ 2
code = list(input())
for i in range(len(code)) :
    t = ord(code[i])
    if t >= 65 and t <= 90 :
        t += 13
        if t > 90 :
            t -= 26
    elif t >= 97 and t <= 122 :
        t += 13
        if t > 122 :
            t -= 26
    print(chr(t), end='')





# 1676 _ 1
fact = 1
for i in range(1, int(input()) + 1) :
    fact *= i
fact = str(fact)

res = 0
for j in range(len(fact) -1, -1, -1) :
    if fact[j] == '0' :
        res += 1
    else :
        print(res)
        break





# 1676 _ 2
fact = 1
for i in range(1, int(input()) + 1) :
    fact *= i
cnt = 0
while fact % 10 == 0 :
    fact //= 10
    cnt += 1
print(cnt)




