import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())
# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
# 숫자는 1 이상. 양방향. 가중치 존재할 수 있음
edge = [[] for _ in range(N + 1)]
for m in range(1, M + 1):  # 간선들
    s, t = map(int, input().split())  # 양방향
    edge[s].append(t)
    edge[t].append(s)
for _ in edge:  # 오름차순
    _.sort()
# DFS
visited = [False] * (N + 1)
now = V
order = [now]
stack = [now]
while stack:
    visited[now] = True
    for nxt in range(N + 1):
        if not visited[nxt] and nxt in edge[now]:
            stack.append(now)
            now = nxt
            order.append(nxt)
            break
    else:
        now = stack.pop()
print(*order)
# BFS
order = list()
queue = [V]
while queue:
    s = queue.pop(0)
    if s not in order:
        order.append(s)
        for t in edge[s]:
            if t not in order:
                queue.append(t)
print(*order)
