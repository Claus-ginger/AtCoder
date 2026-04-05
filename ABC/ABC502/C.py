import sys
input = sys.stdin.readline

N = int(input())
A = [None] * N
B = [None] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

M = int(input())
S = [input().strip() for _ in range(M)]

L = [[set() for _ in range(11)] for _ in range(11)]

for s in S:
    l = len(s)
    for t in range(1, l + 1):
        L[l][t].add(s[t - 1])

for s in S:
    if len(s) != N:
        print("No")
        continue

    flag = True
    for i in range(N):
        if s[i] not in L[A[i]][B[i]]:
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")