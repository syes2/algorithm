N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
# dp[y][x][dir] dir - 가로(0), 세로(1), 대각선(2)

# 초기 값 설정
dp[0][1][0] = 1

for x in range(2, N):
    if house[0][x] == 0:
        dp[0][x][0] = dp[0][x-1][0]

for y in range(1, N):
    for x in range(2, N):
        if house[y][x] == 0 and house[y-1][x] == 0 and house[y][x-1] == 0:
            dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] +dp[y-1][x-1][2]
        if house[y][x] == 0:
            dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]
            dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]

print(sum(dp[N-1][N-1]))