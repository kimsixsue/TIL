def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


TCN = int(input())  # 테스트 케이스의 개수
for T in range(1, TCN + 1):  # 1 ~ 50
    # node 0번 ~ V번(1~1000), edge 개수(1~1,000,000)
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda e: e[2])  # KRUSKAL
    rep = [_ for _ in range(V + 1)]  # 대표
    count = 0
    total = 0  # w 가중치(1~10)의 최소 합
    for n1, n2, w in edge:
        if find_set(n1) != find_set(n2):
            count += 1
            total += w
            rep[find_set(n2)] = find_set(n1)
            # if cnt == V:  # 간선 수
            #     break     # 해당 문제는 이 부분 없어도 pass
    print(f'#{T} {total}')