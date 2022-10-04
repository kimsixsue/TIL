from heapq import heappush, heappop


def dijkstra(adj_list, total):
    start = X
    total[0], total[start] = 0, 0
    hq = list()
    heappush(hq, (0, start))  # 힙큐에 (0, 시작점) 넣기
    while hq:  # DO-WHILE
        cost_s, source = heappop(hq)  # Time, 출발지
        if total[source] < cost_s:
            continue
        for weight, target in adj_list[source]:
            cost_t = cost_s + weight
            if cost_t < total[target]:
                total[target] = cost_t
                heappush(hq, (cost_t, target))  # 힙큐에 (Time, 목적지) 넣기
    return total


# 마을(학생) N(1<=X<=N), M = len(directed edge), X = 파티 마을
N, M, X = map(int, input().split())
adj_list_o = [list() for _ in range(N + 1)]
adj_list_r = [list() for _ in range(N + 1)]
for _ in range(M):  # 1<= T_i <= 100
    s, g, T = map(int, input().split())
    adj_list_o[s].append((T, g))  # start = Time, goal
    adj_list_r[g].append((T, s))  # goal = Time, start
total_o = [1000000] * (N + 1)
total_r = [1000000] * (N + 1)
toX = dijkstra(adj_list_o, total_o)  # 파티 가기
fromX = dijkstra(adj_list_r, total_r)  # 집 돌아오기
answer = [0] * (N + 1)
for _ in range(1, N + 1):
    answer[_] = toX[_] + fromX[_]
print(max(answer))  # 오고 가는데 가장 오래 걸리는 소요시간
