def calculate(bs, c, rs):  # bus_stop, count
    global answer  # min(count)
    if bs == N - 1:
        if c < answer:
            answer = c
        return
    elif N - 1 < bs:
        return
    elif answer < c:
        return
    else:
        for i in range(bs + M_i[bs], bs, -1):
            calculate(i, c + 1, rs - i)


T = int(input())  # 1 <= 테스트케이스의 수
for t in range(1, T + 1):
    nmi = list(map(int, input().split()))
    N = nmi[0]  # 3 <= 정류장 수
    M_i = nmi[1:]  # 0 < 정류장 별 배터리 용량 < N
    answer = 10000
    cnt = 0
    calculate(0, 0, sum(M_i))
    print(f'#{t} {answer - 1}')