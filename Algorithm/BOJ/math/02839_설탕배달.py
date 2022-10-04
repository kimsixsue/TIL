N = int(input())  # 3 ~ 5000
count = [-1 for _ in range(N + 1)]
for _ in range(3, N + 1, 3):
    count[_] = _ // 3
for _ in range(5, N + 1, 5):
    count[_] = _ // 5
    for t in range(3, 15, 3):
        if _ + t <= N:
            if count[_ + t] == -1 or count[_ + t] > count[_] + t // 3:
                count[_ + t] = count[_] + t // 3
print(count[N])
