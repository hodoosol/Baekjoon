# 1966 프린터 큐, 실버 3
# 딕셔너리로 풀어보려다 슬라이싱을 사용할 수 없는 게 너무 불편해서
# 그냥 리스트 2개로 풀었다.

# 테스트케이스만큼 for문
for i in range(int(input())) :
    n, x = map(int, input().split())                            # n = 문서의 개수, x = 알아볼 문서의 현재 위치
    important = list(map(int, input().split()))                 # 문서 별 중요도를 리스트로 입력 받음

    files = [chr(i) for i in range(65, 65 + n)]                 # 문서를 알아보기 쉽게 A B C ... 로 이름을 붙여주었다
    target = files[x]                                           # 알아볼 문서의 이름을 target이라는 변수에 저장
    answer = []                                                 # 문서들의 출력 순서를 리스트에 담아두기 위해 빈 리스트 생성

    for j in range(n) :                                         # 문서들의 개수만큼 for문
        temp = important.index(max(important))                  # 가장 중요도가 높은 문서의 인덱스를 temp에 담아두었다.
                                                                # 현재 중요도 리스트와 문서 이름 리스트의 순서는 일치한다 !!!
        answer.append(files[temp])                              # 가장 중요도가 높은 문서를 answer 리스트에 담는다 (출력하는 것)
        files = files[temp + 1:] + files[:temp]                 # 출력된 문서를 기준으로 뒤에 있던 문서가 그대로 앞에 오고
                                                                # 앞에 있던 문서는 그대로 뒤로 온다 (선입선출되는 큐의 구조)
                                                                # [abcdeFghijk]의 문서들이 있을 때 F가 출력된 후에 [ghijkabcde]가 된다
        important = important[temp + 1:] + important[:temp]     # 마찬가지로 중요도 리스트도 똑같이 변형해 준다

    print(answer.index(target) + 1)                             # 모두 처리한 후 답인 target의 인덱스 + 1을 출력



    

