import bisect

N = int(input())
A = list(map(int, input().split()))

LEN = 0
L = []

for i in range(N):
    pos = bisect.bisect_left(L, A[i])
    if pos >= LEN:
        L.append(A[i])
        LEN += 1
    else:
        L[pos] = A[i]

print(LEN)