# 상하좌우 4방향 중 한 방향을 가진다. (상: 1, 하: 2, 좌: 3, 우: 4)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
T = int(input())  # 총 테스트 케이스의 개수
for x in range(1, T + 1):
    # 5 ≤ N ≤ 100, 1 ≤ M ≤ 1000, 5 ≤ K ≤ 1,000,
    # 구역의 한 변에 있는 셀의 개수 N, 격리 시간 M, 미생물 군집의 개수 K
    N, M, K = map(int, input().split())
    # 각 위치는 0번부터 시작, 각 군집 내 미생물 수는 1 이상 10,000 이하의 정수
    # 최초 미생물 군집 K개의 정보(세로 위치, 가로 위치, 미생물 수, 이동 방향)
    germ = dict()
    for _ in range(K):
        row, col, number, direction = map(int, input().split())
        germ[(row, col)] = [direction, number, number]  # big = max(number)
    for _ in range(M):  # 각 군집들은 1시간마다
        after = dict()
        for rc, dbn in germ.items():
            row, col = rc
            direction, big, number = dbn
            # 이동방향에 있는 다음 셀로 이동한다.
            nr, nc = row + dr[direction], col + dc[direction]
            # 미생물 군집이 이동 후 약품이 칠해진 셀에 도착하면
            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                if number == 1:  # 군집에 미생물이 한 마리 있는 경우
                    continue  # 군집이 사라지게 된다
                number //= 2  # 군집 내 미생물의 절반이 죽고
                if direction % 2 == 1:  # 이동방향이 반대로 바뀐다
                    direction += 1
                else:
                    direction -= 1
            if (nr, nc) not in after:
                after[(nr, nc)] = [direction, number, number]  # 이 때, big = number
            # 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐지게 된다.
            # 합쳐 진 군집의 미생물 수는 군집들의 미생물 수의 합이며,
            elif number < after[(nr, nc)][1]:  # 미생물 수가 동일한 경우는 없다
                after[(nr, nc)][2] += number
            else:  # 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 된다.
                after[(nr, nc)] = [direction, number, number + after[(nr, nc)][2]]
        germ = after  # 군집 갱신
    total = 0
    for d, big, number in germ.values():
        total += number
    print(f"#{x} {total}")  # M 시간 후 남아 있는 미생물 수의 총 합
