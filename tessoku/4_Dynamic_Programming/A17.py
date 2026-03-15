import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None]*N
dp[0] = 0
dp[1] = A[0]
for i in range(2, N):
    dp[i] = min(dp[i-1]+A[i-1], dp[i-2]+B[i-2])
#print(dp[N-1])

# 答えの復元
ans = []
Place = N-1
while True:
    ans.append(Place+1)
    if Place == 0:
        break

    if dp[Place-1] + A[Place-1] == dp[Place]:
        Place = Place - 1
    else:
        Place = Place - 2
ans.reverse()

ans2 = [str(i) for i in ans]
print(len(ans))
print(*ans2)