import sys
input = sys.stdin.readline

N, M = map(int, input().split())
C = list(map(int, input().split()))

P = [0]* M
for i in range(N):
  A, B = map(int, input().split())
  P[A-1] += B

ans = 0
for i in range(M):
  if C[i] >= P[i]:
    ans += P[i]
  else:
    ans += C[i]

print(ans)
