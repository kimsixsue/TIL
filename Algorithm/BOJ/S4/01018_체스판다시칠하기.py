def count(s_row, s_col):
    global small
    global flag
    clr_1 = board[s_row][s_col]
    if clr_1 == 'W':
        clr_2 = 'B'
    else:
        clr_2 = 'W'
    cnt_1, cnt_2, cnt_3, cnt_4 = 0, 0, 0, 0
    for r in range(s_row, s_row + 8):
        for c in range(s_col, s_col + 8):
            if (r + c) % 2 == 1:
                if board[r][c] == clr_1:
                    cnt_1 += 1
                else:
                    cnt_2 += 1
            else:
                if board[r][c] == clr_2:
                    cnt_3 += 1
                else:
                    cnt_4 += 1
    temp = min(cnt_1 + cnt_3, cnt_2 + cnt_4)
    if temp < small:
        small = temp
        flag = True


N, M = map(int, input().split())  # 8 ~ 50
board = [list(input()) for _ in range(N)]
small = 32
flag = False
for row in range(N - 7):
    for col in range(M - 7):
        count(row, col)
if flag is True:
    print(small)
else:
    print(32)
