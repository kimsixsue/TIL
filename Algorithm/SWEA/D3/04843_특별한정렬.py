for testcase in range(1, int(input()) + 1):  # 1 <= 테스트 케이스 개수 <= 50
    N = int(input())  # 10 <= 정수의 개수 <= 100
    ai = list(map(int, input().split()))  # 1 <= N개의 정수 ai <= 100
    count = [0] * 101
    for _ in ai:
        count[_] += 1
    ordered = []
    for n in range(101):
        if count[n]:
            for c in range(count[n]):
                ordered.append(n)  # 여러 개일 경우를 반영해야함
    order = [-1, 0, -2, 1, -3, 2, -4, 3, -5, 4]
    ordered_specially = ''
    for _ in order:  # N개의 정수에 대해 큰 수와 작은 수를 번갈아 특별한 정렬
        ordered_specially += ' ' + str(ordered[_])
    print(f'#{testcase}{ordered_specially}')  # 특별히 정렬된 숫자를 10개까지 출력
