import sys
import bisect
input = sys.stdin.readline

N = int(input())
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

LEN = 0
L = []
dp = [None] * N

for i in range(N):
    W = bisect.bisect_left(L, X[i])
    H = bisect.bisect_left(L, Y[i])