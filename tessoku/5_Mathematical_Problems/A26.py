def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

Q = int(input())

for _ in range(Q):
    X = int(input())
    if isPrime(X):
        print("Yes")
    else:
        print("No")