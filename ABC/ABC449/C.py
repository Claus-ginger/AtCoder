import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
S = input().strip()

cnt = {}
ans = 0

for i in range(N):
    l = i - R
    r = i - L

    if l - 1 >= 0:
        ch = S[l - 1]
        cnt[ch] -= 1
        if cnt[ch] == 0:
            del cnt[ch]

    if r >= 0:
        ch = S[r]
        if ch in cnt:
            cnt[ch] += 1
        else:
            cnt[ch] = 1

    if S[i] in cnt:
        ans += cnt[S[i]]

print(ans)