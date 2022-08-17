import sys
input = sys.stdin.readline
N = int(input())  # 돌 1 ≤ N ≤ 1000 개
# 게임은 상근이가 먼저 시작한다.
if (N % 2) or (N == 2):
    print('SK')
else:
    print('CY')
# 마지막 돌을 가져가는 사람이 게임을 이기게 된다.
