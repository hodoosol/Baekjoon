# 3009
dot = []
for i in range(3):
    x, y = map(int, input().split())
    dot.append(x)
    dot.append(y)
# x, y 좌표 별로 슬라이싱
Xs = dot[: : 2]
Ys = dot[1 :: 2]
# 1개의 값만을 가지는 요소가 정답, 따로 저장한 뒤 출력
for i in range(3) :
    if Xs.count(Xs[i]) == 1 :
        x = Xs[i]
    if Ys.count(Ys[i]) == 1:
        y = Ys[i]

print(x, y)





# 2476
n = int(input())
prize = []
for i in range(n) :
    a, b, c = map(int, input().split())
    if a == b == c :
        prize.append(10000 + (a * 1000))

    if a == b or b == c or c == a :
        temp = sorted([a, b, c])
        prize.append(1000 + (temp[1] * 100))

    if a != b != c :
        prize.append(max(a, b, c) * 100)

print(max(prize))





# 2754
grade = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
         'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
         'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
         'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0}

print(grade[input()])





# 2884
hour, min = map(int, input().split())
min -= 45
if min < 0 :
    min += 60
    hour -= 1
    if hour < 0 :
        hour += 24

print(hour, min)





# 7567 _ while문 사용
dish = input()
i = 1
cnt = 10

while True :
    if i >= len(dish) :
        break
    if dish[i] == dish[i - 1] :
        cnt += 5
    elif dish[i] != dish[i - 1] :
        cnt += 10
    i += 1

print(cnt)




# 7567 _ for문 사용
dish = input()
cnt = 10

for i in range(1, len(dish)) :
    if dish[i] == dish[i - 1] :
        cnt += 5
    elif dish[i] != dish[i - 1] :
        cnt += 10

print(cnt)


