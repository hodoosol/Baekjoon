# 10845 큐, 실버 4
# import sys
# queue = []
# for i in range(int(input())) :
#     order = sys.stdin.readline().strip()
#     if 'push' in order :
#         x = order.split(' ')[1]
#         queue.append(x)
#     elif order == 'pop' :
#         if not queue :
#             print(-1)
#         else :
#             print(queue[0])
#             queue.pop(0)
#     elif order == 'size' :
#         print(len(queue))
#     elif order == 'empty' :
#         if not queue :
#             print(1)
#         else :
#             print(0)
#     elif order == 'front' :
#         if not queue :
#             print(-1)
#         else :
#             print(queue[0])
#     elif order == 'back' :
#         if not queue :
#             print(-1)
#         else :
#             print(queue[-1])





# 10866 덱, 실버 4
# import sys
# deque = []
# for i in range(int(input())) :
#     order = sys.stdin.readline().strip()
#     if 'push_front' in order :
#         x = order.split(' ')[1]
#         deque.insert(0, x)
#     elif 'push_back' in order :
#         x = order.split(' ')[1]
#         deque.append(x)
#     elif 'pop_front' in order :
#         if not deque :
#             print(-1)
#         else :
#             print(deque[0])
#             deque.pop(0)
#     elif 'pop_back' in order:
#         if not deque:
#             print(-1)
#         else:
#             print(deque[-1])
#             deque.pop()
#     elif order == 'size' :
#         print(len(deque))
#     elif order == 'empty' :
#         if not deque :
#             print(1)
#         else :
#             print(0)
#     elif order == 'front' :
#         if not deque :
#             print(-1)
#         else :
#             print(deque[0])
#     elif order == 'back' :
#         if not deque :
#             print(-1)
#         else :
#             print(deque[-1])





# 1406 에디터, 실버 3
import sys
word = list(input())
cursor = len(word)
for i in range(int(input())) :
    order = sys.stdin.readline().strip()
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
    elif 'P' in order :
        x = order.split(' ')[1]
        if cursor == 0 :
            word.insert(0, x)
        else :
            word.insert(cursor, x)
            cursor += 1
word = str(word)
print(word)

