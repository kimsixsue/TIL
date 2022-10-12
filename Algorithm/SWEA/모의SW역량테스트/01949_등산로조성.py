def dfs(row, col, depth, can_cut):
    global answer  # global can_cut 하면, 대참사
    if answer < depth:
        answer = depth
    visited[row][col] = True
    for way in range(4):
        nr, nc = row + dr[way], col + dc[way]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] is False:
            # 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다
            # 필요한 경우 지형을 깎아 높이를 0 이하로 만드는 것도 가능하다
            if can_cut is True and info[row][col] <= info[nr][nc]:
                for k in range(1, K + 1):
                    if info[nr][nc] - k < info[row][col]:
                        info[nr][nc] -= k
                        dfs(nr, nc, depth + 1, False)
                        info[nr][nc] += k
            # 등산로는 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결
            elif info[nr][nc] < info[row][col]:
                dfs(nr, nc, depth + 1, can_cut)
    visited[row][col] = False


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
T = int(input())  # 총 테스트 케이스의 개수
for t in range(1, T + 1):
    # 지도의 한 변의 길이 3 ≤ N ≤ 8, 최대 공사 가능 깊이 1 ≤ K ≤ 5
    N, K = map(int, input().split())
    # 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수
    info = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = 0
    peak = 0  # 지도에서 가장 높은 봉우리는 최대 5개
    for _ in info:
        if peak < max(_):
            peak = max(_)
    for r in range(N):
        for c in range(N):
            if info[r][c] == peak:  # 등산로는 가장 높은 봉우리에서 시작
                dfs(r, c, 1, True)
    print(f'#{t} {answer}')  # 만들 수 있는 가장 긴 등산로의 길이
