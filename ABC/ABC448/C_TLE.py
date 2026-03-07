import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
  K = int(input())
  B = list(map(int, input().split()))
  result = [A[i-1] for i in range(1, N+1) if i not in B]
  print(min(result))

#  > 2000 ms 全探索では実行時間超過を起こす
