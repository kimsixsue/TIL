T = int(input())  # 총 테스트 케이스의 개수
for t in range(1, T + 1):

    # 1일 이용권의 요금, 1달 이용권의 요금, 3달 이용권의 요금, 1년 이용권의 요금
    day, month, three, year = map(int, input().split())  # 10 ~ 3000
    # (내년) 1월부터 12월까지의 이용 계획
    plan_m = list(map(int, input().split()))  # 0 ~ 11

    DP = [0] * 13  # 0 ~ 12, 누적
    for m in range(1, 13):  # 1 ~ 12
        fee_d = day * plan_m[m - 1]  # 1일 이용권
        fee_m = min(fee_d, month)  # min(1일 이용권, 1달 이용권)
        if m < 3:
            DP[m] = DP[m - 1] + fee_m  # 누적
        else:
            fee_t = three + DP[m - 3]  # 3달 이용권
            DP[m] = min(DP[m - 1] + fee_m, fee_t)  # min(1일, 1달, 3달) 누적
    answer = min(DP[12], year)  # min(1년, 나머지) 누적

    # 이용 계획대로 수영장을 이용하는 경우 중 가장 적게 지출하는 비용
    print(f"#{t} {answer}")