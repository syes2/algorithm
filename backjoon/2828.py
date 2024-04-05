n, m = map(int, input().split())
j = int(input())

baguni = 1 # 바구니 위치
m_count = 0 # 이동 횟수

for i in range(j):
    move = 0
    apple = int(input())
    if (apple > baguni + m-1):
        move += apple - (baguni+m-1)
        baguni += move
        m_count += move
    elif (apple < baguni):
        move += baguni - apple
        baguni -= move
        m_count += move
print(m_count)

