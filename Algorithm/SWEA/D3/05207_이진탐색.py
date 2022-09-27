def binary_search(n, s, key):
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if s[m] == key:
            return m
        elif s[m] < key:
            pattern.append('r')
            l = m + 1
        else:  # key < s[m]
            pattern.append('l')
            r = m - 1
    return -1


T = int(input())  # 1 <= 테스트케이스의 수
for t in range(1, T + 1):
    N, M = map(int, input().split())  # len(A), len(B)
    # 서로 다른 정수 N개가 주어지면, 정렬한 상태로 리스트 A에 저장
    A = sorted(list(map(int, input().split())))  # N == len(A)
    B = list(map(int, input().split()))  # M == len(B)
    count = 0
    # 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인
    for b in B:
        pattern = list()
        index = binary_search(N, A, b)
        # B에 속한 어떤 수가 A에 들어있으면서,
        # 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수
        if -1 < index:
            if len(pattern) <= 1:
                count += 1
            else:  # 2 <= len(pattern)
                for lr in range(len(pattern) - 1):
                    if pattern[lr] == 'l' and pattern[lr + 1] == 'l':
                        break
                    if pattern[lr] == 'r' and pattern[lr + 1] == 'r':
                        break
                else:
                    count += 1
    print(f'#{t} {count}')
"""
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5

"""
