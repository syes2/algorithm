
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
tree = [list(input()) for i in range(n)]

def quadtree(x, y, n):
    num = tree[x][y]  # 해당 영역의 첫번째 수를 뽑는다.
    for i in range(x, x+n):
        for j in range(y, y+n):
            if (num != tree[i][j]):
                print('(', end="")
                quadtree(x, y ,n//2)
                quadtree(x, y+n//2, n // 2)
                quadtree(x + n//2, y, n//2)
                quadtree(x + n // 2, y+n//2, n // 2)
                print(')',end="")
    if num == '0':
        print('0',end="")
    else:
        print('1',end="")

quadtree(0, 0, n)

