# 10162 _ 1번째 시도, 완전 길다.
time = int(input())
btn_a, btn_b, btn_c = 300, 60, 10
a = b = c = 0

while True :
    if time == 0 :
        print(a, b, c)
        break
    if time % btn_c != 0:
        print(-1)
        break
    if time // btn_a >= 1 :
        a += time // btn_a
        time %= btn_a
    if time // btn_b >= 1 :
        b += time // btn_b
        time %= btn_b
    if time // btn_c >= 1 :
        c += time //btn_c
        time %= btn_c





# 10162 _ 2번째 시도, 변수를 줄이고 알고리즘을 간단히 했다.
time = int(input())

if time % 10 == 0 :
    a = time // 300
    time %= 300
    b = time // 60
    time %= 60
    c = time // 10
    print(a, b, c)

else :
    print(-1)





# 10103
round = int(input())
seul = sol = 100

for i in range(round) :
    a, b = map(int, input().split())
    if a > b :
        sol -= a
    elif a < b :
        seul -= b

print(seul, sol, sep='\n')





# 10214
case = int(input())
for i in range(case) :
    yonsei = korea = 0
    for j in range(9) :
        y, k = map(int, input().split())
        yonsei += y
        korea += k
    if yonsei > korea :
        print('Yonsei')
    elif yonsei < korea :
        print('Korea')
    else :
        print('Draw')





# 11557
case = int(input())

for i in range(case) :
    school = []
    alcohol = []
    uni = int(input())
    for j in range(uni) :
        name, alc = input().split()
        school.append(name)
        alcohol.append(int(alc))
    # 제일 큰 알콜의 인덱스 = 그 알콜 섭취한 학교이름 인덱스
    print(school[alcohol.index(max(alcohol))])





# 10757
a, b = map(int, input().split())
print(a+b)



