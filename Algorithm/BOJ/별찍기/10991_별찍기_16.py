import sys
input = sys.stdin.readline

N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 공백을 N - r개, ' *'를 r - 1개 출력한다.
for r in range(1, N + 1):
    print(''.join(' ' * (N - r) + '*' + ' *' * (r - 1)))
