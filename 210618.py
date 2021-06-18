# 10815 숫자 카드, 실버 4 _ 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find = map(int, input().split())

for i in find :
    if i in cards :
        print(1, end=' ')
    else :
        print(0, end=' ')





# 10815 _ 재도전 _ 이분 탐색
import sys
n = int(input())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(input())
find = map(int, sys.stdin.readline().split())

for i in find :
    start = 0
    end = n - 1
    while start <= end :
        mid = (start + end) // 2
        if cards[mid] == i :
            print(1, end=' ')
            break
        elif cards[mid] > i :
            end = mid - 1
        else :
            start = mid + 1
    else :
        print(0, end=' ')





# 10815 _ 카드를 set으로 중복 제거 해주면 이진탐색 안해도 가능
import sys
input = sys.stdin.readline

n = input()
cards = set(input().split())
m = input()
find = input().split()

for i in find :
    if i in cards :
        print(1, end=' ')
    else :
        print(0, end=' ')





# 10828 스택, 실버 4
import sys
stack = []

for i in range(int(input())) :
    order = list(sys.stdin.readline().split())
    if order[0] == 'push' :
        stack.append(int(order[1]))
    elif order[0] == 'pop' :
        if not stack :
            print(-1)
        else :
            print(stack[-1])
            stack.pop()
    elif order[0] == 'size' :
        print(len(stack))
    elif order[0] == 'empty' :
        if not stack :
            print(1)
        else :
            print(0)
    elif order[0] == 'top' :
        if not stack :
            print(-1)
        else :
            print(stack[-1])





# 10828 _ 다른 풀이
import sys
stack = []

for i in range(int(input())) :
    order = sys.stdin.readline().rstrip()
    if 'push' in order :
        num = order.split(' ')[1]
        stack.append(int(num))
    elif order == 'pop' :
        if not stack :
            print(-1)
        else :
            print(stack[-1])
            stack.pop()
    elif order == 'size' :
        print(len(stack))
    elif order == 'empty' :
        if not stack :
            print(1)
        else :
            print(0)
    elif order == 'top' :
        if not stack :
            print(-1)
        else :
            print(stack[-1])




