n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
count = 0

for i in range(n):
    if x[i][0]**2+x[i][1]**2 <= d**2:
        count += 1

print(count)
