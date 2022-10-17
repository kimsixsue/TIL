from heapq import heappush, heappop

N = int(input())  # 1~300 개의 논
hq = list()
pipe = [list() for _ in range(N + 1)]
for w in range(1, N + 1):  # 논에 우물을 팔 때 드는 비용
    heappush(hq, (int(input()), w))  # 0->w = 우물 파는 비용
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    for j in range(1, N + 1):  # 논을 연결하는데 드는 비용
        if i != j:  # P_ii = 0, undirected
            heappush(pipe[i], (info[j - 1], j))
total, count = 0, 0
mst = [False] * (N + 1)  # 정점
mst[0] = True
while True:
    cost, j = heappop(hq)  # 최소 비용의 간선
    if mst[j]:
        continue
    total += cost
    mst[j] = True
    if count == N - 1:
        break
    count += 1
    while pipe[j]:
        n_cost, n_j = heappop(pipe[j])
        if not mst[n_j]:
            heappush(hq, (n_cost, n_j))  # prim
print(total)
