for testcase in range(1, 11):  # 10개의 테스트 케이스가 주어진다.

    size = int(input())  # 정사각형 테이블의 한 변의 길이가 주어진다. (이 값은 항상 100이다)
    table = [[0] * size for _ in range(size)]  # 테이블의 크기는 100x100으로 주어진다.
    for _ in range(size):  # 100 x 100크기의 테이블의 초기 모습이 주어진다.
        table[_] = list(map(int, input().split()))
    # N극(1) 성질을 가지는 자성체는 테이블의 아래부분에 위치한 S극(2)에만 이끌린다.
    # S극(2) 성질을 가지는 자성체는 테이블의   윗부분에 위치한 S극(1)에만 이끌린다.
    # 편의 위해 전치행렬로,     # 1 => right    # left <= 2
    for i in range(100):
        for j in range(100):
            if i > j:
                table[i][j], table[j][i] = table[j][i], table[i][j]

    # 자성체들
    stack = [[] for _ in range(100)]
    for a in range(100):
        for b in range(100):
            if table[a][b] == 1:
                stack[a].append(1)
            if table[a][b] == 2:
                stack[a].append(2)

    deadlock = 0  # 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수
    # stack 순회
    for line in range(100):
        idx = 0
        while idx < len(stack[line]) - 1:
            if stack[line][idx] == 1 and stack[line][idx + 1] == 2:
                deadlock += 1  # 교착상태
                idx += 2
            else:
                idx += 1

    print(f'#{testcase} {deadlock}')
