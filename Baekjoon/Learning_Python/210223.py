# 1977
m = int(input())
n = int(input())
result = []

for i in range(1, n) :
    if m <= (i * i) <= n :
        result.append(i * i)

if not result :
    print(-1)
else :
    print(sum(result))
    print(min(result))




# 11098
case = int(input())
cost_list = []
name_list = []

for i in range(case) :
    num = int(input())

    for j in range(num) :
        cost, name = input().split()
        cost_list.append(int(cost))
        name_list.append(name)

    print(name_list[cost_list.index(max(cost_list))])
    del cost_list[:]
    del name_list[:]





# 5635 _ 1번 _ int -> str -> int 바꾸는 부분 비효율적
student = int(input())

NAME = []
birth = []

for i in range(student) :
    name, day, month, year = input().split()
    if int(month) // 10 == 0 :
        month = str('0' + month)
    if int(day) // 10 == 0 :
        day = str('0' + day)
    birth.append(int(year + month + day))
    NAME.append(name)

print(NAME[birth.index(max(birth))])
print(NAME[birth.index(min(birth))])




# 5635 _ 2번 _ len()을 이용해서 형변환 횟수 줄이기
student = int(input())

NAME = []
birth = []
for i in range(student):
    name, day, month, year = input().split()
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    birth.append(year + month + day)
    NAME.append(name)

print(NAME[birth.index(max(birth))])
print(NAME[birth.index(min(birth))])

