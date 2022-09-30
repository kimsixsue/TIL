def prim(v):
    mst = [False] * (v + 1)
    weight = [10000] * (v + 1)
    weight[0] = 0
    weight[1] = 0
    for _ in range(1, v + 1):
        u = 0
        min_v = 10000
        for i in range(1, v + 1):
            if mst[i] is False and weight[i] < min_v:
                u = i
                min_v = weight[i]
        mst[u] = True
        for t, w in edge[u]:
            if mst[t] is False:
                weight[t] = min(weight[t], w)
    return sum(weight)


V, E = map(int, input().split())  # 1<=len(정점),len(간선)
edge = [list() for _ in range(V + 1)]  # 1번 ~ V번
for _ in range(E):
    A, B, C = map(int, input().split())
    edge[A].append((B, C))  # C는 정수
print(prim(V))
