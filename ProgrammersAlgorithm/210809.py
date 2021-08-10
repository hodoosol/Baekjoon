# 프로그래머스 도둑질, level 4
def solution(money):
    M = len(money)
    case1 = [0] * M
    case2 = [0] * M
    # 첫 번째 집을 털 경우
    case1[0] = money[0]
    for i in range(1, M - 1):
        case1[i] = max(case1[i - 1], case1[i - 2] + money[i])
        print(case1)
    # 첫 번째 집을 털지 않을 경우
    case2[0] = 0
    for j in range(1, M):
        case2[j] = max(case2[j - 1], case2[j - 2] + money[j])
        print('----', case2)
    return max(case1[-2], case2[-1])




