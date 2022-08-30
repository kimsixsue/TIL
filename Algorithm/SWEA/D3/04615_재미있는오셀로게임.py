import sys

sys.stdin = open('./sample_input(1).txt')
dr = [0, 0, 1, -1, 1, -1, 1, -1]
dc = [-1, 1, 0, 0, 1, -1, -1, 1]
for testcase in range(1, int(input()) + 1):  # 테스트 케이스의 수
    N, M = map(int, input().split())  # N : 보드의 한 변의 길이 (4 or 6 or 8)
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1], board[N // 2 - 1][N // 2] = 2, 1
    board[N // 2][N // 2 - 1], board[N // 2][N // 2] = 1, 2
    for t in range(M):  # (row, col), color (1: black, 2: white)
        row, column, color = map(int, input().split())
        row -= 1
        column -= 1
        board[row][column] = color
        for way in range(8):  # 모든 방향
            cr, cc = row + dr[way], column + dc[way]
            # 돌이 존재하는 경우만 해당 way
            if (0 <= cr <= N - 1) and (0 <= cc <= N - 1) and board[cr][cc]:

                if board[cr][cc] == board[row][column]:
                    continue  # 색이 칸이 다를 때 해당 way
                between = 0  # 뒤집을 돌의 개수
                for _ in range(N):  # 가던 방향 추가 탐색

                    cr += dr[way]
                    cc += dc[way]
                    if cr < 0 or cr > N - 1 or cc < 0 or cc > N - 1 \
                            or board[cr][cc] == 0:
                        break  # 돌이 존재하는 경우만 pass
                    between += 1
                    if board[cr][cc] == color:  # 이번에 놓은 돌의 색과 동일
                        break  # 탐색 종료

                if (0 <= cr <= N - 1) and (0 <= cc <= N - 1) \
                        and board[cr][cc] and between:
                    cr, cc = row + dr[way], column + dc[way]  # 처음 만난 다른 색 돌
                    for _ in range(between):
                        board[cr][cc] = color
                        cr += dr[way]
                        cc += dc[way]

    black, white = 0, 0  # 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                black += 1
            if board[row][col] == 2:
                white += 1
    print(f'#{testcase}', black, white)
