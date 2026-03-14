import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

T = sorted(set(A))

# T = set(A)
# T.sort()はエラー．setオブジェクトはsortできない．

B = [None]*N
for i in range(N):
    B[i] = bisect_left(T, A[i]) + 1

print(*B)