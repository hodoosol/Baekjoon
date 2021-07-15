# 2525
hour, min = map(int, input().split())
time = int(input())

hour += time // 60
min += time % 60

if min >= 60 :
    hour += 1
    min -= 60

if hour >= 24 :
    hour %= 24

print(hour, min)





# 2530
hour, min, sec = map(int, input().split())
time = int(input())

sec += time % 60
time = time // 60
if sec >= 60 :
    min += 1
    sec -= 60

min += time % 60
if min >= 60 :
    hour += 1
    min -= 60

hour += time // 60
if hour >= 24 :
    hour %= 24

print(hour, min, sec)





# 2914
import math
song, mean = map(int, input().split())
melody = (mean - 1) * song
print(melody + 1)





# 5355
testcase = int(input())

for i in range(testcase) :
    l = list(input().split())
    result = float(l[0])

    for j in range(len(l) - 1) :
        if l[j + 1] == '@' :
            result *= 3
        elif l[j + 1] == '%' :
            result += 5
        elif l[j + 1] == '#' :
            result -= 7

    print('%0.2f' %result)





# 2675
T = int(input())

for i in range(T) :
    R, S = input().split()
    R = int(R)
    S = list(S)
    for j in S :
        print(j * R, end='')
    print()




