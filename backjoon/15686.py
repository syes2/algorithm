from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
result = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        if city[i][j] == 2:
            chicken.append([i, j])

for chick in combinations(chicken, M):
    min_sum = 0
    for h in home:
        min_d = float('inf')
        for c in chick:
            min_d = min(min_d, abs(c[0] - h[0]) + abs(c[1] - h[1]))
        min_sum += min_d
    result.append(min_sum)


print(min(result))