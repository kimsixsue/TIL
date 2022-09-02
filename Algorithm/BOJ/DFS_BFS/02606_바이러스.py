import sys

input = sys.stdin.readline
N = int(input())
P = int(input())
C = [[] for _ in range(N + 1)]
for _ in range(P):
    a, b = map(int, input().split())
    C[a].append(b)
    C[b].append(a)
# BFS
visited = [0] * (N + 1)
queue = list()
queue.append(1)
while queue:
    t = queue.pop(0)
    if not visited[t]:
        visited[t] = 1
        for i in C[t]:
            if not visited[i]:
                queue.append(i)
print(sum(visited) - 1)
