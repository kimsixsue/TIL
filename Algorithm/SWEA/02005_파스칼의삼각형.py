for testcase in range(1, int(input()) + 1):
    count = int(input())
    triangle = [[1]*_ for _ in range(1, count + 1)]
    if count >= 3:
        for row in range(2, count):
            for col in range(1, row):
                triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
    print(f'#{testcase}')
    for _ in triangle:
        print(*_)
