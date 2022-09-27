def merge_sort(a):
    if len(a) <= 1:
        return a
    n = len(a) // 2
    left = a[:n]  # L[0:N//2]
    right = a[n:]  # L[N//2:N]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    global count  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
    if right[-1] < left[-1]:
        count += 1  # 오른쪽 원소가 먼저 복사되는 경우의 수
    index, i_left, i_right = 0, 0, 0
    len_l, len_r = len(left), len(right)
    result = [0 for _ in range(len_l + len_r)]
    while i_left < len_l or i_right < len_r:
        if i_left < len_l and i_right < len_r:
            if left[i_left] <= right[i_right]:
                result[index] = left[i_left]
                i_left += 1
                index += 1
            else:
                result[index] = right[i_right]
                i_right += 1
                index += 1
        elif i_left < len_l:
            result[index] = left[i_left]
            i_left += 1
            index += 1
        elif i_right < len_r:
            result[index] = right[i_right]
            i_right += 1
            index += 1
    return result


T = int(input())  # 1 <= 테스트케이스의 수
for t in range(1, T + 1):
    N = int(input())  # 5 <= len(a_i)
    a_i = list(map(int, input().split()))  # 0 <= 정수
    count = 0
    L = merge_sort(a_i)
    print(f'#{t} {L[N // 2]} {count}')
"""
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

"""
