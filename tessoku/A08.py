import sys
input = sys.stdin.readline

H, W = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(H)]
#print(X)

Z = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(H):
  for j in range(W):
    Z[i+1][j+1] = Z[i+1][j] + Z[i][j+1] -Z[i][j] + X[i][j]

#print(Z)

Q = int(input())
for _ in range(Q):
  A, B, C, D = map(int, input().split())
  print(Z[C][D] - Z[A-1][D]- Z[C][B-1] + Z[A-1][B-1])
  
