total = 0
m = 100
for _ in range(7):
    n = int(input())
    if n % 2:
        total += n
        if m > n:
            m = n
if total:
    print(total)
    print(m)
else:
    print(-1)
