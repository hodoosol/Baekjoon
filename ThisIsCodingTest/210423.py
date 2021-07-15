"""

2021.04.23
백준 _ 단계별로 풀어보기 _ 이분 탐색

"""



## 1920 수 찾기
# 1920 _ 이분 탐색
n = int(input())
# 이분 탐색을 하기 위해서는 찾으려는 리스트를 반드시 오름차순으로 정렬해야 한다 !!!
a = sorted(list(map(int, input().split())))
m = int(input())
t = list(map(int, input().split()))

for i in t :
    start = 0
    end = n - 1
    while True :
        if start > end :
            print(0)
            break
        mid = (start + end) // 2
        if a[mid] == i :
            print(1)
            break
        elif a[mid] > i :
            end = mid - 1
        else :
            start = mid + 1





# 1920 _ 당연하게도 시간 초과
n = int(input())
a = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

for i in t :
    if i in a :
        print(1)
    else :
        print(0)





# 1920 _ 찾는 대상이 되는 a를 중복을 허용하지 않는 unique한 set으로 만든 뒤 찾기.
# why ? 문제에서 각각의 t가 a에 있는지의 여부만 물었기때문에 가능.
n = int(input())
# int로 입력받을 필요도 없다.
a = set(input().split())
m = int(input())
# a를 str로 입력 받았으니 t도 str로 입력 받기.
t = input().split()

for i in range(m):
    if t[i] in a :
        print(1)
    else :
        print(0)





## 10816 숫자카드 2
# 이분 탐색 _ 5번 시도 ... 시간초과 _ 이 방법은 성공
# 이분 탐색과 딕셔너리를 함께 이용하지 않으면 무조건 시간 초과인듯 하다.
import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
t = list(map(int, input().split()))

def bisearch(array, target) :
    start = 0
    end = n - 1
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return array[start : end + 1].count(target)
            break
        elif array[mid] > target :
            end =  mid - 1
        else :
            start = mid + 1
    return 0

res = {}

for i in t :
    if i not in res :
        res[i] = bisearch(card, i)

print(' '.join(str(res[x]) for x in t))






# 10816 _ 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
card = input().split()
m = int(input())
t = input().split()

res = []

for i in range(m) :
    res.append(card.count(t[i]))

print(*res)





# 10816 _ collections 모듈의 Counter 클래스 사용 _ 성공
# Counter는 배열의 각 요소가 몇 개나 있는지 세어준다.
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

x = Counter(card)

for i in t :
    print(x[i], end=' ')





# 10816 _ bisect 사용하기.
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
t = list(map(int, input().split()))

for i in range(m) :
    r = bisect_right(card, t[i])
    l = bisect_left(card, t[i])
    print(r - l, end=' ')




