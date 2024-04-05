N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1, 0, -1):
    for j in range(i):
        dp[i-1][j] = max(dp[i-1][j] + dp[i][j], dp[i-1][j] + dp[i][j+1])

print(dp[0][0])