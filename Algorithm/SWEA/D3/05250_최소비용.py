from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
tcn = int(input())  # 테스트 케이스의 개수 1 ~ 50
for T in range(1, tcn + 1):
    N = int(input())  # 표의 가로, 세로 칸수 3 ~ 100
    # 0 <= 이동 가능한 지역의 높이 정보 H[row][col] <= 999
    H = [list(map(int, input().split())) for _ in range(N)]
    v = N ** 2
    adj_list = [[] for _ in range(v)]  # 인접 리스트
    for r in range(N):
        for c in range(N):
            source = r * N + c
            for d in range(4):  # 상하좌우 인접 지역으로만 이동
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:  # 표시된 지역
                    target = nr * N + nc
                    fuel = 1  # 이동 기본 연료 = 1
                    if H[nr][nc] > H[r][c]:  # 더 높은 곳으로 이동
                        fuel += H[nr][nc] - H[r][c]  # 높이 차이
                    adj_list[source].append((target, fuel))
    consum = [1000000] * v
    consum[0] = 0  # 출발은 맨 왼쪽 위
    for v, d in adj_list[0]:
        consum[v] = d
    q = deque()
    q.append(adj_list[0][0])
    q.append(adj_list[0][1])
    while q:
        now, dist = q.popleft()
        if consum[now] < dist:
            continue
        for v in range(len(adj_list[now])):
            n_v, n_dist = adj_list[now][v]
            if dist + n_dist < consum[n_v]:  # min(연료)
                consum[n_v] = dist + n_dist
                q.append((n_v, consum[n_v]))
    print(f'#{T} {consum[-1]}')  # 도착지는 가장 오른쪽 아래