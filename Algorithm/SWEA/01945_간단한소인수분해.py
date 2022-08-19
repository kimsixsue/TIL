T = int(input())  # 테스트 케이스의 개수
for t in range(1, T + 1):
    N = int(input())  # 2**a * 3**b * 5**c * 7**d * 11**e
    abcde = [2, 3, 5, 7, 11]
    answer = [0] * 5
    while N > 1:  # N이 주어질 때
        for m in range(5):
            if N % abcde[m] == 0:
                N //= abcde[m]
                answer[m] += 1
    print(f'#{t}', *answer)  # a, b, c, d, e 를 출력
