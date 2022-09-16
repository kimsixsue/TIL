import sys
from collections import deque

sys.stdin = open('./01953_탈주범검거_sample_input.txt')

tnl = {
    1: [[-1, 0], [1, 0], [0, -1], [0, 1]],  # 상하좌우
    2: [[-1, 0], [1, 0]],  # 상하
    3: [[0, -1], [0, 1]],  # 좌우
    4: [[-1, 0], [0, 1]],  # 상    우
    5: [[1, 0], [0, 1]],  # 하  우
    6: [[1, 0], [0, -1]],  # 하좌
    7: [[-1, 0], [0, -1]],  # 상  좌
}


def bfs():
    can = 1  # L hour 에 몇 곳이 가능한가
    while queue:
        q = queue.popleft()
        way = tnl[under[q[0]][q[1]]]
        for w in way:
            nr, nc = q[0] + w[0], q[1] + w[1]
            if 0 <= nr < N and 0 <= nc < M and under[nr][nc] and not candi[nr][nc]:
                # 현재 w와 nr nc의 터널이 호환되면
                if [-w[0], -w[1]] in tnl[under[nr][nc]]:
                    queue.append([nr, nc])
                    candi[nr][nc] = candi[q[0]][q[1]] + 1
                    if candi[nr][nc] > L:
                        return can  # L hour 기준 후보 수
                    can += 1  # 후보 증가
    return can  # 순회 완료


T = int(input())  # 테스트 케이스의 개수
for x in range(1, T + 1):
    # 터널 r c / 맨홀 r c / hour
    N, M, R, C, L = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]
    candi = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append([R, C])
    candi[R][C] = 1

    print(f'#{x} {bfs()}')
