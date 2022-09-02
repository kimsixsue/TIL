"""
4 6
101111
101010
101011
111011
"""
N, M = map(int, input().split())  # row N x column M 배열 미로
maze = [[] for _ in range(N)]  # 길은 항상 있음
for r in range(N):  # (0,0) 에서 (N-1,M-1)으로 1을 통해 이동 가능
    maze[r] = list(map(int, list(input())))
row, col = 0, 0
visited = [[False] * M for _ in range(N)]
visited[0][0] = True

while row != N - 1 and col != M - 1:
    for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr, nc = row + d[0], col + d[1]
        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = True
            maze[nr][nc] += 1
            row, col = nr, nc
print(maze)
