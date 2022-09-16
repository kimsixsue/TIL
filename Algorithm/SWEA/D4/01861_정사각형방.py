import sys

sys.stdin = open('./01861_정사각형방_input.txt')
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
                            break  # 찾았으면, 다른 방향 볼 필요 없음
    temp = list()
    big_value = 0
    small = 1000001

    for row in range(N):
        for col in range(N):
            if big_value < move[row][col]:  # 더 큰 값으로 바꾸고, 후보 새로
                big_value = move[row][col]
                temp = [number[row][col] - big_value + 1]
            elif big_value == move[row][col]:  # 값 동일, 후보 추가
                temp.append(number[row][col] - big_value + 1)

    for n in temp:  # 가장 작은 숫자
        if small > n:
            small = n

    print(f'#{x} {small} {big_value}')
