# 1547 공, 브론즈 3
cups = [1, 2 ,3]
for i in range(int(input())) :
  x, y = map(int, input().split())
  cups[x - 1], cups[y - 1] = cups[y - 1], cups[x - 1]

print(cups.index(1) + 1)



# 1547 _ 다른 풀이
cups = [-1, 1, 2, 3]
for i in range(int(input())) :
  x, y = map(int, input().split())
  cups[x], cups[y] = cups[y], cups[x]

print(cups.index(1))





# 1568 새, 브론즈 2
n = int(input())        # 새의 마리수 n
i = 1                   # 현재 부르고 있는 자연수 노래 k
cnt = 0                 # 몇 초 걸리는지 세는 cnt
while True :
  if n > i :
    n -= i
    i += 1
    cnt += 1
  elif n == i :
    print(cnt + 1)
    break
  else :
    i = 1





# 1731 추론, 브론즈 2
nums = []
for i in range(int(input())) :
  nums.append(int(input()))

a, b = nums[1] - nums[0], nums[2] - nums[1]
c, d = nums[1] // nums[0], nums[2] // nums[1]

if a == b :
  print(nums[-1] + a)
else :
  print(nums[-1] * c)





# 1834 나머지와 몫이 같은 수 , 브론즈 1
n = int(input())
nums = []
for i in range(1, n) :
    nums.append((n * i) + i)
print(sum(nums))





# 1864 문어 숫자, 브론즈 3
octp = {'-' : 0, '\\' : 1, '(' : 2, '@' : 3,
        '?' : 4, '>' : 5, '&' : 6, '%' : 7, '/' : -1}
while True :
    x = input()
    if x == '#' :
        break
    res = 0
    l = len(x)
    for i in range(l) :
        res += octp[x[i]] * (8 ** (l - i - 1))
    print(res)




