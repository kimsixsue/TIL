import sys

input = sys.stdin.readline


def nm(n):
    if n == M:  # length == M
        print(*number)  # 고른 수열은 비내림차순이어야 한다.
        return  # 중복되는 수열을 여러 번 출력하면 안됨
    else:
        for i in range(n+1, N + 1):
            number[n] = i  # 같은 수를 여러 번 골라도 된다
            checked[i] = 1
            nm(n + 1)
            checked[i] = 0


N, M = map(int, input().split())  # 1~N, len(nm)
checked = [0] * (N + 1)
number = [0] * M
nm(0)
