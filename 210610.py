# 1259 팰린드롬수, 브론즈 1
## str, list에 [::-1] 하면 데이터가 뒤집힌다.
## [::-1] == 처음부터 끝까지 역순으로 한칸씩

while True :
    w = input()
    if w == '0' :
        break

    if w == w[::-1] :
        print('yes')
    else :
        print('no')





# 1264 모음의 개수, 브론즈 2
target = ['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']
while True :
    s = input()
    if s == '#' :
        break
    answer = 0
    for i in s :
        if i in target :
            answer += 1
    print(answer)





# 1371 가장 많은 글자, 브론즈 2
## sys의 sys.stdin.read()를 사용하려고 해봤지만 왜인지 파이참에서는 되지가 않는다 ...
import sys
s, word = sys.stdin.read(), [0 for i in range(26)]
for i in s :
    if i.islower() :
        word[ord(i) - 97] += 1
for j in range(26) :
    if word[j] == max(word) :
        print(chr(j + 97), end='')




