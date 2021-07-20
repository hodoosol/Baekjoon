# 2217 로프, 실버 4
n = int(input())                             # 문제 입력 받기
rope = []                                    # n = 로프의 개수, rope = 로프가 버틸 수 있는 최대 무게
for i in range(n) :
    rope.append(int(input()))

rope.sort(reverse=True)                      # 내림차순으로 정렬하여 효율성 높이기
weight = 0                                   # max()를 사용해야 하므로 weight 변수를 0으로 초기화

for j in range(n) :                          # 로프의 개수만큼 for문 돌리기
    weight = max(weight, rope[j] * (j + 1))  # 버틸 수 있는 최대 무게가 큰 로프부터 꺼내서
                                             # 첫 번째 로프 혼자 버티는 무게, 두 번째 로프의 무게로 둘이 함께 버티는 무게,
                                             # 세 번째 로프의 무게로 셋이 함께 버티는 무게 ... 끝까지를 차례로 따져보고
print(weight)                                # 가장 큰 무게를 출력한다.




