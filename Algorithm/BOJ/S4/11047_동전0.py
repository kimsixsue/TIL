N, K = map(int, input().split())
price = [int(input()) for _ in range(N)]
count = 0
for _ in range(N - 1, -1, -1):
    if not K:
        break
    if K >= price[_]:
        count += K // price[_]
        K %= price[_]
print(count)
