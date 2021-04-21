# 2751
import sys
nums = []
for i in range(int(input())) :
    nums.append(int(sys.stdin.readline()))

for j in sorted(nums) :
    print(j)





# 2751 _ 선택 정렬 try _ but, 시간 초과
import sys
nums = []
for i in range(int(input())) :
    nums.append(int(sys.stdin.readline()))

for j in range(len(nums)) :
    temp = j
    for k in range(j + 1, len(nums)) :
        if nums[temp] > nums[k] :
            temp = k
    nums[j], nums[temp] = nums[temp], nums[j]

for x in nums :
    print(x)





# 10989 _ 계수 정렬 _ 메모리 초과
import sys
n = []
for i in range(int(input())) :
    n.append(int(sys.stdin.readline()))
# 이 부분이 잘못됨. 숫자의 크기는 10000 이하이므로 n개의 0 리스트를 만들 필요가 없음.
res = [0] * (max(n) + 1)

for j in range(len(n)) :
    res[n[j]] += 1

for x in range(min(n), max(n) + 1) :
    for y in range(res[x]) :
        print(x)





# 10989 _ 계수 정렬 재도전 _ 성공
# 수의 개수 n은 1 <= n <= 10,000,000의 범위를 갖지만
# 각각의 수는 10,000보다 작거나 같으므로
# 수의 개수를 카운트할 리스트 res를 10,001개로 초기화하면 된다.
import sys
input = sys.stdin.readline
n = int(input())
res = [0] * 10001

for i in range(n) :
    res[int(input())]  += 1

for j in range(1, 10001) :
    for k in range(res[j]) :
        print(j)





# 2108
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n) :
    nums.append(int(input()))
# 미리 정렬하기.
nums.sort()
# 산술 평균과 중앙값 구하기.
print(round(sum(nums) / n))
print(nums[(n // 2)])
# 최빈값 구하기.
cnt = Counter(nums)
com = cnt.most_common()
if len(com) > 1 :
    if com[1][1] == com[0][1] :
        print(com[1][0])
    else :
        print(com[0][0])
else :
    print(com[0][0])
# 범위 구하기.
print(nums[-1] - nums[0])




