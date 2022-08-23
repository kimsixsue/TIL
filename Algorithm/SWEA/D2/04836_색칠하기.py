for testcase in range(1, int(input()) + 1):  # 1 ≤ 테스트 케이스 개수 ≤ 50
    matrix = list([0] * 10 for _ in range(10))  # 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
    for _ in range(int(input())):  # 2 ≤ 칠할 영역의 개수 ≤ 30
        # N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때,
        # 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color 가 주어진다.
        # ( 0 ≤ r1, c1, r2, c2 ≤ 9 ), color = 1 (빨강), color = 2 (파랑)
        r1, c1, r2, c2, color = map(int, input().split())  # 주어진 정보에서 같은 색인 영역은 겹치지 않는다.
        painting = list([0] * 10 for _ in range(10))
        for outer in range(r1, r2 + 1):
            for inner in range(c1, c2 + 1):
                painting[outer][inner] += color
                matrix[outer][inner] += painting[outer][inner]
    total = 0
    for outer in range(10):
        for inner in range(10):
            if matrix[outer][inner] == 3:
                total += 1
    print(f'#{testcase} {total}')  # 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램
