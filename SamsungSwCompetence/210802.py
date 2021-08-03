# 3190 뱀, 골드 5
n = int(input())                                 # 문제 기본 입력
board = [[0] * n for i in range(n)]              # n = 보드 크기, 2차원 배열로 보드를 만들어 준다.
for i in range(int(input())) :                   # 사과의 개수를 입력 받고 그만큼 for문
    a, b = map(int, input().split())             # 사과의 좌표를 하나씩 입력 받아서
    board[a - 1][b - 1] = 1                      # 보드의 해당 좌표를 0에서 1로 업데이트

direct = []                                      # 뱀의 방향 변환 정보를 저장할 리스트 direct
for j in range(int(input())) :                   # 뱀의 방향 변환 횟수를 입력 받아서 그만큼 for문
    x, c = map(str, input().split())             # 게임 시작 시간으로부터 x초가 끝난 뒤 c로 방향 전환
    direct.append((int(x), c))                   # 하나씩 입력 받아서 direct 리스트에 추가

snake = [(0, 0)]                                 # 뱀은 1행 1열(0, 0)에 있다.
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]           # 동남서북의 방향을 미리 리스트 d에 저장
now = 0                                          # 지금 뱀의 방향을 나타내는 변수 now
time = 0                                         # 시작한 시점으로부터 몇 초 지났는지 저장할 변수 time
X, Y = 1, 1                                      # 1초마다 한 번씩 이동하는 뱀의 좌표 X, Y

while True :                                     # 보드 밖으로 나가거나, 자신의 몸과 부딪히면 탈출하는 while문
    time += 1                                    # 1초 증가
    X += d[now][0]                               # 뱀이 이동하는 좌표 X, Y
    Y += d[now][1]
    if 1 <= X <= n and 1 <= Y <= n :             # 뱀이 보드 안에 있다면,
        snake.append((X, Y))                     # snake에 좌표 추가
        for i in snake[:-1] :                    # snake의 현재 좌표 제외, 이전의 좌표 중에 현재 좌표가 있다면, 게임 종료.
            if (X, Y) == i :                     # 즉, 스스로의 몸에 닿았다면 종료
                print(time)                      # 시간 출력하고 while문 탈출
                exit(0)
        if board[X - 1][Y - 1] == 0 :            # 보드의 해당하는 좌표값이 사과도 아니고 벽도 아니라면
            snake.pop(0)                         # 뱀이 이동하므로 꼬리에 해당하는 부분은 pop
        if board[X - 1][Y - 1] == 1 :            # 보드의 해당하는 좌표값에 사과가 있다면
            board[X - 1][Y - 1] = 0              # 사과를 먹었으므로 값을 0으로 바꿔준다.

    else :                                       # 뱀이 보드를 벗어났다면,
        print(time)                              # 시간을 출력하고
        break                                    # while문 탈출

# 뱀이 전환할 방향이 아직 남아있고 == direct 리스트가 비어있지 않고,
    if direct and time == direct[0][0] :         # 뱀의 방향을 전환해야 할 시간이 되면,
        if direct[0][1] == 'D' :                 # 전환할 방향이 D이고 (오른쪽이고)
            if now < 3 :                         # 현재 뱀의 방향이 동,남,서라면 오른쪽으로 이동하기 위해서는
                now = now + 1 #if now < 3 else 0 # 리스트 d의 다음 요소를 전환할 방향으로 설정해야 한다.
            else :                               # 현재 뱀의 방향이 북이라면
                now = 0                          # 리스트 d의 맨 처음 요소로 방향을 전환해야 한다.
            direct.pop(0)                        # 방향 전환이 끝났으므로 pop

        elif direct[0][1] == 'L' :               # 전환할 방향이 L이라면 (왼쪽이라면)
            if now > 0 :                         # 현재 뱀의 방향이 남,서,북이라면 왼쪽으로 이동하기 위해서는
                now = now - 1 #if now > 0 else 3 # 리스트 d의 이전 요소를 전환할 방향으로 설정해야 한다.
            else :                               # 현재 뱀의 방향이 동이라면
                now = 3                          # 리스트 d의 맨 마지막 요소로 방향을 전환해야 한다.
            direct.pop(0)                        # 방향 전환이 끝났으므로 pop




