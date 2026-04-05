# LIS ... 最長増加部分列(Longest Increasing Subsequence)

import sys
import bisect
input = sys.stdin.readline

def Get_LISvalue(A):
    LEN = 0
    L = []
    for i in range(N):
        pos = bisect.bisect_left(L, A[i])
        if pos == LEN:
            L.append(A[i])
            LEN += 1
        else:
            L[pos] = A[i]
    return LEN

N = int(input())
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

tmp = []
for i in range(N):
    tmp.append([X[i], -Y[i]])
    # -Yとする理由
    # 昇順に並べると，Xが同じとき両方とってしまう．これはよくないので降順
tmp.sort()

A = []
for i in range(N):
    A.append(-tmp[i][1])

print(Get_LISvalue(A))