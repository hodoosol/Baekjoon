# 1181 단어 정렬, 실버 4
import sys
n = int(input())
words = [i for i in range(51)]                      # 주어지는 문자열의 길이가 50을 넘지 않기 때문에
                                                    # 0부터 50까지 숫자로 채운 리스트를 생성했다.
                                                    # words[0]은 사용하지 않으므로 words의 인덱스가 입력받은 문자열의 길이가 된다.
for i in range(n) :
    x = sys.stdin.readline().rstrip()               # 문자열을 입력받고 개행문자 \n을 rstrip()으로 삭제해준다.
    if len(x) == words[len(x)] :                    # 만약 words[길이] 원소가 숫자라면 즉, 아직 입력받은 적이 없는 상태라면
        words[len(x)] = x + ' '                     # 그 숫자 원소를 문자열로 치환하고 구분을 위해 공백을 같이 입력해준다.
    else :                                          # 만약 이미 입력받은 문자열이 있다면
        words[len(x)] += x + ' '                    # 그 뒤에 지금 입력받은 문자열을 추가하고 공백을 같이 입력한다.

for j in words :                                    # words의 원소 하나하나를 가지고
    if type(j) == str :                             # 그 원소가 str이라면 즉, 가능한 문자열의 길이 1부터 50 중에 입력받은 것이 있다면
        j = j.rstrip()                              # 원소의 마지막 공백 ' '을 지우고
        result = []                                 # 출력을 위한 리스트 result를 초기화한 뒤
        result = list(set(map(str, j.split(' '))))  # 띄어쓰기를 기준으로 원소를 나누어 result에 입력, set으로 공백 제거 뒤 다시 list 변환
        for k in sorted(result) :                   # 정렬하여 한 줄에 원소 하나씩 출력한다.
            print(k)





# 11650 좌표 정렬하기, 실버 5
# 맨 처음 sort로 했다가 실패해서 ... 덕지덕지 사족이 붙은 코드이다.
# 그래도 도전한 것에 의의가 있기에 정리
import sys
location = []
for i in range(int(input())) :                                   # x, y 좌표들을 2차원 배열로 입력받는다.
    xy = list(map(int, sys.stdin.readline().rstrip().split()))
    location.append(xy)

location.sort(key=lambda x : x[0])                               # x 좌표를 기준으로 정렬한다.
result = []                                                      # 정답 출력을 위한 리스트 result 생성

for j in location :                                              # 좌표 하나하나 마다
    if not result or result[-1][0] == j[0] :                     # 정답 리스트가 비어있거나 x 좌표가 동일하다면
        result.append(j)                                         # result 리스트에 추가 (2차원)
    else :                                                       # 그렇지 않다면 == 새로운 x좌표가 들어왔다면
        result.sort(key=lambda x : x[1])                         # result에 들어있던 좌표들을 y기준으로 정리한 뒤
        for k in result :                                        # 하나씩 출력한다.
            print(k[0], k[1])
        result = [j]                                             # result를 새로운 x좌표를 가진 좌표로 초기화한다. (2차원)

result.sort(key=lambda x: x[1])                                  # 마지막으로 남아있는 좌표들도 정렬하여 출력한다.
for k in result :
    print(k[0], k[1])





# 11650 _ sort로 재도전
import sys
location = []
for i in range(int(input())) :
    xy = list(map(int, sys.stdin.readline().rstrip().split()))
    location.append(xy)

location.sort(key=lambda x : (x[0], x[1]))        # (x[0], x[1]) -> 괄호 필수 !

for j in location :
    print(j[0], j[1])





# 11650 _ sorted로 재도전
import sys
location = []
for i in range(int(input())) :
    xy = list(map(int, sys.stdin.readline().rstrip().split()))
    location.append(xy)

location = sorted(location)

for j in location :
    print(j[0], j[1])





# 11651 좌표 정렬하기 2, 실버 5
import sys
location = []
for i in range(int(input())) :
    xy = list(map(int, sys.stdin.readline().rstrip().split()))
    location.append(xy)

location.sort(key=lambda x : (x[1], x[0]))            # 정렬 순서만 바꾸어주면 된다.

for j in location :
    print(j[0], j[1])





# 10867 중복 빼고 정렬하기, 실버 5
n = input()
nums = sorted(list(set(map(int, input().split()))))
print(*nums)




