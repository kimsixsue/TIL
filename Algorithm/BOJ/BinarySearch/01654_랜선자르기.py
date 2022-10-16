K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]
left = 1
right = sum(length) // N
while left <= right:
    count = 0
    mid = (left + right) // 2
    for cm in length:
        count += cm // mid
    if count < N:
        right = mid - 1
    else:
        left = mid + 1
print(right)
