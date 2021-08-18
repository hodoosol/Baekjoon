# 프로그래머스 하노이의 탑, Level 3
def solution(n):
    answer = [[]]
    answer.append([1, 3]) if n % 2 == 1 else answer.append([1, 2])
    answer.append([1, 2]) if n % 2 == 1 else answer.append([1, 3])
    chk = n - 2

    while chk != 0 :
        for i in range(chk) :
            if n % 2 == 1 :
                answer.append([3, 2])
            else :
                answer.append([2, 3])
        
    return answer

solution(3)