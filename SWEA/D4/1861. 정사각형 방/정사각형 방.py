dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())  # 테스트 케이스의 수
for x in range(1, T + 1):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]
    move = [[1] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            stack = [(row, col)]
            while stack:
                s = stack.pop()
                for d in range(4):
                    next_r, next_c = s[0] + dr[d], s[1] + dc[d]
                    if 0 <= next_r < N and 0 <= next_c < N:
                        if number[s[0]][s[1]] + 1 == number[next_r][next_c]:
                            move[next_r][next_c] = move[s[0]][s[1]] + 1
                            stack.append((next_r, next_c))
                            break
    temp = list()
    big_value = 0
    for row in range(N):
        for col in range(N):
            if big_value < move[row][col]:
                big_value = move[row][col]
                temp = [number[row][col] - big_value + 1]
            elif big_value == move[row][col]:
                temp.append(number[row][col] - big_value + 1)
    small = 1000001
    for n in temp:
        if small > n:
            small = n
    print(f'#{x} {small} {big_value}')
