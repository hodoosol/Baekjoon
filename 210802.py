# 3190 뱀, 골드 5
n = int(input())
board = [[0] * n for i in range(n)]
for i in range(int(input())) :
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

direct = []
for j in range(int(input())) :
    x, c = map(str, input().split())
    direct.append((int(x), c))

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]    
