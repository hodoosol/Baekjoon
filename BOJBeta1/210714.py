# 1874 스택 수열, 실버 3 _ for-else 문 쓰는 법 이제 완전히 알았다 ...
n = int(input())
nums = [i for i in range(1, n + 1)]
stack = []
now = 1
answer = []

for i in range(n) :
    x = int(input())
    while now <= x :
        stack.append(now)
        answer.append('+')
        now += 1
    if stack[-1] == x :
        stack.pop()
        answer.append('-')
    else :
        print('NO')
        break
else :
    for k in answer :
        print(k)





# 1158 요세푸스 문제, 실버 5 _ 초반에 어렵게 생각해서 헤매느라 꽤 걸림 ...
# 그래도 처음 아이디어 그대로 구현해보았다. good !
n, k = map(int, input().split())
circle = [i for i in range(1, n + 1)]
answer = []

for i in range(n) :
    x = k % len(circle)
    answer.append(circle[x - 1])

    if circle[x - 1] == circle[-1] :
        circle.pop()
    else :
        circle = circle[x:] + circle[:x - 1]

print('<', ', '.join(str(i) for i in answer), '>', sep='')




