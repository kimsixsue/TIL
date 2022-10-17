def nm(n):
    if n == M:  # length == M
        print(*number)
        # 중복되는 수열을 여러 번 출력하면 안됨
        return
    else:
        for i in range(1, N + 1):
            # 같은 수를 여러 번 골라도 된다
            number[n] = i
            checked[i] = 1
            nm(n + 1)
            checked[i] = 0


N, M = map(int, input().split())
# 1~N, len(nm)
checked = [0] * (N + 1)
number = [0] * M
nm(0)
