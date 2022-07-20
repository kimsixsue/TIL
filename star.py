N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))
for i in range(N + 1, 2 * N):
    print(' ' * (i - N) + '*' * (4 * N - 2 * i - 1))
