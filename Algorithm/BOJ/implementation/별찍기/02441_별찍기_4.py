N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
for i in range(0, N+1):
    print(" " * i + "*" * (N-i))
# 첫째줄에 *이 N개 나와야하며,
# N 번째줄에 공백이 N-1개 나와야함
