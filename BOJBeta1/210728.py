# 1735 분수 합, 실버 3
import math                                 # 최대공약수를 구하기위해 math 라이브러리 불러오기
num1, den1 = map(int, input().split())      # 분수 2개를 더해야하므로 num = 분자, den = 분모를 두 번 입력 받는다.
num2, den2 = map(int, input().split())

num3 = (num1 * den2) + (num2 * den1)        # 더해서 나오는 분수의 요소를 num3, den3라는 변수로 만들어주었다.
den3 = den1 * den2                          # 분모는 곱해주고, 분자는 자기자신이 아닌 다른 분모를 각각 곱하여 서로 더한다.

gcd = math.gcd(num3, den3)                  # 그렇게 나온 분모와 분자의 최소공약수를 구하고,

print(num3 // gcd, den3 // gcd, end=' ')    # 각각을 나눈 몫을 1번 띄어쓰기하여 출력한다.





1924 2007년, 브론즈 1
thirtyone = [1, 3, 5, 7, 8, 10, 12]
thirty = [4, 6, 9, 11]

x, y = map(int, input().split())
day = 0

if x >= 2 :
    for i in range(1, x) :
        if i in thirtyone :
            day += 31
        elif i in thirty :
            day += 30
        else :
            day += 28

day += y
day %= 7

if day == 1 :
    print('MON')
elif day == 2 :
    print('TUE')
elif day == 3 :
    print('WED')
elif day == 4 :
    print('THU')
elif day == 5 :
    print('FRI')
elif day == 6 :
    print('SAT')
else :
    print('SUN')





# 1924 _ 다른 버전 _ 코드는 짧지만 위의 코드보다 아주 조금 느림
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']    # 요일을 미리 리스트에 넣어놓기
ends = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]     # 각 달의 일 수를 리스트에 넣어놓기

x, y = map(int, input().split())                            # 문제 입력 받기
day = 0                                                     # 1월 1일부터 며칠이 지났는지 셀 변수

for i in range(x - 1) :                                     # 입력받은 날짜의 월 - 1만큼 for문
    day += ends[i]                                          # day 변수에 입력받은 월의 이전 달 * 일 수를 더함

day = (day + y) % 7                                         # 입력받은 날짜의 일 y를 더하고 7로 나눈다.

print(days[day])                                            # 7로 나눈 나머지에 해당하는 인덱스로 요일을 출력한다.




