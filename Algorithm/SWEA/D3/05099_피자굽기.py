import sys

sys.stdin = open('./sample_input.txt')

T = int(input())
for t in range(1, T + 1):

    N, M = map(int, input().split())     # 화덕의 크기 N과 피자의 개수 M
    C = list(map(int, input().split()))  # M개의 피자에 뿌려진 치즈의 양 Ci

    pizza = list()
    for p in range(M):               # enumerate 를 쓰는 것도 좋다
        pizza.append([p + 1, C[p]])  # [ , [피자 번호, 치즈], ]

    oven = [[] for _ in range(N)]
    oven_1 = -1  # 피자는 1번위치에서 넣거나 뺄 수 있다.

    # 화덕 내부의 피자받침은 회전해서 1번에서 치즈를 확인할 수 있다.
    while True:
        oven_1 = (oven_1 + 1) % N
        if oven[oven_1]:           # 화덕을 한 바퀴 돌 때 치즈의 양은 반으로 줄어든다
            oven[oven_1][1] //= 2  # 이전 치즈의 양을 C, 다시 꺼냈을 때 C//2로 줄어든다.
        if oven[oven_1] and oven[oven_1][1] == 0:  # 치즈가 모두 녹아 0이 되면
            oven[oven_1] = []                      # 화덕에서 꺼내고,
        if not oven[oven_1] and pizza:             # 그 자리에 남은 피자를 순서대로 넣는다.
            oven[oven_1] = pizza.pop(0)

        # 마지막 피자 찾기
        if not pizza and [] in oven:
            empty_oven = last_pizza = 0
            for _ in oven:
                if not _:
                    empty_oven += 1
                else:
                    last_pizza = _[0]  # 화덕에 가장 마지막까지 남아있는 피자 번호
            if empty_oven == N - 1:    # 화덕에 피자가 유일할 때
                break

    print(f'#{t}', last_pizza)
