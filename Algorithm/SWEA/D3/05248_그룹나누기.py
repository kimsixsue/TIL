def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


tcn = int(input())  # 테스트 케이스의 개수
for T in range(1, tcn + 1):
    N, M = map(int, input().split())  # 2<=출석번호 1~N<=100
    number = list(map(int, input().split()))  # 1<=M장의 신청서<=100 쌍의 번호
    rep = [_ for _ in range(N + 1)]
    for _ in range(M):
        a, b = number[_ * 2], number[_ * 2 + 1]
        rep[find_set(b)] = find_set(a)  # union
    team = set()
    for _ in range(1, N + 1):
        team.add(find_set(_))  # 대표자만 남음
    # 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성
    print(f'#{T} {len(team)}')  # 전체 몇 개의 조가 만들어지는지