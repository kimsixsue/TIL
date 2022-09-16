import sys

sys.stdin = open('./05688_세제곱근을찾아라_sample_input.txt')


def is_tres(n):
    for x in range(1, 1000001):

        if x ** 3 > n:  # 세제곱수를 발견 못하고 지나쳤다
            return -1
        elif x ** 3 == n:  # x^3 = n 에 해당하는 숫자 발견
            return x


T = int(input())  # 테스트 케이스의 수
for t in range(1, T + 1):
    N = int(input())

    X = is_tres(N)
    print(f'#{t} {X}')
