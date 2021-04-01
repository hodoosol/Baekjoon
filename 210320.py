# 1357
x, y = map(int, input().split())
def Rev(n) :
    n = int(str(n)[::-1])
    return n
print(Rev(Rev(x) + Rev(y)))





# 10987 _ 1
word = input()
vowel = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for i in word :
    if i in vowel :
        cnt += 1
print(cnt)





# 10987 _ 2
word = input()
vowel = 'aeiou'
cnt = 0
for i in vowel :
    cnt += word.count(i)
print(cnt)





# 4458
for i in range(int(input())) :
    sent = input()
    sent = sent[0].upper() + sent[1:]
    print(sent)





# 11654
print(ord(input()))





# 11720 _ 1
input()
num = input()
res = 0
for i in num :
    res += int(i)
print(res)





# 11720 _ 2
input()
num = list(input())
print(sum(map(int, num)))





# 11721 _ 1
word = input()
res = ''
cnt = 0
for i in range(len(word) // 10 + 1) :
    if i == len(word) // 10 :
        print(word[i * 10 :])
    else :
        print(word[i * 10 : (i + 1) * 10])





# 11721 _ 2  :  슬라이싱은 인덱스랑 다르게 범위가 초과해도 끝까지 출력됨.
word = input()
res = ''
cnt = 0
for i in range(len(word) // 10 + 1) :
    print(word[i * 10 : (i + 1) * 10])





# 10821
nums = list(map(int, input().split(',')))
print(len(nums))




