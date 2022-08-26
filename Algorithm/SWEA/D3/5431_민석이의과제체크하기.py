import sys

sys.stdin = open('./sample_input.txt')

T = int(input())  # 테스트 케이스의 수
for testcase in range(1, T + 1):

    # 수강생의 수를 나타내는 정수 N(2≤N≤100)
    N, K = map(int, input().split())
    # 과제를 제출한 수강생의 번호 K개
    submit = list(map(int, input().split()))

    number = list()  # 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력
    for lazy in range(1, N + 1):
        if lazy not in submit:
            number.append(lazy)

    print(f'#{testcase}', *number)
