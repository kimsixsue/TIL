T = int(input())  # 테스트 케이스의 수
for testcase in range(1, T + 1):
    N = int(input())  # len(price_of_day) = 2 ≤ N ≤ 1,000,000
    price_of_day = list(map(int, input().split()))  # 각 날의 매매가 <= 10000
    sale_idx = [0] * 10001  # benefit = sum ( (해당 idx) * (해당 idx 에 누적된 이익) )
    min_price = 10001
    max_benefit = max_price = 0
    point = price_of_day[N - 1]
    for day in range(N - 1, -1, -1):  # idx 범위 N
        if min_price > price_of_day[day]:
            min_price = price_of_day[day]
        if max_price < price_of_day[day]:
            max_price = price_of_day[day]
        if price_of_day[day] < point:
            sale_idx[point] += point - price_of_day[day]
        elif price_of_day[day] > point:
            point = price_of_day[day]
    for trade in range(max_price, min_price - 1, - 1):
        max_benefit += sale_idx[trade]
    print(f'#{testcase} {max_benefit}')
