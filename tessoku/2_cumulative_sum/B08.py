import sys
input = sys.stdin.readline

N = int(input())

coord = [list(map(int, input().split())) for _ in range(N)]
#print(coord)

M = [[0] * 1502 for _ in range(1502)]
Z = [[0] * 1502 for _ in range(1502)]
for i in range(N):
  M[coord[i][0]+1][coord[i][1]+1] += 1

for i in range(1501):
  for j in range(1501):
    Z[i+1][j+1] = Z[i+1][j] + Z[i][j+1] -Z[i][j] + M[i+1][j+1]

#print(Z)

Q = int(input())
for _ in range(Q):
  a, b, c, d = map(int, input().split())
  print(Z[c+1][d+1] - Z[a][d+1]- Z[c+1][b] + Z[a][b])
  
