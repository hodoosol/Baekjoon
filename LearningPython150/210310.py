# 2953
rank = []
for i in range(5) :
    score = sum(map(int, input().split()))
    rank.append(score)
print(rank.index(max(rank)) + 1, max(rank))





# 3052 _ 1
remain = []
for i in range(10):
    n = int(input())
    remain.append(n % 42)
remain = set(remain)
print(len(remain))





# 3052 _ 2
remain = []
for i in range(10) :
    remain.append(int(input()) % 42)
print(len(set(remain)))





# 1292
seq = []
a, b = map(int, input().split())
for i in range(1, 1001) :
    for j in range(i) :
        seq.append(i)
print(sum(seq[a - 1 : b]))





# 3460
case = int(input())
for i in range(case) :
    # 2진수로 바꾸고 뒤집어주기
    n = bin(int(input()))
    n = list(n[::-1])
    for j in range(len(n)) :
        if n[j] == '1' :
            print(j, end=' ')





# 10807
n = int(input())
num = list(map(int, input().split()))
print(num.count(int(input())))





# 1037
count = int(input())
real = list(map(int, input().split()))
print(max(real) * min(real))





# 1065
n = int(input())
cnt = 0

for i in range(1, n + 1) :
    if i // 100 < 1 :
        cnt += 1
    else :
        n = list(map(int, str(i)))
        if n[1] - n[0] == n[2] - n[1] :
            cnt += 1

print(cnt)





