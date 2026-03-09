import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
#print(A)

Q = int(input())
for _ in range(Q):
  X = int(input())
  print(bisect_left(A, X))
# ソート済み配列の中で位置を探す関数
