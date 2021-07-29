# 2456 나는 학급회장이다, 브론즈 1 _ 무식하게 풀기
n = int(input())
first = []
second = []
third = []
sums = [0, 0, 0]

for i in range(n) :
    x, y, z = map(int, input().split())
    first.append(x)
    sums[0] += x
    second.append(y)
    sums[1] += y
    third.append(z)
    sums[2] += z
Max = max(sums)

if len(set(sums)) == 3 :
    print(sums.index(Max) + 1, Max)
else :
    three = [first.count(3), second.count(3), third.count(3)]
    th_cnt, th_idx = three.count(max(three)), three.index(max(three))

    if th_cnt== 1 and Max == sums[th_idx] :
        print(th_idx + 1, Max)

    else :
        two = [first.count(2), second.count(2), third.count(2)]
        tw_cnt, tw_idx = two.count(max(two)), two.index(max(two))

        if tw_cnt == 1 and Max == sums[tw_cnt] :
            print(tw_cnt + 1, Max)
        else :
            print(0, Max)





# 5354 J박스, 브론즈 3
for i in range(int(input())) :
    n = int(input())
    if n < 3 :
        for j in range(n) :
            print('#' * n)
        print()
    else :
        print('#' * n)
        for j in range(n - 2) :
            print('#{0}#'.format('J' * (n - 2)))
        print('#' * n)
        print()





# 5361 전투 드로이드 가격, 브론즈 3
droid = [350.34, 230.90, 190.55, 125.30, 180.90]

for i in range(int(input())) :
    case = list(map(int, input().split()))
    cost = 0
    for j in range(5) :
        cost += (case[j] * droid[j])
    print('${:.2f}'.format(cost))




