N = int(input())  # 1~20 개
price = list(map(int, input().split()))
Y, M = 0, 0
for p in price:
    y = ((p // 30) + 1) * 10
    m = ((p // 60) + 1) * 15
    Y += y
    M += m
if Y < M:
    print('Y', Y)
elif M < Y:
    print('M', M)
else:
    print('Y M', Y)
