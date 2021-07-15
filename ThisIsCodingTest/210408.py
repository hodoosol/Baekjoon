# 11399 _ ATM
n = int(input())
time = sorted(list(map(int, input().split())))
res = 0
tmp = 0
for i in time :
    # tmp에 time의 원소들을 누적해서 더하고
    tmp += i
    # 결과값에 더해준다.
    res += tmp
print(res)





# 13305 _ 주유소
n = int(input())
road = list(map(int, input().split()))
gas = list(map(int, input().split()))
# 임시 변수에 첫 도시의 기름 값 저장.
tmp = gas[0]
# 첫 도시에서는 무조건 그 기름을 사야하므로 결과 값에 저장.
res = tmp * road[0]
# 첫 도시를 처리했으니 인덱스는 for문의 인덱스는 1부터 시작.
for i in range(1, n - 1) :
    # 만약 이전 도시의 기름이 현재 도시의 기름보다 싸다면
    if tmp <= gas[i] :
        # 결과 값 = 이전 도시의 기름을 구입하여 이동한 금액.
        res += tmp * road[i]
    else :
        # 현재 도시의 기름이 이전 도시의 기름보다 싸다면
        # 결과 값 = 현재 도시의 기름을 구입하여 이동한 금액.
        res += gas[i] * road[i]
        # 임시 변수에 현재 도시의 기름값을 저장.
        tmp = gas[i]
# 출력
print(res)










