import sys
from bisect import bisect_left

input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

print(bisect_left(A, X) + 1)
