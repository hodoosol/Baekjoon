# 9085
case = int(input())
for i in range(case) :
    input()
    print(sum(map(int, input().split())))





# 2490
for i in range(3) :
    game = sum(map(int, input().split()))
    if game == 3 :
        print('A')
    elif game == 2 :
        print('B')
    elif game == 1 :
        print('C')
    elif game == 0 :
        print('D')
    else :
        print('E')





# 2490 _ 2
score = {3 : 'A', 2 : 'B', 1 : 'C', 0 : 'D', 4 : 'E'}
for i in range(3) :
    game = sum(map(int, input().split()))
    print(score[game])





# 10797
day = int(input())
car = list(map(int, input().split()))
print(car.count(day))





# 2506
n = int(input())
test = list(map(int, input().split()))
cnt = 1
score = 0
for i in test :
    if i == 1 :
        score += cnt
        cnt += 1
    else :
        cnt = 1
print(score)





# 1546
n = int(input())
grade = list(map(int, input().split()))
high = max(grade)

for i in range(n) :
    grade[i] = grade[i] / high * 100

print(sum(grade) / float(n))





# 2455
result = 0
list = []
for i in range(4) :
    off, on = map(int, input().split())
    result -= off
    result += on
    list.append(result)
print(max(list))





