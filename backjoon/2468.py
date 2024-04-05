# from collections import deque
#
# N = int(input())
# graph = []
# max_height = 0
#
# for i in range(N):
#     graph.append(list(map(int, input().split())))
#     max_height = max(max_height, max(graph[-1]))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y, max_height):
#     queue = deque()
#     queue.append((x, y))
#
#     while queue:
#         x, y = queue.popleft()
#         visited[x][y] = 1
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < N and 0<= ny < N and graph[x][y] > max_height and visited[nx][ny] == 0:
#                 queue.append((nx, ny))
#                 visited[nx][ny] = 1
#
# result = 0
# for i in range(1, max_height):
#     count = 0
#     visited = [[0] * N for _ in range(N)]
#     for j in range(N):
#         for k in range(N):
#             if graph[j][k] > i and visited[j][k] == 0:
#                 bfs(j, k, i)
#                 count += 1
#     result = max(result, count)
# print(result)

# dfs

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y, h):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] > h and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, h)


result = 0
for i in range(1, 101):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if (graph[j][k] > i and visited[j][k] == 0):
                visited[j][k] = 1
                dfs(j, k, i)
                count += 1
    result = max(result, count)
print(result)

