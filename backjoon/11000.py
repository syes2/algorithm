# 3
# 1 3
# 2 4
# 3 5

import heapq

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
max_room = 0
result = []
schedule.sort(key = lambda x: (x[0], x[1]))

heapq.heappush(result, schedule[0][1])

for i in range(1, n):
    if result[0] <= schedule[i][0]:
        heapq.heappop(result)
    heapq.heappush(result, schedule[i][1])
    max_room = max(max_room, len(result))

print(max_room)



