# 10448 _ 공식없이 무대뽀로 !!!
from itertools import combinations_with_replacement

trinums = [1]
i = 2
while True :
    if trinums[-1] + i < 1001 :
        trinums.append(trinums[-1] + i)
        i += 1
    else :
        break

temp = list(combinations_with_replacement(trinums, 3))
sums = []

for i in temp :
    if sum(i) < 1001 :
        sums.append(sum(i))

for j in range(int(input())) :
    n = int(input())
    if n in sums :
        print(1)
    else :
        print(0)





# 10448 _ 공식을 이용해서 길이를 줄여보자 ...
tri = [i * (i + 1) // 2 for i in range(1, 46)]
sums = []

for i in tri :
    for j in tri :
        for k in tri :
            sums.append(i + j + k)

for x in range(int(input())) :
    n = int(input())
    if n in sums :
        print(1)
    else :
        print(0)





# 10448 _ 다른 사람 풀이가 신기해서 정리
# 미리 삼각수를 구하는 것은 동일
triangle = [n * (n + 1) // 2 for n in range(1, 46)]
# 삼각수의 합을 구하기 위해 0으로 초기화
eureka = [0] * 1001
# 세 개의 삼각수를 더해서
for i in triangle :
    for j in triangle :
        for k in triangle :
            # 그것이 1000 이하이면 유레카 리스트의 해당 인덱스를 1로 변경한다.
            # ex) eureka[1 + 3 + 3] = 1, eureka[7] = 1이 되는 것이다.
            if i + j + k <= 1000 :
                eureka[i + j + k] = 1
# 테스트케이스와 정수 n입력 받고
T = int(input())
for _ in range(T) :
    # 찾고자 하는 수가 10이라면 eureka[10]을 호출.
    # -> 세 개의 삼각수의 합이라면 1, 아니라면 0 이 출력된다.
    print(eureka[int(input())])





# 2161
n = int(input())
card = [i for i in range(1, n + 1)]

while len(card) > 1 :
        print(card[0], end=' ')
        card.pop(0)
        card.append(card[0])
        card.pop(0)

print(card[0])





# 2161 _ deque로 풀기.
from collections import deque
n = int(input())
card = deque([i for i in range(1, n + 1)])

while len(card) > 1 :
    print(card[0], end=' ')
    card.popleft()
    card.append(card[0])
    card.popleft()

print(card[0])





# 1592
n, m, l = map(int, input().split())
ball = [0] * n

i = 0
cnt = 0

while True :
    ball[i] += 1
    if ball[i] == m :
        print(cnt)
        break
    i = (i + l) % n
    cnt += 1




    
