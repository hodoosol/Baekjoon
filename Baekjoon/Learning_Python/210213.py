# 10039 _ 기본 리스트 함수 사용
grade_list = []
for i in range(5):
    grade_list.append(int(input()))
    if grade_list[i] < 40:
        grade_list[i] = 40

avg = sum(grade_list) / 5
print(int(avg))



# 10039 _  numpy 사용
import numpy as np
grade_list = []
for i in range (5) :
    grade_list.append(int(input()))
    if grade_list[i] < 40 :
        grade_list[i] = 40

avg = np.mean(grade_list)
print(int(avg))





# 1934 _ 시간 초과 _ 최소공배수 == 두 수의 곱 / 최대공약수 인걸 몰랐다.
testcase = int(input())
factorization = []
result = 1

for i in range(testcase) :
    a, b = map(int, input().split())
    # 소수 = 2
    prime = 2
    # 최대공약수 구하기 - 두 수가 소수보다 작아지면 탈출
    while a >= prime and b >= prime :
        # a, b 모두 소수로 나누어 떨어지면
        if a % prime == 0 and b % prime == 0 :
            # 나눈뒤 다시 저장
            a /= prime
            b /= prime
            # 그 소수를 리스트에 저장
            factorization.append(prime)
        # 나누어 떨어지지 않으면
        elif a % prime != 0 or b % prime != 0 :
            # 소수에 1을 더하여 다시 진행
            prime += 1
    # 소인수분해한 뒤 남은 두 수도 리스트에 저장
    factorization.append(int(a))
    factorization.append(int(b))
    # 리스트 안의 모든 수를 곱해서 결과값에 저장
    for i in factorization :
        result *= i
    print(result)
    # 케이스마다 초기화
    result = 1
    factorization = []



# 1934 _ 두번째 시도도 시간 초과 ...
def GCD(n, m) :
    prime = 2
    result = 1
    while n >= prime and m >= prime :
        if n % prime == 0 and m % prime == 0 :
            n /= prime
            m /= prime
            result *= prime

        elif n % prime != 0 or m % prime != 0 :
            prime += 1

    return result


testcase = int(input())
for i in range(testcase) :
    a, b = map(int, input().split())
    # 두 수의 곱을 함수로 구한 최대공약수로 나눈 것이 최소공배수
    print(int((a * b) / GCD(a, b)))




# 1934 _ 정답 _ 유클리드 호제법을 사용하여 최대공약수 구한 뒤,
# (a * b) / gcd = 최소공배수임을 이용해보자.

# 최대공약수 구하는 함수
def GCD(n, m) :
    # 첫번째 값의 크기가 커야하므로 설정해줌
    if n < m :
        n, m = m, n
    # n이 m으로 나누어떨어진다면 m이 최대공약수
    if n % m == 0:
        return m
    # 그렇지 않다면 m과 n을 m으로 나눈 나머지를 구하여 처음으로 돌아간다.
    if n % m != 0:
        return GCD(m, n % m)

# 테스트케이스의 개수 입력 받기
testcase = int(input())

# 테스트케이스의 개수만큼 for문을 돌리는 동안
# 최소공배수를 구할 두 수를 입력받고, 두 수의 곱을 최대공약수로 나누어준다.
# 그 값이 최소공배수이다. float으로 출력될 수 있으니 정수형으로 바꿔준다.
for i in range(testcase) :
    a, b = map(int, input().split())
    print(int((a * b) / GCD(a, b)))





# 2480
a, b, c = map(int, input().split())
if a == b == c :
    print(10000 + (a * 1000))

elif a == b or b == c or c == a :
    numlist = sorted([a, b, c])
    # 세 개중 두개가 같다면 오름차순 정렬하여 가운데 값이 동일한 값.
    print(1000 + (numlist[1] * 100))

elif a != b != c :
    print(max(a, b, c) * 100)





# 4101
while True :
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break

    elif a > b :
        print('Yes')

    elif a <= b :
        print('No')





# 10156
price, snack, money = map(int, input().split())
allowance = (price * snack) - money
if allowance > 0 :
    print(allowance)

elif allowance <= 0 :
    print(0)






