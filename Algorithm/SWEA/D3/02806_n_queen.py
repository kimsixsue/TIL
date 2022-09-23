def n_queen(depth):
    global count
    if depth == N:  # len(queen) = N
        count += 1
        return  # 다음 경우로
    for n in range(N):
        if not checked[n]:
            col[depth] = n  # col[depth]에서 row n에 위치
            flag = True
            for d in range(depth):
                if abs(col[depth] - col[d]) == abs(depth - d):
                    flag = False
                    break  # 대각선 공격 가능
            if flag:
                checked[n] = 1
                n_queen(depth + 1)
                checked[n] = 0


T = int(input())  # 테스트 케이스의 수
for x in range(1, T + 1):
    N = int(input())  # N*N board
    count = 0  # number of case
    col = [0] * N  # 2차원 배열을 1차원 배열로
    checked = [0] * N
    n_queen(0)
    print(f'#{x} {count}')
