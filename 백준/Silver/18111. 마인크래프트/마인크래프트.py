from collections import Counter

N, M, B = map(int, input().split())
height = list()
for _ in range(N):
    height += map(int, input().split())
low, high, total = min(height), max(height), sum(height)
height = dict(Counter(height))  # 좌표는 의미 없으므로
top, small = 0, 64000000  # 500**2 * 256
for z in range(low, high + 1):
    if z * N * M <= total + B:
        time = 0
        for key in height:
            if 0 < z - key:  # 높이들이 기준보다 작다
                time += height[key] * (z - key)  # place
            elif 0 < key - z:  # 높이들이 기준보다 크다
                time += height[key] * (key - z) * 2  # mine
        if small >= time:
            small = time
            top = z
print(small, top)  # 땅 고르기, 최소 시간, 땅의 높이가 가장 높은 것
