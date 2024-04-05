from collections import deque

N, M = map(int, input().split())
island = [list(input()) for _ in range(N)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(x, y):
    visited = [[-1]*M for _ in range(N)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0
    max_distance = 0  # 각 시작점에서의 최대 거리를 저장

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and island[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                max_distance = visited[nx][ny]  # 최대 거리 업데이트

    return max_distance

result = 0
for x in range(N):
    for y in range(M):
        if island[x][y] == 'L':
            result = max(result, bfs(x, y))  # 모든 'L'에서의 최대 거리 중 최대값을 찾음

print(result)




