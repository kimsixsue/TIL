import sys

sys.stdin = open('./input.txt')

TC = 10  # 총 10개의 테스트 케이스가 주어진다.
for tcn in range(1, TC + 1):
    length = int(input())  # 찾아야 하는 회문의 길이
    size = 8  # 8x8 크기의 평면 글자판
    plane = [[''] * size for _ in range(size)]
    for row in range(size):  # 각 칸의 들어가는 글자는 'A', 'B', 'C' 중 하나이다.
        plane[row] = list(map(str, input()))
    count = 0  # 제시된 길이를 가진, 가로 또는 세로로 이어진, 회문의 개수
    # 가로 회문
    for row in range(size):
        for col in range(size - length + 1):
            if plane[row][col:col + length] == plane[row][col:col + length][::-1]:
                count += 1
    # 전치 행렬
    for r in range(size):
        for c in range(size):
            if r > c:
                plane[r][c], plane[c][r] = plane[c][r], plane[r][c]
    # 세로 회문
    for row in range(size):
        for col in range(size - length + 1):
            if plane[row][col:col + length] == plane[row][col:col + length][::-1]:
                count += 1
    print(f'#{tcn} {count}')
