import sys

sys.stdin = open('./sample_input.txt')

T = int(input())
for t in range(1, T + 1):

    N, M = map(int, input().split())
    natural = list(map(int, input().split()))  # N개의 숫자로 이루어진 수열

    # 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때,
    for _ in range(M):
        natural.append(natural.pop(0))

    print(f'#{t} {natural[0]}')  # 수열의 맨 앞에 있는 숫자
