from copy import deepcopy

# 3
# 2 2 2
# 4 4 4
# 8 8 8

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def move(board, dir):
    if dir == 0:#좌
        for i in range(n):
            pointer = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] = tmp * 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[i][pointer] = tmp
    if dir == 1:
        for i in range(n):
            pointer = n-1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] = tmp * 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp
    if dir == 2: # 상
        for j in range(n):
            pointer = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] = tmp * 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[pointer][j] = tmp
    if dir == 3:
        for j in range(n):
            pointer = n-1
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] = tmp * 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp
    return board

def dfs(board, count):
    global result
    if count == 5:
        for i in range(n):
            for j in range(n):
                result = max(result, board[i][j])
        return

    for i in range(4):
        move_board = move(deepcopy(board), i)
        dfs(move_board, count+1)

result = 0
dfs(graph, 0)
print(result)