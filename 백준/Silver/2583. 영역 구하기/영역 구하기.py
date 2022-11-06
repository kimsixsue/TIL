import sys
from collections import deque

input = sys.stdin.readline
M, N, K = map(int, input().split())  # 1~100
rect = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            rect[y][x] = 1  # 상하반전
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
queue = deque()
area = list()
for row in range(M):
    for col in range(N):
        if not rect[row][col]:
            area.append(1)
            rect[row][col] = 1
            queue.append([row, col])
            while queue:
                q = queue.popleft()
                for w in range(4):
                    nr, nc = q[0] + dr[w], q[1] + dc[w]
                    if 0 <= nr < M and 0 <= nc < N and not rect[nr][nc]:
                        area[-1] += 1
                        rect[nr][nc] = 1
                        queue.append([nr, nc])
print(len(area))
print(*sorted(area))
