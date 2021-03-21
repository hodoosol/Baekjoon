# 1063
a, b = map(int, input().split())
print(a if a>b else b)



# 1064
c, d, e = map(int, input().split())
print(min(c, d, e))



# 1065
f, g, h = map(int, input().split())
if f % 2 == 0 :
    print(f)
if g % 2 == 0 :
    print(g)
if h % 2 == 0 :
    print(h)



# 1066
def oddandeven(n):
    if n % 2 == 0 :
        print('even')
    else :
        print('odd')

i, j, k = map(int, input().split())
oddandeven(i)
oddandeven(j)
oddandeven(k)



# 1067
l = int(input())
if l > 0 :
    print('plus')
elif l < 0 :
    print('minus')
if l % 2 == 0 :
    print('even')
else :
    print('odd')



# 1068
grade = int(input())
if grade >= 90 :
    print('A')
elif grade >= 70 :
    print('B')
elif grade >= 40 :
    print('C')
else :
    print('D')



# 1069
evaluation = input()
if evaluation == 'A' :
    print('best!!!')
elif evaluation == 'B' :
    print('good!!')
elif evaluation == 'C' :
    print('run!')
elif evaluation == 'D' :
    print('slowly~')
else :
    print('what?')



# 1070
m = int(input())

if m==12 or m==1 or m==2 :
    print('winter')
elif m==3 or m==4 or m==5 :
    print('spring')
elif m==6 or m==7 or m==8 :
    print('summer')
elif m==9 or m==10 or m==11 :
    print('fall')



# 1071
numbers = input().split()
for n in numbers :
    if n == '0' :
        break
    print(n)



# 1072
o = int(input())
nums = map(int, input().split())
for n in nums :
    print(n)



# 1073 p, i, 0 모두 string
p = input().split()
for i in p :
    if i == '0' :
        break
    print(i)



# 1073 int로 하려면
p = map(int, input().split())
for i in p :
    if int(i) == 0 :
        break
    print(i)



# 1074
q = int(input())
while 0<q<=100 :
    print(q)
    q -= 1



# 1075
r = int(input())
while 0<r<=100 :
    r -= 1
    print(r)



# 1076
s = ord(input())
a = ord('a')
while a <= s :
    print(chr(a), end=' ')
    a += 1



# 1077
t = int(input())
i = 0
while i <= t :
    print(i)
    i += 1



# 1077 모범답안
a=input()
n=int(a)

for i in range(n+1):
    print(i)
