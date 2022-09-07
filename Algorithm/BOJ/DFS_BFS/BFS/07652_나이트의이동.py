import sys
from collections import deque

input = sys.stdin.readline
dr = [2, 2, 1, 1, -1, -1, -2, -2]
dc = [1, -1, 2, -2, 2, -2, 1, -1]
tcn = int(input())  # 테스트 케이스의 개수
for _ in range(tcn):
    length = int(input())  # 체스판의 한 변의 길이, 4 이상
    visited = [[0] * length for _ in range(length)]
    move = [[0] * length for _ in range(length)]
    now = list(map(int, input().split()))  # 나이트가 현재 있는 칸, 0 ~ len -1
    target = list(map(int, input().split()))  # 나이트가 이동하려고 하는 칸, 0 ~ len -1
    if now == target:
        print(0)
        continue
    queue = deque([now])
    while queue:
        if move[target[0]][target[1]]:
            print(move[target[0]][target[1]])
            break
        q = queue.popleft()
        visited[q[0]][q[1]] = 1
        for w in range(8):
            nr, nc = q[0] + dr[w], q[1] + dc[w]
            # nr, nc가 0 ~ length-1, not visited nr nc
            if 0 <= nr < length and 0 <= nc < length and not move[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                move[nr][nc] = move[q[0]][q[1]] + 1
                queue.append([nr, nc])
