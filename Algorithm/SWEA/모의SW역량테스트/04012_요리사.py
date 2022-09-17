import sys
from itertools import combinations

sys.stdin = open('./04012_요리사_sample_input.txt')

T = int(input())  # 테스트 케이스의 개수
for t in range(1, T + 1):
    answer = 2399881  # EDGE CASE
    N = int(input())  # 식재료의 수
    S = [list(map(int, input().split())) for _ in range(N)]
    combinate = list(combinations(range(N), N // 2))

    if N == 4:  # 4_C_2
        for i, j in combinate[:len(combinate) // 2]:  # 절반만 탐색
            r1, r2 = set(range(N)) - {i, j}  # 여집합
            set_total = S[i][j] + S[j][i]  # 요리 A
            rest_total = S[r1][r2] + S[r2][r1]  # 요리 B

            dif = abs(set_total - rest_total)
            if answer > dif:  # 최소값
                answer = dif

    else:  # (N)_C_(N//2)
        for combi in combinate[:len(combinate) // 2]:  # 절반만 탐색
            com = list(combinations(combi, 2))
            rest = set(range(N)) - set(combi)  # 여집합
            set_total = 0
            for s1, s2 in com:
                set_total += S[s1][s2] + S[s2][s1]  # 요리 A
                r_set = list(combinations(rest, 2))
                rest_total = 0
                for r1, r2 in r_set:
                    rest_total += S[r1][r2] + S[r2][r1]  # 요리 B

            dif = abs(set_total - rest_total)
            if answer > dif:  # 최소값
                answer = dif

    print(f'#{t} {answer}')
