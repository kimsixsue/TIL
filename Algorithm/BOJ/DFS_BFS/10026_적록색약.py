import sys
from collections import deque

input = sys.stdin.readline
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N = int(input())
checked = [[0] * N for _ in range(N)]
drawing = [list(input()[:-1]) for _ in range(N)]

# 비적록색약은 R 과 G 와 B
# 방문한 곳이 B면, 인접도 B인가
queue = deque()
rgb = 0  # 비적록색약 구역 수
for row in range(N):
    for col in range(N):
        if not checked[row][col]:
            checked[row][col] = 1
            color = drawing[row][col]
            queue.append([row, col])
            rgb += 1
            while queue:
                q = queue.popleft()
                for w in range(4):
                    nr, nc = q[0] + dr[w], q[1] + dc[w]
                    if 0 <= nr < N and 0 <= nc < N and not checked[nr][nc] and drawing[nr][nc] == color:
                        checked[nr][nc] = 1
                        queue.append([nr, nc])


def rg_weak(c):
    if c == "B":
        return "B"
    else:
        return "R"


#   적록색약은 B 와 비 B
# 인접이 B인지 B가 아닌지
checked = [[0] * N for _ in range(N)]
queue = deque()
weak = 0  # 적록색약 구역 수
for row in range(N):
    for col in range(N):
        if not checked[row][col]:
            checked[row][col] = 1
            color = rg_weak(drawing[row][col])
            queue.append([row, col])
            weak += 1
            while queue:
                q = queue.popleft()
                for w in range(4):
                    nr, nc = q[0] + dr[w], q[1] + dc[w]
                    if 0 <= nr < N and 0 <= nc < N and not checked[nr][nc] and rg_weak(drawing[nr][nc]) == color:
                        checked[nr][nc] = 1
                        queue.append([nr, nc])
print(rgb, weak)
