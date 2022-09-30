from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
T = int(input())  # 테스트케이스의 수
for C in range(1, T + 1):
    N = int(input())  # 지도의 크기(N x N) 최대 100 x 100
    v = N ** 2  # vertex
    adj_list = [[] for _ in range(v)]
    depth = [list(map(int, input())) for _ in range(N)]  # 0 ~ 9
    for r in range(N):
        for c in range(N):
            source = r * N + c
            for d in range(4):  # 상하좌우
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:
                    target = nr * N + nc
                    time = depth[nr][nc]  # 깊이 == 복구 시간
                    adj_list[source].append((target, time))
    resto = [90000] * v
    resto[0] = 0  # 출발지 = 0
    for road, time in adj_list[0]:
        resto[road] = time  # 경로 복구 시간
    q = deque()
    q.append(adj_list[0][0])
    q.append(adj_list[0][1])
    while q:
        now, time = q.popleft()
        if resto[now] < time:
            continue
        for v in range(len(adj_list[now])):  # 상하좌우
            target, t_time = adj_list[now][v]
            if time + t_time < resto[target]:
                resto[target] = time + t_time
                q.append((target, resto[target]))
    print(f'#{C} {resto[-1]}')
