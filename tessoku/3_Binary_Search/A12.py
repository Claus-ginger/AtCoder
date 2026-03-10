import sys
input = sys.stdin.readline

def check(A, K, x):
    return sum(x // a for a in A) >= K

N, K = map(int, input().split())
A = list(map(int, input().split()))

l, r = 1, 10**9

while l < r:
    m = (l + r) // 2
    if check(A, K, m):
        r = m
    else:
        l = m + 1

print(l)