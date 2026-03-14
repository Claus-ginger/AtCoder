import sys
input = sys.stdin.readline

H, W, Q = map(int, input().split())


for i in range(Q):
  q, n = map(int, input().split())
  if q == 1:
    H -= n
    print(W * n)
  else:
    W -= n
    print(H*n)