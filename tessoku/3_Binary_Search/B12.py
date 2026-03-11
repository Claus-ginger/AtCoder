import sys
input = sys.stdin.readline

def check(n, x):
    return n >= x**3 + x 

N = int(input())

l, r = 0.0, 100.0

while l < r:
    m = (l + r) / 2
    if abs(N - m**3 - m) < 0.001:
        break
    if check(N, m):
        l = m
    else:
        r = m

print(l)

"""
解答例 

def f(x):
	return x**3 + x

N = int(input())

# 二分探索
L = 0.0
R = 100.0
for i in range(20): -> 100/(2**20) < 0.001だから
	M = (L + R) / 2
	val = f(M)

	# 探索範囲を絞る
	if val > N:
		R = M # 左半分に絞られる
	else:
		L = M # 右半分に絞られる

# 出力
print(M)
"""