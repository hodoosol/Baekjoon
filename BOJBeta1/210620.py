# 10845 큐, 실버 4
import sys
queue = []
for i in range(int(input())) :
    order = sys.stdin.readline().strip()
    if 'push' in order :
        x = order.split(' ')[1]
        queue.append(x)
    elif order == 'pop' :
        if not queue :
            print(-1)
        else :
            print(queue[0])
            queue.pop(0)
    elif order == 'size' :
        print(len(queue))
    elif order == 'empty' :
        if not queue :
            print(1)
        else :
            print(0)
    elif order == 'front' :
        if not queue :
            print(-1)
        else :
            print(queue[0])
    elif order == 'back' :
        if not queue :
            print(-1)
        else :
            print(queue[-1])





# 10866 덱, 실버 4
import sys
deque = []
for i in range(int(input())) :
    order = sys.stdin.readline().strip()
    if 'push_front' in order :
        x = order.split(' ')[1]
        deque.insert(0, x)
    elif 'push_back' in order :
        x = order.split(' ')[1]
        deque.append(x)
    elif 'pop_front' in order :
        if not deque :
            print(-1)
        else :
            print(deque[0])
            deque.pop(0)
    elif 'pop_back' in order:
        if not deque:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif order == 'size' :
        print(len(deque))
    elif order == 'empty' :
        if not deque :
            print(1)
        else :
            print(0)
    elif order == 'front' :
        if not deque :
            print(-1)
        else :
            print(deque[0])
    elif order == 'back' :
        if not deque :
            print(-1)
        else :
            print(deque[-1])





# 1406 에디터, 실버 3 _ 시간 초과 _ 짜증 ~!
import sys
word = list(sys.stdin.readline().rstrip())
cursor = len(word)
for i in range(int(input())) :
    order = sys.stdin.readline().rstrip()
    if order == 'L' :
        if cursor == 0 :
            pass
        else :
            cursor -= 1
    elif order == 'D' :
        if cursor == len(word) :
            pass
        else :
            cursor += 1
    elif order == 'B' :
        if cursor == 0 :
            pass
        else :
            word.pop(cursor - 1)
            cursor -= 1
    elif 'P' in order :
        x = order.split(' ')[1]
        if cursor == 0 :
            word.insert(0, x)
        else :
            word.insert(cursor, x)
            cursor += 1

print(''.join(word))





# 1406 _ 두 개의 list를 이용하여 풀기 _ 와 진짜 힘들었다 시간 제한이 너무 타이트
# 리스트에서 insert와 del의 시간 복잡도는 O(n)이다.
# append와 pop은 O(1) !
import sys
word1 = list(sys.stdin.readline().strip())      # 왼쪽 리스트 _ 기본
word2 = []                                      # 오른쪽 리스트 _ 거꾸로

for i in range(int(input())) :
    order = sys.stdin.readline().strip()
    if word1 and order == 'L' :                 # 왼쪽 리스트가 비어있지 않고, L이라면
        word2.append(word1.pop())               # 오른쪽 리스트의 맨 오른쪽에 왼쪽 리스트의 맨 오른쪽 요소를 넣고 삭제
    elif word2 and order == 'D' :               # 오른쪽 리스트가 비어있지 않고, D라면
        word1.append(word2.pop())               # 왼쪽 리스트의 맨 오른쪽에 오른쪽 리스트의 맨 오른쪽 요소를 넣고 삭제
    elif word1 and order == 'B' :               # 왼쪽 리스트가 비어있지 않고, B라면
        word1.pop()                             # 왼쪽 리스트의 맨 오른쪽 요소 삭제
    elif 'P' in order :                         # P x 가 들어온다면
        word1.append(order[2])                  # 왼쪽 리스트의 맨 오른쪽에 x를 추가

print(''.join(word1 + list(reversed(word2))))   # 왼쪽 리스트와 거꾸로 뒤집은 오른쪽 리스트를 출력한다.
                                                # reversed(list)를 하면 <class 'list_reverseiterator'> 객체가 생성되므로
                                                # 다시 리스트로 바꾸어주어야 한다.




