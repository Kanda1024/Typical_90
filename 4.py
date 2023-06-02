H,W = map(int, input().split())
A = []

for i in range(H):
    A.append(list(map(int, input().split())))

W_sum = []
H_sum = []

for i in range(H):
    W_sum.append(sum(A[i]))

for i in range(W):
    num = 0
    for j in range(H):
        num += A[j][i]
    H_sum.append(num)

for i in range(H):
    for j in range(W):
        print(W_sum[i] + H_sum[j] - A[i][j],end=" ")
    print()