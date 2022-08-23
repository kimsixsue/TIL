# 상우좌하
dr = [1, 0, 0, -1]
dc = [0, 1, -1, 0]

T = int(input())
for testcase_number in range(1, T + 1):

    N = int(input())  # 미로의크기
    maze = [''] * N
    for _ in range(N):
        maze[_] = input()  # 0은 통로, 1은 벽, 2는 출발, 3은 도착
    # start, arriv
    for row in range(N):
        for col in range(N):
            if maze[row][col] == '2':
                start = int(row), int(col)
            if maze[row][col] == '3':
                arriv = int(row), int(col)
    visited = [[False] * N for _ in range(N)]
    answer = -1
    stack = []

    while True:
        for direction in range(4):
            row = start[0] + dr[direction]
            col = start[1] + dc[direction]
            if 0 <= row < N and 0 <= col < N and maze[row][col] != '1' \
                    and (row, col) not in stack and not visited[row][col]:
                stack.append(start)
                start = row, col
                break
        else:
            visited[start[0]][start[1]] = True
            if stack:
                start = stack.pop()
            else:
                answer = 0
                break
        if start == arriv:
            answer = 1  # 도착할 수 있으면 1, 아니면 0, 또는 ‘error’
            break

    print(f'#{testcase_number} {answer}')
