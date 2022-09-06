import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
drawing = list()  # 순회, 1은 색칠이 된 부분
visited = [[0] * m for _ in range(n)]
idx = -1
stack = deque()
for v in range(n):  # 세로, 가로
    for h in range(m):
        if paper[v][h] == 1 and not visited[v][h]:
            idx += 1
            stack.append([v, h])
            drawing.append(1)
            visited[v][h] = 1
            while stack:
                s = stack.popleft()
                for na in [s[0] + 1, s[1]], [s[0] - 1, s[1]], [s[0], s[1] + 1], [s[0], s[1] - 1]:
                    if 0 <= na[0] < n and 0 <= na[1] < m and paper[na[0]][na[1]] == 1 and not visited[na[0]][na[1]]:
                        visited[na[0]][na[1]] = 1
                        stack.append(na)
                        drawing[idx] += 1
print(len(drawing))  # 그림의 개수
if len(drawing):
    print(max(drawing))  # 가장 넓은 그림의 넓이
else:  # 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
    print(0)
