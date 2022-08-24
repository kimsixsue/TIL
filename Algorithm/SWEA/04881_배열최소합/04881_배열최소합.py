import sys

sys.stdin = open('./sample_input.txt')


def f(i, N, v):
    global min_total
    if min_total < v:
        return
    elif i == N:  # 순열완성
        if min_total > v:
            min_total = v
    else:
        for j in range(i, N):  # P[i]에 들어갈 숫자 P[j] 결정
            P[i], P[j] = P[j], P[i]
            f(i + 1, N, v + array[i][P[i]])
            P[i], P[j] = P[j], P[i]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    array = [[0] * N for _ in range(N)]
    for _ in range(N):
        array[_] = list(map(int, input().split()))
    min_total = 25000  # (행과 열이 모두 다른) 최소 합
    P = list(range(N))
    f(0, N, 0)
    print(f'#{t} {min_total}')
