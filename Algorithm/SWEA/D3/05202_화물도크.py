import sys

sys.stdin = open('./05202_화물도크_sample_input.txt')

TC = int(input())  # 테스트케이스의 수
for T in range(1, TC + 1):
    N = int(input())  # len(신청서), 시간: 1~24 자연수
    s_e = [list(map(int, input().split())) for _ in range(N)]
    s_e.sort()
    s_e.sort(key=lambda s_e: s_e[1])

    truck = 1
    end = s_e[0][1]
    for _ in range(1, N):
        if s_e[_][0] >= end:  # 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
            truck += 1
            end = s_e[_][1]

    print(f'#{T} {truck}')  # 최대한 많은 화물차
