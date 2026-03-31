import sys
import heapq
input = sys.stdin.readline

Q = int(input())
T = []

for _ in range(Q):
    n, h = map(int, input().split())

    if n == 1:
        heapq.heappush(T, h)
    else:
        while T and T[0] <= h: # T を入れている理由：Tが空だとT[0]が存在しないのでIndexErrorになる．andで評価して，Falseなら右は評価しない
            heapq.heappop(T)

    print(len(T))