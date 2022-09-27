def calculate(depth, s):
    global total
    if depth == N:  # 최소 생산 비용
        if s < total:
            total = s
        return
    elif total < s:  # 최소 생산 비용
        return
    else:
        for i in range(N):
            if not visited[i]:  # 공장에서 한 곳당 한가지씩 생산
                visited[i] = True
                calculate(depth + 1, s + V[depth][i])
                visited[i] = False


T = int(input())  # 1 <= 테스트케이스의 수
for t in range(1, T + 1):
    N = int(input())  # 3 <= 제품 수 <= 15
    # 1 <= 각 제품의 공장별 생산비용 <= 99
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    total = 22275
    calculate(0, 0)  # 전체 제품의 최소 생산 비용을 계산
    print(f'#{t} {total}')

"""
3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4

"""
