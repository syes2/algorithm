N = int(input())
dp = list(map(int, input().split()))
sum = dp

for i in range(N-1):
    sum[i] = max(sum[i] + dp[i+1], dp[i+1])

print(max(sum))
