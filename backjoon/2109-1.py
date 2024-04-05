import heapq

n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]
temp = []

lecture.sort(key = lambda x: (x[1]))

for p, d in lecture:
    heapq.heappush(temp, p)
    if len(temp) > d:
        heapq.heappop(temp)

print(sum(temp))
