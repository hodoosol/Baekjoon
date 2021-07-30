# 5347 LCM, 실버 4
# 유클리드 호제법으로 최소공약수 구한 뒤, 최소공배수 구하기
for i in range(int(input())) :
    a, b = map(int, input().split())     # 문제 기본 입력
    x, y = a, b                          # 원래 숫자를 기억해두어야하므로 새로운 변수 x, y에 a, b의 값 복사
    while y :                            # y가 0이 되면 while문 탈출
        x, y = y, x % y                  # 유클리드 호제법, x와 y의 최대공약수 == y와 x를 y로 나눈 나머지의 최대공약수
    answer = (a * b) // x                # 그렇게 구해진 최대공약수 x로 원래 수 a와 b의 곱을 나눈 몫이 최소공배수
    print(answer)                        # 정답 출력




    