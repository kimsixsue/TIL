import sys
input = sys.stdin.readline

N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

for r in range(1, N + 1):
    if r == 1:  # 첫째 줄은 공백 + 별
        print(''.join(' ' * (N - r) + '*'))
    elif r == N:  # 마지막 줄은 별만
        print('*' * (2 * N - 1))
    else:  # 공백 감소 + 별 + 공백 증가 + 별
        print(''.join(' ' * (N - r) + '*' + ' ' * (2 * r - 3) + '*'))
