def quick(n):
    length = len(n)
    if length <= 1:
        return n
    left, right = list(), list()
    pivot = n[length // 2]
    for i in range(length):
        if i == length // 2:
            continue
        if n[i] < pivot:
            left.append(n[i])
        else:  # pivot <= n[i]
            right.append(n[i])
    return quick(left) + [pivot] + quick(right)


T = int(input())  # 1 <= 테스트케이스의 수
for t in range(1, T + 1):
    N = int(input())  # 정수의 개수
    a_i = list(map(int, input().split()))
    print(f'#{t} {quick(a_i)[N // 2]}')
"""
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

"""
