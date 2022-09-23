import sys

sys.stdin = open('./02819_격자판의숫자이어붙이기_sample_input.txt')


def move(num, r, c):  # 시작 지점 포함 종료 지점까지, 이어 붙이면 7자리 string
    if len(num) == 7:
        candi.add(num)
        return
    else:
        for w in range(4):
            nr, nc = r + dr[w], c + dc[w]
            if 0 <= nr < 4 and 0 <= nc < 4:  # 범위 체크 필요
                move(num + board[nr][nc], nr, nc)


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
T = int(input())  # 테스트 케이스의 수
for x in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]  # str(0~9)
    candi = set()
    for r in range(4):
        for c in range(4):
            move(board[r][c], r, c)
    print(f'#{x} {len(candi)}')
