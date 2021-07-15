# 2798 _ itertools 이용, 시간 초과
from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))
# temp에 모든 조합을 저장하고 sums에 조합의 합을 저장
temp = list(combinations(cards, 3))
sums = []
for i in temp :
    sums.append(sum(i))
# while문을 통해 m과 가장 가까운 결과값 찾기
j = 0
while True :
    if m - j in sums :
        print(m - j)
        break
    else :
        j += 1





# 2798 _ 직접 모든 경우의 수 다 찾기
n, m = map(int, input().split())
cards = list(map(int, input().split()))
res = 0
for i in range(n) :
    for j in range(i + 1, n) :
        for k in range(j + 1, n) :
            if cards[i] + cards[j] + cards[k] > m :
                continue
            else :
                res = max(res, cards[i] + cards[j] + cards[k])

print(res)





# 2231 _ 시간 초과
n = int(input())
m = 0

while True :
    res = m
    nums = list(str(m))
    for i in nums :
        res += int(i)
    if res == n :
        if res == m :
            print(0)
            break
        else :
            print(m)
            break
    else :
        m += 1





# 2231
n = int(input())

for i in range(1, n + 1) :
    nums = list(map(int, str(i)))
    sums = i + sum(nums)
    if sums == n :
        print(i)
        break
    if i == n :
        print(0)




