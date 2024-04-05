N = int(input())
tree = [list(input()) for _ in range(N)]

result = ""

def quad(x, y, n):
    global result
    num = tree[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != tree[i][j]:
                result += '('
                quad(x, y, n // 2)
                quad(x, y + n // 2, n // 2)
                quad(x + n // 2, y, n // 2)
                quad(x + n // 2, y + n // 2, n // 2)
                result += ')'
                return
    if num == '0':
        result += '0'
    else:
        result += '1'

quad(0, 0, N)
print(result)
