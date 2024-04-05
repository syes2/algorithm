from collections import deque

N, M = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for a, b in edge:
    graph[a].append(b)
    indegree[b] += 1

queue = deque([i for i in range(1, N+1) if indegree[i] == 0])
result = []

while queue:
    node = queue.popleft()
    result.append(node)
    for next in graph[node]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

for i in result:
    print(i, end=" ")




