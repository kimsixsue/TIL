import sys
input = sys.stdin.readline

N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

for _ in range(1, N + 1):
    if _ % 2:  # 홀수 line
        print(''.join('* ' * N).rstrip())
    else:  # 짝수 line
        print(''.join(' *' * N))
