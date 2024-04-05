# 8
# 11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011

n = int(input())
graph = [list(input()) for _ in range(n)]

def quadtree(x, y, n):
    num = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != graph[i][j]:
                print('(', end="")
                quadtree(x, y, n//2)
                quadtree(x, y+ n//2, n // 2)
                quadtree(x+n//2, y, n // 2)
                quadtree(x+n//2, y+n//2, n // 2)
                print(')', end="")
                return
    if num == '0':
        print('0', end="")
    else:
        print('1', end="")

quadtree(0, 0, n)