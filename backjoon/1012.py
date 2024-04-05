import sys
sys.setrecursionlimit(10000)

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0<=nx<N and 0<=ny<M):
            if (cabbage[nx][ny] == 1):
                cabbage[nx][ny] = 0
                dfs(nx, ny)
    return

for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    cabbage = [[0 for i in range(M)] for j in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    for a in range(N):
        for b in range(M):
            if cabbage[a][b] == 1:
                dfs(a, b)
                cnt += 1
    print(cnt)









