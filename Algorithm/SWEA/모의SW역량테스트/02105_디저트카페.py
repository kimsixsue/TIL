def tour(row, col, count, direction):
    if direction == 4:
        return
    if 0 <= row < N and 0 <= col < N:
        global best
        # 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 한다
        if direction == 3 and (row, col) == (r, c):
            if best < count:
                best = count
            return
        # 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안 된다
        if not eat[number[row][col]]:
            eat[number[row][col]] = True  # 먹음
            nr, nc = row + dr[direction], col + dc[direction]  # 다음 카페
            tour(nr, nc, count + 1, direction)  # 직진
            tour(nr, nc, count + 1, direction + 1)  # 돌기
            eat[number[row][col]] = False  # 안 먹음


dr = [1, 1, -1, -1]  # 대각선 방향으로 움직일 수 있는 길들이 있다
dc = [1, -1, -1, 1]
T = int(input())  # 총 테스트 케이스의 개수
for t in range(1, T + 1):
    N = int(input())  # 디저트 카페가 모여있는 지역의 한 변의 길이 4 ≤ N ≤ 20
    # 디저트 카페에서 팔고 있는 디저트 종류, 1 이상 100 이하의 정수
    number = [list(map(int, input().split())) for _ in range(N)]
    best = -1  # 디저트를 먹을 수 없는 경우 정답은 -1
    eat = [False] * 101
    for r in range(N):
        for c in range(N):
            tour(r, c, 0, 0)
    print(f'#{t} {best}')  # 가능한 경우 중 디저트를 가장 많이 먹을 때의 디저트 수
