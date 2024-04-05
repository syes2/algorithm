# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

from collections import deque
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0,0,1,-1],[1, -1, 0, 0]
result = 0

def bfs():
    queue = deque()

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                queue.append((i, j))

    temp =[g[:] for g in lab]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and temp[nx][ny]==0:
                temp[nx][ny] = 2
                queue.append((nx, ny))

    count = 0
    global result
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    result = max(result, count)


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(count+1)
                lab[i][j] = 0

make_wall(0)
print(result)