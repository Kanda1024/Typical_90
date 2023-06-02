import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())

for i in range(Q):
    b = int(input())
    pos = bisect.bisect(A, b)
    if pos-1 < 0:
        print(abs(b-A[pos]))
    elif pos == N:
        print(abs(b-A[pos-1]))
    else:
        print(min(abs(b - A[pos]), abs(b - A[pos-1])))