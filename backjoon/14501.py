n = int(input())
sche = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n):
    for j in range(i+sche[i][0], n+1):
        if dp[j] < dp[i] + sche[i][1]:
            dp[j] = dp[i] + sche[i][1]

print(dp[-1])