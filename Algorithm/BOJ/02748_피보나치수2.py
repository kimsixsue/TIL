import sys
input = sys.stdin.readline
n = int(input())
f_n = [0, 1]
for _ in range(2, n + 1):
    f_n.append(f_n[_ - 1] + f_n[_ - 2])
print(f_n[n])