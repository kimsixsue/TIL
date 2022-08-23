T = int(input())  # 테스트 케이스의 개수
for testcase in range(1, T + 1):
    N, K = map(int, input().split())  # 5 ≤ 퍼즐 N ≤ 15, 2 ≤ 단어 K ≤ N
    puzzle = [[0] * (N + 2) for _ in range(N + 2)]  # 흰색 부분은 1, 검은색 부분은 0
    for _ in range(1, N + 1):
        puzzle[_][1: N + 1] = list(map(int, input().split()))
    trans = [[0] * (N + 2) for _ in range(N + 2)]  # 전치 행렬
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            trans[row][col] = puzzle[col][row]
    want = [0] + [1] * K + [0]  # 0 1 1 1 0 꼴
    count = 0  # 특정 행이나 열에서 연속해서 1이 K개만 나오면, count += 1
    for row in puzzle[1:-1]:  # 가로
        for cases in range(1, N - K + 2):
            if row[cases - 1: cases + K + 1] == want:
                count += 1
    for row in trans[1:-1]:  # 세로
        for cases in range(1, N - K + 2):
            if row[cases - 1: cases + K + 1] == want:
                count += 1
    print(f'#{testcase} {count}')
