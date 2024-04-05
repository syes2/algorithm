N = int(input())
W = [[] for _ in range(N)]
dp = [[0 for _ in range(1 << N - 1)] for _ in range(N)]

for i in range(N):
    W[i] = list(map(int, input().split()))

def solution(i, route):
    global N, W, dp

    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (N - 1)) - 1:
        if not W[i][0]:
            return float('inf')
        else:
            return W[i][0]

    min_price = float('inf')
    for j in range(1, N):
        if not W[i][j] or route & (1 << j - 1):
            continue
        print("i,j = ", i,j , "sol(",j,",",route | (1<<(j-1)),")")
        print(route,(1<<(j-1)) )
        dist = W[i][j] + solution(j, route | (1 << (j - 1)))
        if min_price > dist:
            min_price = dist
    dp[i][route] = min_price
    return min_price

print(solution(0, 0))