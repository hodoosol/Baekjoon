# 6588 골드바흐의 추측, 실버 1
# 그때 그때 소수인지 판별하지 않고 소수를 먼저 모두 구해 놓고 확인하기로 했다.
import sys                                      # 입력 시간을 줄이기 위해 sys 라이브러리 사용
input = lambda : sys.stdin.readline().strip()
# 에라토스테네스의 체 사용
num = 1000000                                   # 문제의 범위가 100만 이하이므로 그 안에서 소수 구하기
prime = [False,False] + [True] * num            # 0, 1은 소수가 아니므로 False로 미리 설정, 범위만큼 True 할당
for i in range(2, num + 1) :                    # 2부터 100만까지 for문
    if prime[i] :                               # 만약 그 숫자에 해당하는 값이 True라면, (현재 prime의 인덱스와 실제 수가 동일)
        for j in range(i * 2, num + 1, i) :     # 그 수의 2배수를 모두 False로 바꾼다.
            prime[j] = False                    # 이런 식으로 체로 거르듯이 소수가 아닌 수를 지워나가는 것.
                                                # prime 리스트에는 숫자가 아닌 0부터 100만까지 소수라면 True, 아니라면 False로 채워져있다.
while True :                                    # while문 시작
    n = int(input())                            # 수를 입력 받고
    if n == 0 :                                 # 그 수가 0이라면 테스트케이스가 끝난 것이므로 탈출
        break
    for i in range(num) :                       # 0부터 100만 - 1까지 for문 (사실 의미는 없다 100까지 해도 되고 안해도 되고)
                                                # 왜냐하면 0부터 100만까지의 소수 중 가장 큰 소수가 999983이기 때문
        if prime[i] and prime[n - i] :          # 한 개의 소수 i를 불러와서 n-i 또한 소수이면 출력하고 탈출
            print(n, '=', i, '+', n - i)        # 즉, 소수 i와 n-i가 prime 리스트에서 True면 출력하는 것이다.
            break
    else :                                      # 골드바흐의 추측은 아직 해결되지 않은 문제이므로 이 else문은 없어도 될 것 같다. (내 추측)
        print('Goldbach\'s conjecture is wrong.')




        
