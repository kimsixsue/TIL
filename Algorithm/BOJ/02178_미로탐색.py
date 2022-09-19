import sys
from collections import deque

input = sys.stdin.readline
# 미로 배열 row N x col M
N, M = map(int, input().split())
maze = [list(map(int, input()[:-1])) for _ in range(N)]
# 1은 이동할 수 있는 칸
visited = [[False] * M for _ in range(N)]
visited[0][0] = True
queue = deque()
queue.append((0, 0))  # (0,0)에서 (N-1,M-1)으로 이동 최소 칸 수. 시작 도착 위치 포함
while queue:
    row, col = queue.popleft()
    if row == N - 1 and col == M - 1:
        print(maze[N - 1][M - 1])
        break
    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] and not visited[nr][nc]:
            maze[nr][nc] = maze[row][col] + 1
            visited[nr][nc] = True
            queue.append((nr, nc))
