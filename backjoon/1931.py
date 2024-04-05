# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

n = int(input())
sche = [list(map(int, input().split())) for _ in range(n)]

sche.sort(key = lambda x : (x[1],x[0]))
count = 0

end = sche[0][1]

for i in range(1, n):
    if end <= sche[i][0]:
        end = sche[i][1]
        count += 1

print(count+1)