import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
P = [0]*N
P[0] = A[0]
for i in range(1, N):
  P[i] = max(P[i-1], A[i])
Q = [0]*N
Q[-1] = A[-1]
for i in range(N-2, 0, -1):
  Q[i] = max(Q[i+1], A[i])

#print(P)
#print(Q)
D = int(input())
for i in range(D):
  L, R = map(int, input().split())
  #print("P[L-2]:", P[L-2])
  #print("Q[R]:", Q[R])
  print(max(P[L-2], Q[R]))

# 右累積和と左累積和を使用．
# スライスでリストを作ってmax探索する手法はTLE
