import sys
input = sys.stdin.readline

def bubunretsu(S, T):
    i = 0
    j = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            j += 1
        i += 1
    return j == len(T)
    
S = input().strip()
T = input().strip()

L = len(S)
count = 0
for i in range(L):
  for j in range(L):
    l = i
    r = L-j
    if l < r:
      W = S[l:r]
      #print(W)
      if bubunretsu(W, T):
        #print("hit")
        continue
      else:
        count += 1

print(count)