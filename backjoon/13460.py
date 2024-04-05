from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

visited = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == "R":
                rx, ry = x, y
            if board[x][y] == "B":
                bx, by = x, y
    return rx, ry, bx, by

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    queue = deque()
    rx, ry, bx, by = init()
    queue.append((rx, ry, bx, by, 1))
    visited.append((rx, ry, bx, by))
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(depth)
                return
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth + 1))
    print(-1)

bfs()