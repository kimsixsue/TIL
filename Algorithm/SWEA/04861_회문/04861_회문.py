import sys
sys.stdin = open('./sample_input.txt')


def return_p(matrix):
    para = ''  # 길이가 M인 회문 1개
    if M == N:  # 5 ≤ M ≤ N, 10 ≤ N ≤ 100
        for _ in range(N):
            if matrix[_] == matrix[_][::-1]:
                return matrix[_]
    else:
        for n in range(N):
            for m in range(M):
                if matrix[n][m: m + M] == matrix[n][m + M - 1: m - 1: -1]:
                    para = matrix[n][m: m + M]
                    break
    return para


TestCase = int(input())  # 테스트 케이스 개수 T
for T in range(1, TestCase + 1):
    N, M = list(map(int, input().split()))
    lines = [''] * N  # N개의 글자를 가진 N개의 줄
    for _ in range(N):
        lines[_] = input()     # 가로
    vertical_lines = [''] * N  # 세로
    for row in range(N):  # 행/열 바꿈
        for col in range(N):
            vertical_lines[row] += lines[col][row]

    print(f'#{T} {return_p(lines) + return_p(vertical_lines)}')