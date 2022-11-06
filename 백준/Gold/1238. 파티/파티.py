from heapq import heappush, heappop


def dijkstra(adj_list, total):
    start = X
    total[0], total[start] = 0, 0
    hq = list()
    heappush(hq, (0, start))
    while hq:
        cost_s, source = heappop(hq)
        if total[source] < cost_s:
            continue
        for target, weight in adj_list[source]:
            cost_t = cost_s + weight
            if cost_t < total[target]:
                total[target] = cost_t
                heappush(hq, (cost_t, target))
    return total


N, M, X = map(int, input().split())
adj_list_o = [list() for _ in range(N + 1)]
adj_list_r = [list() for _ in range(N + 1)]
for _ in range(M):
    source, target, weight = map(int, input().split())
    adj_list_o[source].append((target, weight))
    adj_list_r[target].append((source, weight))
total_o = [1000000] * (N + 1)
total_r = [1000000] * (N + 1)
s = dijkstra(adj_list_o, total_o)
t = dijkstra(adj_list_r, total_r)
total = [0] * (N + 1)
for _ in range(1, N + 1):
    total[_] = s[_] + t[_]
print(max(total))
