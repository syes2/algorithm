N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def dfs(x, y, p_map, visited):
    visited[x][y] = 1
    p_map.append([x, y])
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and L <= abs(land[x][y] - land[nx][ny])<=R and visited[nx][ny] == 0:
            dfs(nx, ny, p_map, visited)
    return p_map

while True:
    p_maps = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                p_map = []
                p_maps.append(dfs(i, j, p_map, visited))
    if len(p_maps) == N*N:
        break
    for p_s in p_maps:
        sum = 0
        if len(p_s) > 1:
            for x,y in p_s:
                sum += land[x][y]
            new = sum//len(p_s)
            for x,y in p_s:
                land[x][y] = new
    cnt += 1

print(cnt)

