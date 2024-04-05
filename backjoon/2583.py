# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2

from collections import deque

N, M, K = map(int, input().split())
areas = []
check = [[0] * M for _ in range(N)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            check[j][k] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global area
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0<=nx<N and 0<=ny<M and visited[nx][ny] == 0 and check[nx][ny] == 0):
                area += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

count = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        area = 0
        if (check[i][j] == 0 and visited[i][j] == 0):
            bfs(i, j)
            count += 1
            areas.append(area+1)

print(count)
areas.sort()
print(" ".join(map(str, areas)))
