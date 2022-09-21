import sys

sys.stdin = open('./05188_최소합_sample_input.txt')
T = int(input())  # 테스트케이스의 수
for t in range(1, T + 1):
    N = int(input())  # 가로 세로 칸 수
    board = [list(map(int, input().split())) for _ in range(N)]
    for col in range(1, N):  # 상단은 좌측칸 + 자신
        board[0][col] += board[0][col - 1]
    for row in range(1, N):
        board[row][0] += board[row - 1][0]  # 좌측은 상단칸 + 자신
        for col in range(1, N):  # 좌상 중 작은 값 + 자신
            board[row][col] += min(board[row][col - 1], board[row - 1][col])
    answer = board[N - 1][N - 1]
    print(f'#{t} {answer}')
