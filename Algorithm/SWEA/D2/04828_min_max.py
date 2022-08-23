T = int(input())  # 1 ≤ 테스트 케이스의 수 ≤ 50
for i in range(1, T + 1):
    N = int(input())  # 5 ≤ N ≤ 1000
    ai = list(map(int, input().split()))  # 1 ≤ N개의 ai ≤ 1000000
    big = 0
    small = 1000001
    for positive in ai:
        if big < positive:
            big = positive
        if small > positive:
            small = positive
    print(f'#{i} {big - small}')  # 가장 큰 수와 가장 작은 수의 차이
