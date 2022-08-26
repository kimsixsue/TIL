import sys

sys.stdin = open('./sample_input.txt')

T = int(input())  # 테스트 케이스의 수
for t in range(1, T + 1):

    N, K = map(int, input().split())  # 점수 N개 중, 점수 K개 선택
    score = list(map(int, input().split()))  # 점수 N개

    biggest_total = 0  # 총점 최대값
    # 가장 큰 수가 마지막. 버블 패스는 K번만
    for k in range(K):
        for n in range(N - 1):
            if score[n] > score[n + 1]:
                score[n], score[n + 1] = score[n + 1], score[n]
        biggest_total += score[N - k - 1]

    print(f'#{t} {biggest_total}')
