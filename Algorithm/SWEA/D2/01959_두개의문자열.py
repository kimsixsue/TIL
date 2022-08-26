import sys

sys.stdin = open('./input.txt')

T = int(input())  # 테스트 케이스의 개수
for t in range(1, T + 1):
    N, M = map(int, input().split())  # N 과 M은 3 이상 20 이하이다.
    A_i = list(map(int, input().split()))  # N = len[A_i]
    B_j = list(map(int, input().split()))  # M = len[B_j]
    # Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
    # 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
    biggest = -200
    if N < M:  # A_i가 B_j보다 짧을 때
        for case in range(M - N + 1):  # 경우의 수
            total = 0
            for count in range(N):  # A_i가 이동
                total += A_i[count] * B_j[case + count]
            if biggest < total:
                biggest = total
    elif N > M:  # A_i가 B_J보다 길 떄
        for case in range(N - M + 1):  # 경우의 수
            total = 0
            for count in range(M):  # B_j가 이동
                total += A_i[case + count] * B_j[count]
            if biggest < total:
                biggest = total
    else:  # 한 가지만
        for _ in range(N):
            biggest += A_i[_] * B_j[_]
    print(f'#{t} {biggest}')  # 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값
