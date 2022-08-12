n = int(input())
d = [list(map(int, input().split())) for i in range(n)]
ok = False
for i in range(n-2):
    if d[i][1] == d[i][0]:
        if d[i+1][1] == d[i+1][0]:
            if d[i+2][1] == d[i+2][0]:
                ok = True
if ok == True:
    print("Yes")
else:
    print("No")
