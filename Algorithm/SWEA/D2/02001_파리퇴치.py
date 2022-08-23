T = int(input())  # 테스트 케이스의 개수
for testcase in range(1, T + 1):
    N, M = map(int, input().split())  # 5 <= N <= 15 # 2 <= M <= N
    domain = [[0] * (N + 1) for _ in range(N + 1)]
    for row in range(1, N + 1):  # N 줄에 걸쳐 N x N 배열이 주어진다.
        domain[row][1:] = list(map(int, input().split()))
    max_count = 0
    if N == M:
        for row in domain:
            for col in row:
                max_count += col
    else:  # N x N 배열 안에서 M x M 파리채로 최대한 많은 파리를 죽이고자 한다.
        for row in range(1, N - M + 2):
            for col in range(1, N - M + 2):
                count = 0
                for r in range(row, row + M):
                    for c in range(col, col + M):
                        count += domain[r][c]
                if max_count < count:
                    max_count = count
    print(f'#{testcase} {max_count}')
