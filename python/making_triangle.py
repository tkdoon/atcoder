n = int(input())
l = list(map(int, input().split()))
count = 0


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if l[i] != l[j] and l[i] != l[k] and l[j] != l[k] and abs(l[i]-l[j]) < l[k] < l[i]+l[j]:
                count = count + 1

print(count)
