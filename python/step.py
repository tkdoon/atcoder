n = int(input())
a = list(map(int, input().split()))
hsum = 0
for i in range(n-1):
    if a[i] > a[i+1]:
        hsum += a[i]-a[i+1]
        a[i+1] = a[i]
print(hsum)
