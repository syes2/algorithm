import heapq
n = int(input())
list = [list(map(int, input().split())) for _ in range(n)]

list.sort(key = lambda x: (x[1]))
result = []

for l in list:
    heapq.heappush(result, l[0])
    if len(result) > l[1]:
        heapq.heappop(result)

print(sum(result))