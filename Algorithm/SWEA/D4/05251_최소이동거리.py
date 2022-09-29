def dijkstra():
    cost = [0] * (N + 1)
    union = [False] * (N + 1)
    union[0] = True  # include 시작 지점
    for _ in range(N + 1):
        cost[_] = direct[0][_]
    for _ in range(N):
        min_v = 11
        sr = 0  # source
        for n in range(N + 1):
            if union[n] is False and min_v > cost[n]:
                min_v = cost[n]  # 최소
                sr = n
        union[sr] = True  # include
        for t in range(N + 1):  # target
            if 0 < direct[sr][t] < 11:  # 다익스트라는 음의 가중치를 다루지 않음
                cost[t] = min(cost[t], cost[sr] + direct[sr][t])
    return cost[N]


tcn = int(input())  # 1 ~ 50
for T in range(1, tcn + 1):
    N, E = map(int, input().split())  # N: 1~1000, E: 1~1000000
    direct = [[11] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):  # s: 1~1000, e: 1~1000, w:1~10
        s, e, w = map(int, input().split())
        direct[s][e] = w  # start, end, weight
    print(f'#{T} {dijkstra()}')