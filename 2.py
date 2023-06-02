N = int(input())

ans = []

#bit全探索(2^N)
for bit in range(2**N):
    res = ""
    tmp = 0

    #0~Nbitシフトで1桁ずつ変換
    for i in range(N):
        if (bit >> i) & 1 == 1:
            res += "("
            tmp += 1
        else:
            res += ")"
            tmp -= 1
        if tmp < 0:
            break
    if tmp == 0:
        ans.append(res)

ans.sort()

for i in ans:
    print(i)