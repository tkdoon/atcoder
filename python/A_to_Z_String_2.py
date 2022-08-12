N, X = map(int, input().split())
if X % N == 0:
    y = X//N-1
else:
    y = X//N
print(chr(65+y))
