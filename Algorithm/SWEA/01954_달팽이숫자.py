for testcase in range(1, int(input()) + 1):  # 테스트 케이스의 개수
    N = int(input())  # 1 ≤ 달팽이의 크기 ≤ 10
    print(f'#{testcase}')
    snail = list([0] * N for _ in range(N))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    row, col, direction = 0, 0, 0
    for number in range(1, N**2 + 1):
        snail[row][col] = number
        row += dr[direction]
        col += dc[direction]
        if (row < 0) or (col < 0) or (row >= N) or (col >= N) or snail[row][col] != 0:
            row -= dr[direction]
            col -= dc[direction]
            direction = (direction + 1) % 4
            row += dr[direction]
            col += dc[direction]
    for row in range(N):
        for column in range(N):
            print(snail[row][column], end=' ')
        print()  # 달팽이는 1부터 N*N 까지의 숫자가 시계방향으로 이루어져 있다.
