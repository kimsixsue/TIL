import sys

sys.stdin = open('./input.txt')


def is_possible(m, n, k, sec):
    if 1 < n:  # 손님들이 도착하는 sec 오름차순 정렬
        for end in range(n - 1, 0, -1):
            for start in range(end):
                if sec[start] > sec[start + 1]:
                    sec[start], sec[start + 1] = sec[start + 1], sec[start]
    if sec[0] < m:
        return 'Impossible'
    # 0초부터, m초의 시간을 들이면 k개의 붕어빵을 만들 수 있다.
    # sec 의 index 와 누적 붕어빵 개수 비교 결과에 따라
    for customer_i in range(1, n):
        if (customer_i + 1) > sec[customer_i] // m * k:
            return 'Impossible'
    return 'Possible'


T = int(input())  # 테스트 케이스의 수
for x in range(1, T + 1):
    N, M, K = map(int, input().split())  # 기한 N 초, M 초 당, K 개 붕어빵
    second = list(map(int, input().split()))  # 손님 도착 second 가 N 개
    # 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별
    print(f'#{x} {is_possible(M, N, K, second)}')
