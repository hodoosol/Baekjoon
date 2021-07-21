# 2512 예산, 실버 3 _ 꼭 완전탐색으로 풀어보고 싶었다. 당연히 시간 초과.
# PyPy3로 채점하면 통과한다. ㅎㅎ
import sys
input = lambda : sys.stdin.readline().strip()          # 입력 시간을 줄이기 위해 sys라이브러리 사용

n = int(input())                                       # 문제 입력 받기
ask = sorted(list(map(int, input().split())))          # n = 도시의 개수, ask = 각 도시가 요청한 예산
budget = int(input())                                  # budget = 나라에서 사용 가능한 예산

if sum(ask) <= budget :                                # 만약 조정 없이도 모든 도시가 요청한 예산을 편성할 수 있다면
    print(max(ask))                                    # 그냥 가장 큰 예산을 출력하고 문제 끝

else :                                                 # 아니라면
    while True :                                       # while문 시작
        if sum(ask) > budget :                         # 각 도시가 원하는 모든 예산을 더한 것이 총 예산보다 크다면, 조정 필요
            for i in range(n) :                        # 도시의 개수만큼 for문
                if ask[i] >= ask[-1] :                 # ask는 오름차순 정렬되어 있으므로 맨 끝 요소가 가장 큰 예산이다.
                    ask[i] -= 1                        # 가장 큰 예산부터 차례대로 1씩 빼주다가, 그 다음으로 큰 요소와 같은 값이 되면
                                                       # 그 요소도 1씩 빼주고, 또 다음으로 큰 요소와 같은 값이 되면 함께 1씩 빼주는 것을 반복
        else :                                         # 그러다 각 도시가 원하는 모든 예산을 더한 것이 총 예산보다 같거나 작아지면,
            print(ask[-1])                             # 그것이 상한선이므로 출력하고, while문을 빠져나오면 된다.
            break





# 2512 _ 이번엔 이분탐색으로 풀어보았다. 거의 대부분 이분탐색으로 푼 듯.
# 이분탐색이 역시 빠르다. pypy3로 완전탐색 한 것과 메모리와 시간이 10배 이상 차이난다.
import sys                                        # 기본 입력은 동일하다.
input = lambda : sys.stdin.readline().strip()

n = int(input())
ask = sorted(list(map(int, input().split())))
budget = int(input())

start = 0                                         # 이분탐색을 위해 시작점과 끝점을 start, end 변수로 만들어준다.
end = max(ask)                                    # 시작점과 끝점이란 구해야할 예산 상한선의 최소값과 최대값을 뜻한다.

while(start <= end) :                             # 시작점이 끝점보다 더 커지면 탐색을 종료하는 while문
    mid = (start + end) // 2                      # 중간점은 시작점과 끝점의 평균이다.
    temp = 0                                      # 적절한 상한선을 찾기 위해 중간 과정을 담아둘 temp변수 생성
    for i in ask :                                # 각 도시가 바라는 예산들을 하나씩 꺼내는 for문
        if i >= mid :                             # 각 도시가 바라는 예산이 중간점보다 크다면
            temp += mid                           # 상한선을 담아두는 변수 temp에 중간점의 값을 더한다.
        else :                                    # 아니라면 그 도시의 예산을 더한다.
            temp += i

    if temp <= budget :                           # for문이 끝난 뒤 상한선의 값이 예산보다 작다면
        start = mid + 1                           # 상한선이 더 커져야하므로 시작점을 중간점의 값 +1로 설정한다.
    else :                                        # 상한선의 값이 예산보다 크다면
        end = mid - 1                             # 상한선이 더 작아져야하므로 끝점을 중간점의 값 -1로 설정한다.
print(end)                                        # while문이 종료되면 끝점을 출력한다.




