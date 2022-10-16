from collections import Counter

N, M = map(int, input().split())
height = Counter(map(int, input().split()))
left, right = 0, max(height)
answer = 0
while left <= right:
    total = 0
    mid = (left + right) // 2
    for h, cnt in height.items():
        if 0 < h - mid:
            total += cnt * (h - mid)
    if total < M:
        right = mid - 1
    else:
        left = mid + 1
        answer = mid
print(answer)
