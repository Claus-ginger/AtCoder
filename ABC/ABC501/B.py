import sys
input = sys.stdin.readline

N, M = map(int, input().split())

diff = [0] * M
for _ in range(N):
    A, B = map(int, input().split())
    diff[A - 1] -= 1
    diff[B - 1] += 1

for i in diff:
    print(i)