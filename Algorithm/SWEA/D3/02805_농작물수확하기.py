import sys

sys.stdin = open('./input.txt')

T = int(input())
for t in range(1, T + 1):

    N = int(input())  # N x N 크기의 농장. 농장의 크기 N은 1 이상 49 이하의 홀수
    value = [[0] * N for _ in range(N)]
    for row in range(N):  # 농장 내 농작물의 가치는 0 ~ 5 이다.
        value[row] = list(map(int, input()))
    center = N // 2  # 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능
    profit = 0  # 농장의 규칙에 따라 얻을 수 있는 수익

    # 상단 크기 증가 수확
    for row in range(center):
        for upper_col in range(center - row, center + row + 1):
            profit += value[row][upper_col]
    # 중단 전체 크기 수확
    for col in range(N):
        profit += value[center][col]
    # 하단 크기 감소 수확
    for row in range(center + 1, N):
        for lower_col in range(row - center, N + center - row):
            profit += value[row][lower_col]

    print(f'#{t} {profit}')
