import sys
from bisect import bisect_left
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

Af = A[:N//2]
Ab = A[N//2:]
P = []
Q = []
#print("Af:", Af)
#print("Ab:", Ab)
for i in range(1 << len(Af)):
    total = 0
    for j in range(len(Af)):
        if i & (1 << j):
            total += Af[j]
    P.append(total)

for i in range(1 << len(Ab)):
    total = 0
    for j in range(len(Ab)):
        if i & (1 << j):
            total += Ab[j]
    Q.append(total)
#print("P:", P)
#print("Q:", Q)
#P.sort() いらない
Q.sort()


for p in P:
    X = K - p
    pos = bisect_left(Q, X)
    if pos < len(Q) and Q[pos] == X:
        print("Yes")
        sys.exit(0)
print("No")