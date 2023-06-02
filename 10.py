N = int(input())
P = []
P2 = []

sum = 0
sum2 = 0

for i in range(N):
    c,p = map(int, input().split())
    if c == 1:
        sum += p
    else:
        sum2 += p
    P.append(sum)
    P2.append(sum2)

Q = int(input())

L = []
R = []

for i in range(Q):
    l,r = map(int, input().split())
    L.append(l)
    R.append(r)

    if l-2 < 0:
        print(P[r-1], P2[r-1])
    else:
        print(P[r-1]-P[l-2], P2[r-1]-P2[l-2])