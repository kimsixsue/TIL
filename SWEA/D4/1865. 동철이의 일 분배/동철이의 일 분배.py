def impossible(depth, s):
    global pro
    if depth == N:
        if pro < s:
            pro = s
            # print(pro)
        return
    elif s * 100 ** (N - depth) < pro:
        return
    else:
        for i in range(1, N + 1):
            if not worked[i] and P[depth][i - 1]:
                worked[i] = True
                impossible(depth + 1, s * P[depth][i - 1])
                worked[i] = False


T = int(input())  # 테스트 케이스의 수
for x in range(1, T + 1):
    # 1~N명의 직업이 해야할 일 1~N개
    N = int(input())  # 1 <= (명수 == 일 개수) <= 16
    # i번 직원이 j번 일을 하면 성공할 확률이 P_{i,j}
    P = [list(map(int, input().split())) for _ in range(N)]  # 0 ~ 100
    worked = [False] * (N + 1)
    pro = 0
    impossible(0, 1)
    # “주어진 일이 모두 성공할 확률”의 최댓값
    answer = round(pro / (100 ** (N - 1)), 6)
    # 확률을 퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력
    print(f'#{x} {answer:.6f}')