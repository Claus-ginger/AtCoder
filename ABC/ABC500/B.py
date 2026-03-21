import sys
input = sys.stdin.readline

N = int(input())
C = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N):
  r = list(map(int, input().split()))
  for j in range(i+1, N+1):
    C[i][j] = r[j-i-1]

for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(b + 1, N + 1):
            if C[a][c] > C[a][b] + C[b][c]:
                print("Yes")
                exit()

print("No")