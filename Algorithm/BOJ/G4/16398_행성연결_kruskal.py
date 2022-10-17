from heapq import heappush, heappop


def find_set(n):
    while n != rep[n]:
        n = rep[n]
    return n


def union(v, w):
    pv = find_set(v)
    pw = find_set(w)
    if rank[pv] > rank[pw]:
        rep[pw] = pv
    else:
        rep[pv] = pw
        if rank[pv] == rank[pw]:
            rank[pw] += 1


flow = list()
N = int(input())  # 행성의 수, 1<= N <=1000
for i in range(N):
    C = list(map(int, input().split()))
    for j in range(N):  # undirected
        if i > j:  # C_ii=0
            heappush(flow, (C[j], i, j))
count, total = 0, 0
rep, rank = [n for n in range(N + 1)], [0 for n in range(N + 1)]
while flow:  # kruskal + heapq
    cost, i, j = heappop(flow)
    if find_set(i) != find_set(j):  # 사이클이 없으면
        count += 1
        total += cost
        union(i, j)
        if count == N:  # 모든 행성을 연결
            break
print(total)  # 모든 행성을 연결했을 때, 최소 플로우의 관리비용
