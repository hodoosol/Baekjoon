# 10818
n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))





# 5054 _ 1
case = int(input())
for i in range(case) :
    n = int(input())
    store = sorted(list(map(int, input().split())))
    result = 0
    for j in range(-1, len(store) - 1) :
        result += abs(store[j] - store[j + 1])
    print(result)





# 5054 _ 2
for i in range(int(input())) :
    input()
    store = list(map(int, input().split()))
    print((max(store) - min(store)) * 2)





# 2822
score = []
index = []

for i in range(8) :
    score.append(int(input()))
temp = sorted(score[:], reverse=True)
for j in range(5) :
    index.append(score.index(temp[j]) + 1)

print(sum(temp[:5]))
print(*(sorted(index)))





# 2750
n = int(input())
nums = []
for i in range(n) :
    nums.append(int(input()))
nums.sort()
for j in range(n) :
    print(nums[j])





# 2752
nums = sorted(list(map(int, input().split())))
for i in nums :
    print(i, end=' ')





# 1037
n = int(input())
factor = list(map(int, input().split()))
print(max(factor) * min(factor))





# 5543 _ 1
burger = []
soda = []

for i in range(3) :
    burger.append(int(input()))
for j in range(2) :
    soda.append(int(input()))

print(min(burger) + min(soda) - 50)





# 5543 _ 2
cheap1 = cheap2 = 2001

for i in range(3) :
    burger = int(input())
    cheap1 = min(burger, cheap1)
for j in range(2) :
    soda = int(input())
    cheap2 = min(soda, cheap2)

print(cheap1 + cheap2 - 50)





# 2587
nums = []
for i in range(5) :
    nums.append(int(input()))
nums.sort()
print(sum(nums) // 5)
print(nums[2])





# 1427
n = sorted(input(), reverse=True)
print(''.join(n))





# 2309
# 키 입력받고, 오름차순 정렬 후 temp에 복사, 모든 요소 더해놓기
height = []
for i in range(9) :
    height.append(int(input()))
height.sort()
temp = height[:]
result = sum(height)
# result - (height의 요소 + 그 요소를 뺀 temp의 요소) == 100이 되면 두 요소 제거
# 제거되는 즉시 멈출 수 있도록 if문 걸어주기
for i in height :
    temp.remove(i)
    for j in range(len(temp) - 1) :
        if result - (i + temp[j]) == 100 :
            height.remove(i)
            height.remove(temp[j])
    if len(height) == 7 :
        break
    temp.append(i)
# 출력
for k in height :
    print(k)





# 9076
case = int(input())
for i in range(case) :
    score = sorted(list((map(int, input().split()))))
    if score[3] - score[1] >= 4 :
        print('KIN')
    else :
        print(sum(score[1:4]))





# 2693
case = int(input())
for i in range(case) :
    nums = sorted(list(map(int, input().split())))
    print(nums[7])





# 5176
t = int(input())
for i in range(t) :
    p, m = map(int, input().split())
    avail = []
    cnt = 0
    for j in range(p) :
        want = int(input())
        if want not in avail :
            avail.append(want)
        else :
            cnt += 1
    print(cnt)





# 10773
k = int(input())
money = []
for i in range(k) :
    m = int(input())
    if m == 0 :
        money.pop()
    else :
        money.append(m)
print(sum(money))





# 3040 _ 거의 비슷한 문제 ...
height = []
for i in range(9) :
    height.append(int(input()))
temp = height[:]
result = sum(height)

for i in height :
    temp.remove(i)
    for j in range(len(temp) - 1) :
        if result - (i + temp[j]) == 100 :
            height.remove(i)
            height.remove(temp[j])
    if len(height) == 7 :
        break
    temp.append(i)

for k in height :
    print(k)






