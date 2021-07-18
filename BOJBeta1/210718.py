# 6603 로또, 실버 2
from itertools import combinations
while True :
    nums = list(map(int, input().split()))
    if nums[0] == 0 :
        break
    n = nums.pop(0)

    lotto = list(combinations(nums, 6))
    for i in lotto :
        for j in i :
            print(j, end=' ')
        print()
    print()





# 1182 부분수열의 합, 실버 2
from itertools import combinations
n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

for i in range(1, n + 1) :
    part = list(combinations(nums, i))
    for j in part :
        if sum(j) == s :
            answer += 1

print(answer)




