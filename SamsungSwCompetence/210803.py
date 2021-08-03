# 13458 시험 감독, 브론즈 2
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0

for i in a :
    i -= b
    cnt += 1
    if i > 0 :
        i /= c
        cnt += (int(i) + 1) if i > int(i) else (+ int(i))

print(cnt)
