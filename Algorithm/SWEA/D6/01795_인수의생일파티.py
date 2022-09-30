from collections import deque


def dijkstra(adj_list):
    path_time = [100000] * (N + 1)
    path_time[X] = 0
    for h, t in adj_list[X]:
        path_time[h] = t
    q = deque()
    for _ in adj_list[X]:
        q.append(_)
    while q:
        now, time = q.popleft()
        if path_time[now] < time:
            continue
        for target in range(len(adj_list[now])):
            next_home, next_time = adj_list[now][target]
            if time + next_time < path_time[next_home]:
                path_time[next_home] = time + next_time
                q.append((next_home, path_time[next_home]))
    return path_time


T = int(input())  # 테스트 케이스의 수
for tcn in range(1, T + 1):
    N, M, X = map(int, input().split())  # 집 N개(1~N), M=len(edge), 인수=X번집
    adj_list_origin = [list() for _ in range(N + 1)]
    adj_list_reverse = [list() for _ in range(N + 1)]
    for _ in range(M):  # 1<= source, target <=N-1
        x, y, c = map(int, input().split())  # 1<= w <=100
        adj_list_origin[x].append((y, c))
        adj_list_reverse[y].append((x, c))
    a = dijkstra(adj_list_origin)
    b = dijkstra(adj_list_reverse)
    faraway = 0  # max(X번 집으로 오고 가는데 드는 시간)
    for h in range(1, N + 1):
        total = a[h] + b[h]
        if faraway < total:
            faraway = total
    print(f'#{tcn} {faraway}')
