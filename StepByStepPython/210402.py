# 1011 Fly me to the Alpha Centauri _ 실패 ... 다음에 다시 풀어보자.





# 1929 _ 에라토스테네스의 체 이용
# m, n = map(int, input().split())
#
# def prime_sieve(m, n) :
#     n += 1
#     sieve = [True] * n
#     for i in range(2, int(n ** 0.5) + 1) :
#         if sieve[i] :
#             for j in range(2 * i, n, i) :
#                 sieve[j] = False
#     for i in range(m, n) :
#         if i > 1 :
#             if sieve[i] :
#                 print(i)
#
# prime_sieve(m, n)





# 4948
# n = (2 * 123456) + 1
# sieve = [True] * n
# for i in range(2, int(n ** 0.5) + 1) :
#     if sieve[i] :
#         for j in range(2 * i, n, i) :
#             sieve[j] = False
#
# while True :
#     m = int(input())
#     if m == 0 :
#         break
#     res = 0
#     for i in range(m + 1, (m * 2) + 1) :
#         if i > 1 :
#             if sieve[i] :
#                 res += 1
#     print(res)





# 2420
# a, b = map(int, input().split())
# print(abs(a- b))




