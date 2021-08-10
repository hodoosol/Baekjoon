# 프로그래머스 단속카메라, level 3

def solution(routes) :
    routes = sorted(routes, key = lambda x : (x[0], x[1]))
    end = routes[0][1]
    cnt = 1

    for i in range(1, len(routes)) :
        if routes[i][0] <=  end :
            end = min(end, routes[i][1])
        else :
            cnt += 1
            end = routes[i][1]

    return cnt

print(solution(routes))