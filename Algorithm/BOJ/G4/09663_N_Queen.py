# https://www.acmicpc.net/source/16003379
def back_track(depth):
    count = 0
    if depth == N:
        return 1
    else:
        for n in range(N):
            if depth == 0 and n > (N - 1) // 2:
                break
            if used1[n] or used2[depth + n] or used3[depth + N - n - 1]:
                continue
            used1[n] = used2[depth + n] = used3[depth + N - n - 1] = 1
            if depth == 0 and n < (N - 1) // 2:
                count += back_track(depth + 1) * 2
            elif depth == 0 and n == (N - 1) // 2 and N % 2 == 0:
                count += back_track(depth + 1) * 2
            else:
                count += back_track(depth + 1)
            used1[n] = used2[depth + n] = used3[depth + N - n - 1] = 0
    return count


N = int(input())
used1 = [0] * N
used2 = [0] * (N + N - 1)
used3 = [0] * (N + N - 1)
print(back_track(0))
