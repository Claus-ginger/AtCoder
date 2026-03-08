import sys
input = sys.stdin.readline

N = int(input())

M = [[0] * 1502 for _ in range(1502)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    M[A][B] += 1
    M[A][D] -= 1
    M[C][B] -= 1
    M[C][D] += 1

for i in range(1501):
    for j in range(1, 1501):
        M[i][j] += M[i][j - 1]


for j in range(1501):
    for i in range(1, 1501):
        M[i][j] += M[i - 1][j]

ans = 0
for i in range(1500):
    for j in range(1500):
        if M[i][j] > 0:
            ans += 1

print(ans)
