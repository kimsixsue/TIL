import sys

sys.stdin = open('./sample_input.txt')


def bfs(row, col, n):
    visited = [[0] * n for _ in range(n)]
    queue = list()
    queue.append((row, col))
    visited[row][col] = 1
    while queue:
        row, col = queue.pop(0)
        if maze[row][col] == 3:  # 3은 도착
            return visited[row][col] - 2  # 최소 몇 개의 0을 지나면
        for delta_row, delta_col in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            next_row, next_col = row + delta_row, col + delta_col
            if (0 <= next_row < n) and (0 <= next_col < n) and (  # 0은 통로, 1은 벽
                    maze[next_row][next_col] != 1) and (visited[next_row][next_col] == 0):
                queue.append((next_row, next_col))
                visited[next_row][next_col] = visited[row][col] + 1
    return 0  # 경로가 없는 경우 0을 출력


T = int(input())
for t in range(1, T + 1):
    N = int(input())  # 미로의 크기 NxN
    maze = [list(map(int, input())) for _ in range(N)]  # 미로의 통로와 벽에 대한 정보
    start_row, start_col = -1, -1
    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:  # 2는 출발
                start_row, start_col = row, col
                break
        if start_row != -1:
            break

    print(f'#{t} {bfs(start_row, start_col, N)}')  # 출발지에서 도착지에 다다를 수 있는지
