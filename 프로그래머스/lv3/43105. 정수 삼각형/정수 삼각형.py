def solution(triangle):
    height = len(triangle)  # 삼각형의 높이 1 ~ 500
    for u in range(1, height):  # 높이 별 숫자 개수 = triangle[높이]
        for d in range(0, u + 1):  # 개수가 1씩 증가
            if d == 0:  # left
                triangle[u][0] += triangle[u - 1][0]
            elif d == u:  # right
                triangle[u][-1] += triangle[u - 1][-1]
            else:  # 가운데
                triangle[u][d] += max([triangle[u - 1][d - 1], triangle[u - 1][d]])
    answer = max(triangle[-1])
    return answer


print(solution([
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]))  # result = 30
