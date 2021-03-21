# 10809
s = input()
alpha = []
for i in range(ord('a'), ord('z') + 1) :
    alpha.append(-1)
for j in range(len(s)) :
    if alpha[ord(s[j]) - 97] == -1 :
        alpha[ord(s[j]) - 97] = j

print(*alpha)





# 3058
for i in range(int(input())) :
    nums = list(map(int, input().split()))
    temp = []
    for j in nums :
        if j % 2 == 0 :
            temp.append(j)
    print(sum(temp), min(temp))





# 5800
for i in range(int(input())) :
    grade = list(map(int, input().split()))
    grade = sorted(grade[1:])
    temp = []
    for j in range(len(grade) - 1) :
        temp.append(grade[j + 1] - grade[j])
    print('Class', i + 1, '\nMax {0}, Min {1}, Largest gap {2}'
          .format(max(grade), min(grade), max(temp)))





# 10870
fib = [0, 1]
n = int(input())
for i in range(n - 1) :
    fib.append(fib[i] + fib[i + 1])
print(fib[n])





# 5576 _ 1
w = []
k = []
for i in range(10) :
    w.append(int(input()))
for j in range(10) :
    k.append(int(input()))
w.sort()
k.sort()
print(sum(w[7:]), sum(k[7:]))





# 5576 _ 2
w = sorted([int(input()) for _ in range(10)])
k = sorted([int(input()) for _ in range(10)])
print(sum(w[7:]), sum(k[7:]))




