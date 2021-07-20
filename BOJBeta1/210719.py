# 9095 1, 2, 3 더하기, 실버 3 _ 난 itertools가 좋아요
from itertools import product                    # 그 중에서도 product가 좋다
for i in range(int(input())) :                   # 테스트케이스만큼 for문 돌리기
    n = int(input())                             # n이 1 ~ 11 중 하나이므로 모든 경우의 수를 다 구하기로 했다
    ott = [1, 2, 3]                              # ott = one two three
    cnt = 0                                      # 케이스마다 그 합이 n이 되는지를 세어보기 위한 변수 cnt 초기화

    for j in range(1, n + 1) :                   # 1, 2, 3의 모든 조합을 만들어내는데, 1부터 n까지만 만들면 되므로 범위 설정
        ott_all = list(product(ott, repeat=j))   # 1 ... n의 순서대로 가능한 모든 조합을 만들어 할당한다
        for k in ott_all :                       # 할당된 값들 하나하나를 꺼내서
            if sum(k) == n :                     # 더해보고 그 결과가 n과 같다면 cnt에 1을 더해준다
                cnt += 1

    print(cnt)                                   # cnt 출력





# 14889 스타트와 링크, 실버 3 _ 와우 이게 실버 3이라고 ?? 문제 이해하는 게 좀 힘들었다 ..
from itertools import combinations                     # 조합을 구하기 위해 콤비네이션 라이브러리 불러오기
stat = []                                              # 능력치를 받을 리스트 생성
n = int(input())                                       # 몇 명의 선수인지 입력 받기
for i in range(n) :                                    # 선수의 수만큼 for문으로 능력치 입력 받기
    stat.append(list(map(int, input().split())))

index = set([i for i in range(n)])                     # 능력치에 접근할 인덱스를 리스트에 담아주고, 차집합 이용을 위해 set으로 변환
index_all = list(combinations(index, n // 2))          # 인덱스들의 모든 조합을 구한다

min_value = 101                                        # 최대 능력치는 100이므로 min()이용을 위해 101로 초기화

for j in index_all :                                   # 모든 조합을 for문으로 하나씩 꺼내서
    start = list(combinations(j, 2))                   # 선수 2명씩 조합을 만들어준다
    link = list(combinations(index - set(j), 2))       # start팀에 들어가지 않은 나머지를 차집합으로 구해주고 그것이 링크팀
                                                       # 링크팀도 선수 2명씩 조합을 만들어준다
    temp1, temp2 = 0, 0                                # start, link팀의 능력치를 더해서 잠시 넣어둘 변수 생성
    for k in range(len(start)) :                       # 팀의 길이만큼 for문
        x1 = start[k][0]                               # start팀의 선수 조합을 하나씩 꺼내서 능력치를 구하고
        y1 = start[k][1]
        temp1 += stat[x1][y1] + stat[y1][x1]           # temp1에 더하여 저장해둔다

        x2 = link[k][0]                                # link팀의 선수 조합을 하나씩 꺼내서 능력치를 구하고
        y2 = link[k][1]
        temp2 += stat[x2][y2] + stat[y2][x2]           # temp2에 더하여 저장해둔다

    min_value = min(min_value, abs(temp1 - temp2))     # 위 for문이 다 돌아가면 두 팀의 능력치 차이의 가장 작은 값을 구한다

print(min_value)                                       # 가장 작은 능력치 차이 출력




