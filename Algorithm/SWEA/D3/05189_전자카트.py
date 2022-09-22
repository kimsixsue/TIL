import sys
from itertools import permutations

sys.stdin = open('./05189_전자카트_sample_input.txt')

T = int(input())  # 테스트케이스의 수
for t in range(1, T + 1):

    best = 9000
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    # 0번: 사무실, 출발지, 목적지
    # 1 ~ N-1: 관리구역, 경로 상 한 번씩만 방문
    # 1 ~ N-1의 permutation

    permute = list(permutations(range(1, N), N - 1))
    for perm in permute:  # source, target 변수 할당하면서 누적한다.

        temp = 0
        source = 0

        for _ in perm:
            target = _
            temp += battery[source][target]
            source = _

        target = 0
        temp += battery[source][target]

        if best > temp:  # 값을 비교해서 작으면 best에 할당
            best = temp
    print(f'#{t} {best}')
