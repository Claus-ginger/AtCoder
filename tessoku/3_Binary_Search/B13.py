import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(N+1)
for i in range(0, N):
    S[i+1] = S[i] + A[i]

R = [0]*N
#print(R)

for i in range(N):
    if i == 0: R[i] = -1
    else: R[i] = R[i - 1]

    while R[i] < N-1 and S[(R[i]+1)+1] - S[i] <= K:
        R[i] += 1
    
ans = 0
for i in range(0, N):
    ans += R[i] - i + 1

print(ans)