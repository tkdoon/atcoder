h, w, k = map(int, input().split())
c = [list(map(int, input().split())) for i in range(h)]
blackCount = 0
count = 0
for i in range(h):
    for j in range(w):
        if c[i, j] == '#':
            blackCount += 1
if blackCount == k:
    count += 1
