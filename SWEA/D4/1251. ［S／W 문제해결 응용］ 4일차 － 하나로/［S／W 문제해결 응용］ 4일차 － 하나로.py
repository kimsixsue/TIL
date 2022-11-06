T = int(input())  # 전체 테스트 케이스의 수
for C in range(1, T + 1):
    N = int(input())  # 1≤ len(섬) ≤1,000
    X = list(map(int, input().split()))  # 0≤ 섬의 X 좌표 ≤1,000,000
    Y = list(map(int, input().split()))  # 0≤ 섬의 Y 좌표 ≤1,000,000
    E = float(input())  # 0≤ 환경 부담 세율 E ≤1
    L2 = [[0] * N for f in range(N)]  # 거리^2, 대각선은 0
    for i1 in range(N):
        for i2 in range(N):
            if i1 < i2:
                L2[i2][i1] = L2[i1][i2] = (X[i1] - X[i2]) ** 2 + (Y[i1] - Y[i2]) ** 2
    INF = 2 * 10 ** 12  # 가장 먼 거리^2
    mst = [False] * N
    distance = [INF] * N  # 거리^2
    distance[0] = 0
    for _ in range(N):
        i1 = 0
        min_v = INF
        for t in range(N):  # min(거리) 탐색
            if mst[t] is False and distance[t] < min_v:
                i1 = t
                min_v = distance[t]
        mst[i1] = True  # 포함
        for i2 in range(N):
            if mst[i2] is False and L2[i1][i2] > 0:
                distance[i2] = min(distance[i2], L2[i1][i2])
    answer = round(E * sum(distance))  # 소수 첫째 자리에서 반올림하여 정수 형태로
    print(f'#{C} {answer}')  # 최소 환경 부담금 출력