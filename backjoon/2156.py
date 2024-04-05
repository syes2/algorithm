n = int(input())
dp = []
w = [0] * (n+1)

for _ in range(n):
    dp.append(int(input()))

w[0] = dp[0]
if n > 1:
    w[1] = dp[0] + dp[1]
if n > 2:
    w[2] = max(w[1], dp[0]+dp[2], dp[1]+dp[2])

for i in range(3, n):
    w[i] = max(w[i-1], w[i-2]+dp[i], w[i-3]+dp[i-1]+dp[i])

print(w[n-1])