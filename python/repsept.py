k = int(input())
check = 0
a = 7 % k
for i in range(k):
    if a == 0:
        print(i+1)
        check += 1
        break
    else:
        a = (10*a+7) % k
if check == 0:
    print(-1)
