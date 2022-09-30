def calc(dpth, n, plus, mins, prdt, dvid):
    global smal, huge
    if not (-100000000 <= n <= 100000000):
        return  # -100,000,000 <= 연산 중의 값 <= 100,000,000
    elif dpth == N - 1:
        if smal > n:
            smal = n
        if huge < n:
            huge = n
        return
    else:  # 왼쪽에서 오른쪽으로 차례대로 계산
        if plus:
            calc(dpth + 1, n + nums[dpth + 1], plus - 1, mins, prdt, dvid)
        if mins:
            calc(dpth + 1, n - nums[dpth + 1], plus, mins - 1, prdt, dvid)
        if prdt:
            calc(dpth + 1, n * nums[dpth + 1], plus, mins, prdt - 1, dvid)
        if dvid:  # 나눗셈 : // 으로
            calc(dpth + 1, int(n / nums[dpth + 1]), plus, mins, prdt, dvid - 1)


T = int(input())  # 총 테스트 케이스의 개수
for t in range(1, T + 1):
    N = int(input())  # 3<= 숫자의 개수 <=12
    plus, mins, prdt, dvid = map(int, input().split())
    # 연산자 카드(N-1개)를 모두 사용해야 한다
    nums = list(map(int, input().split()))  # 1~9, 숫자 순서 변경 금지
    smal, huge = 100000000, -100000000
    calc(0, nums[0], plus, mins, prdt, dvid)
    # 연산자 카드를 사용하여 만들 수 있는 수식으로 얻은 결과값 중 최댓값과 최솟값의 차이
    print(f'#{t} {huge - smal}')
