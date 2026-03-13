import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
r = 0
total = 0

for l in range(N):
    while r < N and total + A[r] <= K:
        total += A[r]
        r += 1

    ans += r - l

    if l == r:
        r += 1
    else:
        total -= A[l]

print(ans)