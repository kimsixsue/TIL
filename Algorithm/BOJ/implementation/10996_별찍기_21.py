import sys
input = sys.stdin.readline

N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
repeat = ['*', ' '] * 51
if N == 1:
    print('*')
else:  # 별 공백 \n 공백 별 반복
    for _ in range(N):
        print(''.join(repeat[:N]))
        print(''.join(repeat[1:N + 1]))
