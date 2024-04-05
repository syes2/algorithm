N = int(input())
M = int(input())
if M:
    button = set(input().split())
else:
    button = []
ans = abs(100 - N)

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000000):
    for N in str(num):
        if N in button: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - N))

print(ans)


# N = int(input())
# M = int(input())
# if M > 0:
#     button = input().split()
# minus, plus = N, N
# temp = 0
#
# if (M != 0):
#     while 1:
#         minus -= 1
#         if (minus < 0):
#             minus = 0
#         plus += 1
#         for j in str(minus):
#             if (j not in button):
#                 temp = minus
#                 if (minus == N -1):
#                     temp = N
#             else:
#                 temp = 0
#                 break
#         if (temp != 0):
#             break
#         for j in str(plus):
#             if (j not in button):
#                 temp = plus
#             else:
#                 temp = 0
#                 break
#         if (temp != 0):
#             break
# else:
#     temp = N
#
# print(temp)
#
# if(abs(N-100) < abs(N - temp)+len(str(temp)) or M == 10):
#     print(abs(N-100))
# else:
#     print(abs(N-temp)+len(str(temp)))

