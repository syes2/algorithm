w = list(map(int, input().split()))
d = [1, 1, 1]
count = 1

while(w != d):
    d[0] += 1
    d[1] += 1
    d[2] += 1
    if(d[0] > 15):
        d[0] = 1
    if(d[1] > 28):
        d[1] = 1
    if(d[2] > 19):
        d[2] = 1
    count+=1

print(count)

