def solution(m, n, puddles):  # col(1~m), row(1~n)
    path = [[0] * (m + 1) for _ in range(n + 1)]
    path[1][1] = 1  # 집
    for col, row in puddles:
        path[row][col] = -1  # 물에 잠긴 지역
    for row in range(1, n + 1):  # 1 ~ n
        for col in range(1, m + 1):  # 1 ~ m
            if path[row][col] != -1:  # 물에 잠기지 않은 지역
                path[row][col] += path[row - 1][col] + path[row][col - 1]
            else:  # 물에 잠긴 지역
                path[row][col] = 0
    answer = path[n][m] % 1000000007  # 학교
    return answer  # 최단경로의 개수


print(solution(
    4,  # m
    3,  # n
    [
        [2, 2]  # puddles
    ]
))  # return = 4
