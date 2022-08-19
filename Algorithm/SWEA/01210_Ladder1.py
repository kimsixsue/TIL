for _ in range(10):
    testcase = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    row, col = 99, 0
    for _ in range(100):
        if matrix[row][_] == 2:
            col = _
            break
    while row > 0:
        if (col > 0) and (matrix[row][col - 1]):
            matrix[row][col] = 0
            col -= 1
        elif (col < 99) and (matrix[row][col + 1]):
            matrix[row][col] = 0
            col += 1
        else:
            row -= 1
    print(f'#{testcase} {col}')
