M, N = map(int, input().split())
number = [n for n in range(N + 1)]
number[1] = 0
for n in range(2, N // 2 + 1):
    for i in range(n * 2, N + 1, n):
        number[i] = 0
for _ in range(M, N + 1):
    if number[_]:
        print(number[_])
