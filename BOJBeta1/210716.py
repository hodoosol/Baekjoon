# 5430 AC, 골드 5 _ 틀렸습니다 2번에 시간 초과 2번 ! 5번의 시도 끝에 성공 ..
import sys
input = lambda : sys.stdin.readline().strip()         # 입력받는 시간을 줄이기위해 sys 라이브러리 사용

for i in range(int(input())) :                        # 문제 입력받기
    p = input()
    n = int(input())
    nums = input()

    nums = nums[1:-1]                                  # [] 제거
    if not nums :
        nums = []                                      # []를 제거한 뒤 빈 문자열이라면 빈 리스트 할당
    else :
        nums = list(map(int, nums.split(',')))         # 아니라면 쉼표 , 를 기준으로 숫자만 리스트에 넣기

    r = False                                          # 리스트를 뒤집는 R 명령어가 몇 번 나오느냐에 따라
                                                       # 지금 뒤집혀있는지 상태를 파악하기 위해 r 변수 생성, 초기값 False
    for j in p :                                       # 명령어 모음 p의 원소 하나씩 for문
        if j == 'R' :                                  # j가 R이라면 r값을 뒤집어준다
            r = not r
        elif j == 'D' and nums :                       # j가 D이고 숫자 리스트가 비어있지 않다면,
            if r == True :                             # 리스트가 뒤집어진 상태라면 맨 오른쪽 숫자를 제거
                nums.pop()
            else :                                     # 뒤집혀있지 않은 상태라면 맨 왼쪽 숫자를 제거
                nums.pop(0)
        else :                                         # j가 D이고 숫자 리스트가 비어있다면,
            print('error')                             # error를 출력하고 반복문을 빠져나온다
            break

    else :                                             # 위 for문 동안 break된 적이 없다면,
        if r == True :                                 # r값이 True라면 숫자 리스트를 뒤집어주고
            nums = reversed(list(nums))                # False라면 숫자 리스트 그대로 출력해준다
        print('[', ','.join(str(i) for i in nums), ']', sep='')




