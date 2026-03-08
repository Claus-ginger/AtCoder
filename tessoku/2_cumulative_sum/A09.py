import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())

coord = [list(map(int, input().split())) for _ in range(N)]
#print(coord)

M = [[0] * (W+2) for _ in range(H+2)]
for i in range(N):
  A = coord[i][0]
  B = coord[i][1]
  C = coord[i][2]
  D = coord[i][3]
  
  M[A][B] += 1
  M[A][D+1] -= 1
  M[C+1][B] -= 1
  M[C+1][D+1] += 1

Z = [[0] * (W+2) for _ in range(H+2)]

for i in range(1, H+1):
  for j in range(1, W+1):
    Z[i][j] = Z[i][j-1] + M[i][j]

for i in range(1, H+1):
  for j in range(1, W+1):
    Z[i][j] = Z[i-1][j] + Z[i][j]


#print(Z)
for i in range(1, H+1):
  print(*Z[i][1:W+1])
