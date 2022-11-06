def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


T = int(input())  # 테스트 케이스의 수
for x in range(1, T + 1):
    # 1<= N명(1~N) <=100 , 0 <= M = len(edge)
    N, M = map(int, input().split())
    number = [list(map(int, input().split())) for _ in range(M)]
    rep = [i for i in range(N + 1)]
    for e in number:
        rep[find_set(e[1])] = find_set(e[0])  # union
    # 두 사람이 알 수 있는 관계라면, 이러한 사람들을 모두 다 묶어서 하나의 무리
    group = set()
    for p in range(1, N + 1):
        group.add(find_set(p))
    print(f'#{x} {len(group)}')  # 무리의 개수