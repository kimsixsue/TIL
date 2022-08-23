for i in range(1, 11):
    width = int(input())  # 가로 길이 칸 수
    heights = list(map(int, input().split()))  # 빌딩의 높이들
    total = 0
    for h in range(2, width - 2):  # 양 끝 2칸 제외 빌딩의 높이 확인
        a, b, c, d = heights[h - 2], heights[h - 1], heights[h + 1], heights[h + 2]
        if heights[h] > a and heights[h] > b and heights[h] > c and heights[h] > d:
            top_of_4 = 0
            for t in a, b, c, d:
                if top_of_4 < t:
                    top_of_4 = t  # 4칸(=좌우두칸) 중 가장 큰 값
            total += heights[h] - top_of_4  # 빌딩에서 조망권이 확보된 세대의 수
    print(f'#{i} {total}')
