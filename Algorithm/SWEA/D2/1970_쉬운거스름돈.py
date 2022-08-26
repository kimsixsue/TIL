import sys

sys.stdin = open('./input.txt')

T = int(input())  # 테스트 케이스의 개수
for t in range(1, T + 1):
    N = int(input())  # 금액. 10의 배수 and 10이상 1,000,000이하
    how_many = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    for money in how_many:  # 돈의 최소 개수로 각 종류의 돈이 몇 개씩 필요한지 출력
        how_many[money] = N // money
        N %= money
    print(f'#{t}')
    print(*how_many.values())
