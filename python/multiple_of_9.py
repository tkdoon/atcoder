n = list(input())
# n = map(int, n)
sum = 0
for i in range(len(n)):
    n[i] = int(n[i])
    sum += n[i]
# print(n)
if sum % 9 == 0:
    print('Yes')
else:
    print('No')
