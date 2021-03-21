# 5063
case = int(input())

for i in range(case) :
    non, ad, cost = map(int, input().split())
    if ad - cost > non :
        print('advertise')
    elif ad - cost < non :
        print('do not advertise')
    else :
        print('does not matter')





# 10102
judge = int(input())
vote = input()
A = vote.count('A')
B = vote.count('B')

if A > B :
    print('A')
elif A < B :
    print('B')
else :
    print('Tie')





# 10886
n = int(input())
survey = []
for i in range(n) :
    m = int(input())
    survey.append(m)

if survey.count(1) > survey.count(0) :
    print('Junhee is cute!')
else :
    print('Junhee is not cute!')





# 10988
word = input()
length = len(word)
result = 1

for i in range(0, length // 2) :
    if word[i] != word[length - 1 - i] :
        result = 0

print(result)





# 10988 _ reversed 함수 사용하기 . . .
word = list(input())
reversed_word = list(reversed(word))

if word == reversed_word :
    print(1)
else :
    print(0)




