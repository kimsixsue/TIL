def subsetsum(i, N):
    global count
    if i == N:
        s = 0  # subsetsum
        for i in range(N):
            if bit[i]:
                s += number[i]
        if s == S and sum(bit):  # bit is not None
            count += 1  # subsetsum == S
    else:
        candidate = [0, 1]
        for x in candidate:
            bit[i] = x
            subsetsum(i + 1, N)


N, S = map(int, input().split())
# len(number), subsetsum
number = list(map(int, input().split()))
bit = [0] * N
count = 0
subsetsum(0, N)
print(count)
