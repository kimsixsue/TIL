import sys

input = sys.stdin.readline
N = int(input())  # 사람
S, T = map(int, input().split())  # Source Target
M = int(input())  # 관계
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)
# BFS
distance = [-1] * (N + 1)
queue = [S]
distance[S] += 1
while queue:
    s = queue.pop()
    for n in edge[s]:
        if distance[n] == -1:
            queue.append(n)
            distance[n] = distance[s] + 1
print(distance[T])
