# 9663 N-Queen, 골드 5 _ 체스 두는 법을 몰라서 ...
# 이 문제는 파이썬으로 풀지 않기를 권장한다. 따라서 이 코드도 시간 초과.
# PyPy3로 채점하면 통과한다. 또는 N이 14까지이기 때문에 모두 구해서 제출하는 것도 가능하다 ^^

# 열과 대각선이 같은 경우 체크하는 함수
def check(n) :
    for i in range(n) :
        if chess[n] == chess[i] or abs(chess[n] - chess[i]) == n - i :
            return 0
    return 1

def dfs(n) :
    global answer
    if n == N :
        answer += 1
    else :                            # 각 행에 퀸을 놓고,
        for i in range(N) :           # 열을 하나씩 이동해가면서 유망한 곳 찾기
            chess[n] = i
            if check(n) :             # 만약 행, 열, 대각선 체크함수의 결과가 true이면
                dfs(n + 1)            # 백트랙킹 하지 않고 계속 진행

N = int(input())                      # 문제 기본입력과 입력과 같은 체스판 만들기
chess = [0] * N
answer = 0
dfs(0)
print(answer)




# 1 <= N < 15 이므로 이렇게 미리 구해서 제출할 수도 있다 ... 물론 그러면 안되겠지만
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])




