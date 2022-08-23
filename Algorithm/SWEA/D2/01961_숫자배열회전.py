T = int(input())  # 테스트 케이스의 개수
for t in range(1, T + 1):  # (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

    N = int(input())  # N x N 행렬이 주어질 때, 3 <= N <= 7
    origin = [[0] * N for _ in range(N)]
    for _ in range(N):
        origin[_] = list(map(int, input().split()))

    rotation_090 = [[0] * N for _ in range(N)]
    for row in range(N):  # 90도 회전
        for col in range(N - 1, -1, -1):
            rotation_090[row][col] = origin[N - col - 1][row]

    rotation_180 = [[0] * N for _ in range(N)]
    for row in range(N):  # 180도 회전
        for col in range(N):
            rotation_180[N - row - 1][N - col - 1] = origin[row][col]

    rotation_270 = [[0] * N for _ in range(N)]
    for row in range(N):  # 270도 회전
        for col in range(N - 1, -1, -1):
            rotation_270[row][col] = origin[col][N - row - 1]

    print(f'#{t}')  # 출력의 첫 줄은 '#t' 로 시작
    # 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
    # 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
    for row in range(N):
        print(''.join(map(str, rotation_090[row])),
              ''.join(map(str, rotation_180[row])),
              ''.join(map(str, rotation_270[row])))
