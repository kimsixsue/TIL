from heapq import heappop, heappush


def dijkstra(source, adj_list):
    s_list = [40000000 for _ in range(len(adj_list) + 1)]
    s_list[source] = 0
    heapq = list()
    heappush(heapq, (0, source))
    while heapq:
        fare, spot = heappop(heapq)
        for n_fare, n_spot in adj_list[spot]:
            n_fare += fare
            if s_list[n_spot] > n_fare:
                s_list[n_spot] = n_fare
                heappush(heapq, (n_fare, n_spot))
    return s_list


def solution(n, s, a, b, fares):
    adj_list = list(list() for _ in range(n + 1))
    for v in fares:  # undirected, fare 우선
        adj_list[v[0]].append((v[2], v[1]))
        adj_list[v[1]].append((v[2], v[0]))
    answer = 40000000
    for v in range(1, n + 1):  # 1 ~ n
        dij = dijkstra(v, adj_list)
        temp = dij[s] + dij[a] + dij[b]
        if answer > temp:
            answer = temp
    return answer
