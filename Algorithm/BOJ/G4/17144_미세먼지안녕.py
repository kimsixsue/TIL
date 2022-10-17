def china():
    move = [[0] * C for _ in range(R)]
    for row in range(R):
        for col in range(C):
            if A[row][col] >= 5:
                d = A[row][col] // 5
                for dr, dc in (-1, 0), (1, 0), (0, 1), (0, -1):
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                        move[nr][nc] += d
                        A[row][col] -= d
    for row in range(R):
        for col in range(C):
            A[row][col] += move[row][col]


def purify(start, direction):
    if direction == -1:
        for row in range(start - 1, 0, -1):
            A[row][0] = A[row - 1][0]
        for col in range(0, C - 1):
            A[0][col] = A[0][col + 1]
        for row in range(0, start):
            A[row][C - 1] = A[row + 1][C - 1]
        for col in range(C - 1, 1, -1):
            A[start][col] = A[start][col - 1]
    else:
        for row in range(start + 1, R - 1):
            A[row][0] = A[row + 1][0]
        for col in range(0, C - 1):
            A[R - 1][col] = A[R - 1][col + 1]
        for row in range(R - 1, start, -1):
            A[row][C - 1] = A[row - 1][C - 1]
        for col in range(C - 1, 1, -1):
            A[start][col] = A[start][col - 1]
    A[start][1] = 0


R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
AP = list()
for row in range(R):
    if A[row][0] == -1:
        AP.append(row)
        AP.append(row + 1)
        break
for _ in range(T):
    china()
    purify(AP[0], -1)
    purify(AP[1], 1)
print(sum(map(sum, A)) + 2)
