N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))


for i in range(0, Q):
    if A[L[i]-1] == N:
        print(i, 'u')
        continue
    elif A[L[i+1]-1] == A[L[i]-1]+1:
        continue
    else:
        print(i)
        A[L[i]-1] = A[L[i]-1]+1
print(A)
