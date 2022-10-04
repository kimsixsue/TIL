import sys
from collections import deque

input = sys.stdin.readline
T = int(input())  # 테스트 케이스의 개수
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
for t in range(T):
    M, N, K = map(int, input().split())
    # 가로(1~50), 세로(1~50), 배추(1~2500)
    cabbage = [list(map(int, input().split())) for _ in range(K)]
    checked = [[0] * N for _ in range(M)]
    worm = 0  # 배추흰지렁이
    queue = deque()
    for c in cabbage:
        if not checked[c[0]][c[1]]:
            checked[c[0]][c[1]] = 1
            queue.append(c)
            while queue:
                q = queue.popleft()
                for _ in range(4):
                    nr, nc = q[0] + dr[_], q[1] + dc[_]
                    if 0 <= nr < M and 0 <= nc < N and not checked[nr][nc] and [nr, nc] in cabbage:
                        checked[nr][nc] = 1
                        queue.append([nr, nc])
            worm += 1
    print(worm)
