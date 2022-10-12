# row 가 다를 경우만 만들어도 통과
def in_a_row(col, harvest, earnings):
    if C < harvest:
        return
    global r_best
    if r_best < earnings:
        r_best = earnings
    if col < start + M:
        # 하나의 벌통에 있는 모든 꿀을 한번에 하나의 용기에 담아야 한다.
        # 각 용기에 있는 꿀의 양의 제곱만큼의 수익
        in_a_row(col + 1, harvest + honey[row][col], earnings + honey[row][col] ** 2)
        in_a_row(col + 1, harvest, earnings)


T = int(input())  # 총 테스트 케이스의 개수
for x in range(1, T + 1):
    # 벌통들의 크기 N, 선택할 수 있는 벌통의 개수 M, 두 일꾼이 채취할 수 있는 꿀의 최대 양 C
    # 3 ≤ N ≤ 10, 1 ≤ M ≤ 5, 10 ≤ C ≤ 30
    N, M, C = map(int, input().split())
    # 하나의 벌통에서 채취할 수 있는 꿀의 양은 1 이상 9 이하의 정수
    honey = [list(map(int, input().split())) for _ in range(N)]
    total = [0] * N
    for row in range(N):
        r_best = 0
        # 두 명의 일꾼은 서로 겹치지 않게, 가로로 연속되도록 M개의 벌통을 선택 채취한다.
        for start in range(N - M + 1):  # 경우의 수 = N - M + 1
            in_a_row(start, 0, 0)
        total[row] = r_best
    total.sort(reverse=True)
    print(f"#{x} {total[0] + total[1]}")  # 두 일꾼이 꿀을 채취하여 얻을 수 있는 최대 수익
