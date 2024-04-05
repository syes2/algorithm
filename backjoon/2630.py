N = int(input())
tree = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0]

def quad(x, y, n):
    color = tree[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]:
                quad(x, y, n // 2)
                quad(x, y + n // 2, n // 2)
                quad(x + n // 2, y, n // 2)
                quad(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

quad(0, 0, N)
print(result[0])
print(result[1])