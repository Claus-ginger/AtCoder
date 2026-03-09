import sys
input = sys.stdin.readline

def search(A, x, N):
    L = 0
    R = N-1
    while L <= R:
        M = (L + R) // 2
        if x < A[M]:R = M - 1
        elif x == A[M]:return M
        else:L = M + 1
    return -1

def main():
  N, X = map(int, input().split())
  A = list(map(int, input().split()))
  ans = search(A, X, N)
  print(ans+1)
  
if __name__ == "__main__":
    main()
