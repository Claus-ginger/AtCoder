M, D = map(int, input().split())
if (M == 1 and D == 7) or (M == 3 and D == 3) or (M == 5 and D == 5) or (M == 7 and D == 7) or (M == 9 and D == 9):
  print("Yes")
else:
  print("No")

# 解説
# gissekulist = [(1, 7), (3, 3), (5, 5), (7, 7), (9 9)]
# if ((m, d) in gossekulist):
#     print("Yes")
# else:
#     print("No")   