# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
#
# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
#
# 예제 입력 1
# 4 6
# 101111
# 101010
# 101011
# 111011
# 예제 출력 1
# 15
# 예제 입력 2

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for i in range(N)]

queue = deque([(0,0)])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if (0<=next_x<N and 0<=next_y<M):
            if (graph[next_x][next_y] == 1):
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append((next_x, next_y))

print(graph[N-1][M-1])
