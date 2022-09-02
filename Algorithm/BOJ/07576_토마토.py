import sys
from collections import deque

input = sys.stdin.readline


def min_date(tom):
    count = 0  # 저장될 때부터 모든 토마토가 익어있는 상태
    for _ in tom:
        if 0 not in _:
            count += 1
    if count == N:
        return 0

    queue = deque()
    for row in range(N):
        for col in range(M):
            if tom[row][col] == 1:
                queue.append((row, col))
    # BFS
    day = -1  # 0이 전부 1로 바뀌는 최소 일수
    while queue:
        for _ in range(len(queue)):
            q = queue.popleft()
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr, nc = q[0] + dr, q[1] + dc
                if 0 <= nr < N and 0 <= nc < M and not tom[nr][nc]:
                    tom[nr][nc] = 1
                    queue.append((nr, nc))
        day += 1  # 하루가 지나면, 1 인접한 0 -> 1

    for _ in tom:  # 토마토가 모두 익지는 못하는 상황
        if 0 in _:
            return -1

    return day


# col, row
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
print(min_date(tomato))
