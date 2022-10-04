def pertmutation(n):
    if n == M:  # length == M
        if number == sorted(number):  # ascend
            print(*number)
        return
    else:
        for i in range(1, N + 1):
            if not checked[i]:
                number[n] = i
                checked[i] = 1
                pertmutation(n + 1)
                checked[i] = 0


N, M = map(int, input().split())
# 1~N, len(permutation)
checked = [0] * (N + 1)
number = [0] * M
pertmutation(0)
