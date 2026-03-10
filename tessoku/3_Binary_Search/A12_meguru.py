import sys
input = sys.stdin.readline

def ok(x):
    return sum(x // a for a in A) >= K

N, K = map(int, input().split())
A = list(map(int, input().split()))

ng = 0
okv = 10**9

while abs(okv - ng) > 1:
    mid = (okv + ng) // 2
    if ok(mid):
        okv = mid
    else:
        ng = mid

print(okv)