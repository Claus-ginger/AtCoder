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
        while T and T[0] <= h:
            heapq.heappop(T)

    print(len(T))