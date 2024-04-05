n = int(input())
m = int(input())

graph = [[0] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)
cnt = 0

def dfs(x):
    global cnt
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)
            cnt+= 1

dfs(1)
print(cnt-1)