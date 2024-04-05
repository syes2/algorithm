v = int(input())
e = int(input())
g = [[] for _ in range(v+1)]
visited = [0] * (v+1)

for i in range(e):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


count = 0

def dfs(i):
    global count
    visited[i] = 1
    count += 1
    for i in g[i]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(count)

