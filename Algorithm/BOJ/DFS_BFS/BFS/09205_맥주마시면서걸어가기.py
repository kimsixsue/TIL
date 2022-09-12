import sys

input = sys.stdin.readline
t = int(input())  # testcase number
for _ in range(t):

    n = int(input())  # CVS number
    x, y = [[] for _ in range(n + 2)], [[] for _ in range(n + 2)]
    for _ in range(n + 2):  # (x, y) * (n+2)
        x[_], y[_] = map(int, input().split())

    # find edge
    edge = [[] for _ in range(n + 2)]
    for a in range(n + 2):
        for b in range(a + 1, n + 2):
            if abs(x[b] - x[a]) + abs(y[b] - y[a]) <= 1000:
                edge[a].append(b)
                edge[b].append(a)

    # DFS (index: 0 -> n+1)
    visited = [False] * (n + 2)
    visited[0] = True
    queue = [0]
    while queue:
        q = queue.pop()
        for nxt in edge[q]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
    if visited[-1]:
        print('happy')
    else:
        print('sad')
