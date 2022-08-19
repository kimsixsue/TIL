T = int(input())  # 1 ≤ 테스트 케이스 개수 ≤ 50
for t in range(1, T + 1):
    N, M = map(int, input().split())  # 10 ≤ 정수의 개수 N ≤ 100,  2 ≤ 구간의 개수 M ＜ N
    ai = list(map(int, input().split()))  # 1 ≤ N개의 정수 ai ≤ 10000
    biggest_sumofintervals = 0
    smallest_sumofintervals = N * 10000
    case = N - M + 1
    sumofintervals = [0] * N  # M개의 합이 가장 큰 경우와 가장 작은 경우의 차이
    for outer in range(case):
        for inner in range(M):
            sumofintervals[outer] += ai[outer + inner]
        if biggest_sumofintervals < sumofintervals[outer]:
            biggest_sumofintervals = sumofintervals[outer]
        if smallest_sumofintervals > sumofintervals[outer]:
            smallest_sumofintervals = sumofintervals[outer]
    print(f'#{t} {biggest_sumofintervals - smallest_sumofintervals}')
