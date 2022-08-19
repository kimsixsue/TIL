T = int(input())  # 1 ≤ 노선 수 ≤ 50
for t in range(1, T + 1):
    K, N, M = map(int, input().split())  # 각 노선별로 1 ≤ K, N, M ≤ 100
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점 정류장 (0번에서 출발 이동)
    # M : 충전기가 설치된 정류장 번호 (중간에)
    charge_bus_stop_no = list(map(int, input().split()))
    # M 개 == len(charge_bus_stop_no)
    # 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
    charge_bus_stop_no.insert(0, 0)
    min_charge = 0
    # 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력
    for _ in range(M):
        if K < charge_bus_stop_no[_ + 1] - charge_bus_stop_no[_]:
            break
    else:  # 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력
        start = 0  # 적절한 충전소 위치
        i = 1
        while 1:
            for i in range(start + K, start, -1):
                if i in charge_bus_stop_no:
                    min_charge += 1  # 최소 충전횟수 증가
                    start = i
                    break  # 충전소에서 출발
            if i + K >= N:  # 충전할 필요가 없어짐
                break
    print(f'#{t} {min_charge}')  # #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력
