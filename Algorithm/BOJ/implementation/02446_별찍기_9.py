# N-1 줄만큼 빈칸이 증가 별이 감소합니다
# N 줄만큼 빈칸이 감소 별이 증가합니다

N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
for _ in range(N - 1):
    print(' ' * _ + '*' * (2 * (N - _) - 1))
for _ in range(N - 1, -1, -1):
    print(' ' * _ + '*' * (2 * (N - _) - 1))

# N = int(input())
# for i in range(1, N):
#     for j in range(i - 1):
#         print(' ', end='')
#     for k in range(2 * (N - i) + 1):
#         print('*', end='')
#     print()
# for i in range(1, N + 1):
#     for j in range(N - i):
#         print(' ', end='')
#     for k in range(i * 2 - 1):
#         print('*', end='')
#     print()
