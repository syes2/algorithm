s = input()
bomb = input()
bomb_len = len(bomb)

stack = []
for i in s:
    stack.append(i)
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')