from heapq import heappush, heappop

N = int(input())  # 행성의 수, 1<= N <=1000
C = [list(map(int, input().split())) for _ in range(N)]  # undirected, 1~10^8, C_ii=0
flow = [list() for _ in range(N)]
for i in range(N):
    for j in range(N):
        flow[i].append((C[i][j], j))
start, total, count = 0, 0, 0
mst = [False] * N  # 정점
mst[start] = True
hq = list()
for cost, j in flow[start]:
    heappush(hq, (cost, j))
while count < N - 1:
    cost, j = heappop(hq)  # 최소 비용의 간선
    if mst[j]:
        continue
    total += cost
    count += 1
    mst[j] = True
    for n_cost, n_j in flow[j]:  # 인접 정점
        if not mst[n_j]:
            heappush(hq, (n_cost, n_j))  # prim
print(total)  # 모든 행성을 연결했을 때, 최소 플로우의 관리비용
