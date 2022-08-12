N = int(input())
A = [list(map(int, input())) for i in range(N)]


l = []


for i in range(N):
    for j in range(N):
        sum_1 = str(A[i][j])
        sum_2 = str(A[i][j])
        sum_3 = str(A[i][j])
        sum_4 = str(A[i][j])
        sum_5 = str(A[i][j])
        sum_6 = str(A[i][j])
        sum_7 = str(A[i][j])
        sum_8 = str(A[i][j])
        for s in range(1, N):
            sum_1 += str(A[i % N][(j+s) % N])
            sum_2 += str(A[i % N][(j-s) % N])
            sum_3 += str(A[(i+s) % N][(j+s) % N])
            sum_4 += str(A[(i+s) % N][(j-s) % N])
            sum_5 += str(A[(i-s) % N][(j+s) % N])
            sum_6 += str(A[(i+s) % N][j % N])
            sum_7 += str(A[(i-s) % N][j % N])
            sum_8 += str(A[(i-s) % N][(j-s) % N])
        sum_1 = int(sum_1)
        sum_2 = int(sum_2)
        sum_3 = int(sum_3)
        sum_4 = int(sum_4)
        sum_5 = int(sum_5)
        sum_6 = int(sum_6)
        sum_7 = int(sum_7)
        sum_8 = int(sum_8)
        l.append(max(sum_1, sum_2, sum_3, sum_4,
                     sum_5, sum_6, sum_7, sum_8))
print(max(l))
