def count_node(n):
    global count
    if n:
        count += 1
        count_node(c_left[n])
        count_node(c_right[n])


T = int(input())  # 테스트케이스의 수
for t in range(1, T + 1):
    count = 0
    E, N = map(int, input().split())  # E 간선의 개수, N ROOT
    V = E + 1  # NODE 개수
    par = [0] * (V + 1)
    c_left = [0] * (V + 1)
    c_right = [0] * (V + 1)
    pc_pair = list(map(int, input().split()))
    for i in range(E):
        p, c = pc_pair[i * 2], pc_pair[i * 2 + 1]
        par[c] = p
        if c_left[p]:
            c_right[p] = c
        else:
            c_left[p] = c
    count_node(N)  # 서브 트리에 속한 노드의 개수
    print(f'#{t} {count}')
