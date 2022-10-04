N = int(input())
t = 1
for _ in range(N + 1):
    t += 6 * _
    if N <= t:
        print(_ + 1)
        break
