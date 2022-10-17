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


pipe = list()
N = int(input())  # 1~300 개의 논
for w in range(1, N + 1):  # 논에 우물을 팔 때 드는 비용
    heappush(pipe, (int(input()), 0, w))  # 0->i = 우물 파는 비용
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    for j in range(1, N + 1):  # 논을 연결하는데 드는 비용
        if i != j:  # P_ii = 0
            heappush(pipe, (info[j - 1], i, j))
count, total = 0, 0
rep, rank = [n for n in range(N + 1)], [0 for n in range(N + 1)]
while pipe:  # kruskal + heapq
    cost, i, j = heappop(pipe)
    if find_set(i) != find_set(j):  # 사이클이 없으면
        count += 1
        total += cost
        union(i, j)
        if count == N:  # 모든 논을 연결
            break
print(total)  # 모든 논에 물을 대는데 필요한 최소비용
