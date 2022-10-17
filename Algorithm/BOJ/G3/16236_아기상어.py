from collections import deque


def bfs(x, y):
    go_by = [[0] * N for _ in range(N)]
    q = deque([[x, y]])
    fish = list()
    go_by[x][y] = 1
    while q:
        row, col = q.popleft()
        for d in range(4):
            nr, nc = row + dr[d], col + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if go_by[nr][nc] == 0:
                    if can[x][y] > can[nr][nc]:
                        if can[nr][nc] != 0:
                            go_by[nr][nc] = go_by[row][col] + 1
                            fish.append((go_by[nr][nc] - 1, nr, nc))
                        elif can[x][y] == can[nr][nc]:
                            go_by[nr][nc] = go_by[row][col] + 1
                            q.append([nr, nc])
                        elif can[nr][nc] == 0:
                            go_by[nr][nc] = go_by[row][col] + 1
                            q.append([nr, nc])
                    elif can[x][y] == can[nr][nc]:
                        go_by[nr][nc] = go_by[row][col] + 1
                        q.append([nr, nc])
                    elif can[nr][nc] == 0:
                        go_by[nr][nc] = go_by[row][col] + 1
                        q.append([nr, nc])
    return sorted(fish, key=lambda x: (x[0], x[1], x[2]))


N = int(input())
can = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
baby = list()
for s_r in range(N):
    for s_c in range(N):
        if can[s_r][s_c] == 9:
            baby.append(s_r)
            baby.append(s_c)
time = 0
s_r, s_c = baby
size = [2, 0]
while True:
    can[s_r][s_c] = size[0]
    fish = deque(bfs(s_r, s_c))
    if not fish:
        break
    distance, f_r, f_c = fish.popleft()
    time += distance
    size[1] += 1
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
    can[s_r][s_c] = 0
    s_r, s_c = f_r, f_c
print(time)
