N = int(input())
for n in range(N + 1):
    total = temp = n
    while temp:
        total += temp % 10
        temp //= 10
    if total + temp == N:
        print(n)
        break
else:
    print(0)
