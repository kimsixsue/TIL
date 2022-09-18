def pertmutation(n):
    if n == M:  # length == M
        if answer == sorted(answer):
            print(*answer)  # ascend
        return
    else:
        for i in range(N):
            if not checked[i]:
                answer[n] = number[i]
                checked[i] = 1
                pertmutation(n + 1)
                checked[i] = 0


N, M = map(int, input().split())
# len(number), len(permutation)
number = list(map(int, input().split()))
number.sort()  # ascend
checked = [0] * N
answer = [0] * M
pertmutation(0)
