import sys
from collections import deque

input = sys.stdin.readline


def find_sb():
    for f in range(L):
        for r in range(R):
            for c in range(C):
                if maze[f][r][c] == "S":
                    return f, r, c


def find_exit():
    for f in range(L):
        for r in range(R):
            for c in range(C):
                if maze[f][r][c] == "E":
                    print("Trapped!")
                    return


d1 = [0, 0, 0, 0, -1, 1]
d2 = [0, 0, -1, 1, 0, 0]
d3 = [-1, 1, 0, 0, 0, 0]
while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    visited = [[[0] * C for _ in range(R + 1)] for _ in range(L)]
    maze = [[list(input()[:-1]) for _ in range(R + 1)] for _ in range(L)]
    sb = find_sb()
    maze[sb[0]][sb[1]][sb[2]] = 0
    queue = deque([sb])  # 상범 좌표
    while queue:
        q = queue.popleft()  # 층, row, col
        if str(maze[q[0]][q[1]][q[2]]).isdigit():
            visited[q[0]][q[1]][q[2]] = 1
            for w in range(6):
                n1, n2, n3 = q[0] + d1[w], q[1] + d2[w], q[2] + d3[w]
                if 0 <= n1 < L and 0 <= n2 < R and 0 <= n3 < C and not visited[n1][n2][n3]:
                    if maze[n1][n2][n3] == '.':
                        queue.append((n1, n2, n3))
                        visited[n1][n2][n3] = 1
                        maze[n1][n2][n3] = maze[q[0]][q[1]][q[2]] + 1
                    elif maze[n1][n2][n3] == 'E':  # 탈출
                        queue = deque()
                        visited[n1][n2][n3] = 1
                        maze[n1][n2][n3] = maze[q[0]][q[1]][q[2]] + 1
                        print(f'Escaped in {maze[n1][n2][n3]} minute(s).')
                        break
    find_exit()
