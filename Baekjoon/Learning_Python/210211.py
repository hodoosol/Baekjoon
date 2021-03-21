# 2935
a = int(input())
operator = input()
b = int(input())

if operator == '+' :
    print(a + b)
elif operator == '*' :
    print(a * b)





# 9498
grade = int(input())

if grade >= 90 :
    print('A')
elif 89 >= grade >= 80 :
    print('B')
elif 79 >= grade >= 70 :
    print('C')
elif 69>= grade >= 60 :
    print('D')
else :
    print('F')





# 10817 _ 방법 1
# 리스트에 숫자 입력받고, 오름차순 정렬, 두번째 값 출력하기
# 이렇게 하면 세 개의 정수를 입력받아야 하는 문제와는 달리
# 더 적게, 더 많이 입력받아도 돌아가게 된다.
num_list1 = map(int, input().split())
num_list1 = sorted(num_list1)
print(num_list1[1])



# 10817 _ 방법 2
# 세 개의 정수만 입력 받을 수 있다 !, 문제대로 푼 것. 근데 더 길다.
a, b, c = map(int, input().split())

num_list2 = []
num_list2.append(a)
num_list2.append(b)
num_list2.append(c)

num_list2 = sorted(num_list2)

print(num_list2[1])





# 11653
n = int(input())
prime = 2

while n >= 2 :
    if n % prime == 0 :
        n /= prime
        print(prime)

    elif n % prime != 0 :
        prime += 1





# 1789
n = int(input())
num = 1
sum = 0

while n >= 1 :
        n -= num
        num += 1
        sum += 1

        if n < 0 :
            num -= 2
            sum -= 1
            n += num

if n == 0 :
    print(sum)





# 2753
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print(1)
else :
    print(0)




