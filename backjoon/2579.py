N = int(input())
dp = []
w = [0] * (N+1)

for _ in range(N):
    dp.append(int(input()))

w[0] = dp[0]
if N > 1:
    w[1] = dp[0]+dp[1]

for i in range(2, N):
    w[i] = max(w[i-2]+dp[i], w[i-3]+dp[i-1]+dp[i])

print(w[N-1])

