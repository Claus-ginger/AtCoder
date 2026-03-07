import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
A = list(map(int, input().split()))
sorted_A = sorted(range(N), key=lambda i: A[i])

for _ in range(Q):
    K = int(input())
    B = set(map(int, input().split()))
    for i in sorted_A:
        if (i + 1) not in B:
            print(A[i])
            break
