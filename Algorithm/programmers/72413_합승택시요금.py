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


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10],
         [3, 5, 24],
         [5, 6, 2],
         [3, 1, 41],
         [5, 1, 24],
         [4, 6, 50],
         [2, 4, 66],
         [2, 3, 22],
         [1, 6, 25]]
print(solution(n, s, a, b, fares))  # 82

n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9],
         [4, 6, 4],
         [3, 6, 1],
         [3, 2, 3],
         [2, 1, 6]]
print(solution(n, s, a, b, fares))  # 14

n = 6
s = 4
a = 5
b = 6
fares = [[2, 6, 6],
         [6, 3, 7],
         [4, 6, 7],
         [6, 5, 11],
         [2, 5, 12],
         [5, 3, 20],
         [2, 4, 8],
         [4, 3, 9]]
print(solution(n, s, a, b, fares))  # 18
