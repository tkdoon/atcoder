n = int(input())
a = list(map(int, input().split()))


# def amari(num):
#     return num % (10**9+7)


# a = list(map(amari, a))

sum = 0
for i in range(n):
    for j in range(i+1, n):
        sum += a[i]*a[j] % (10**9+7)
print(sum % (10**9+7))
