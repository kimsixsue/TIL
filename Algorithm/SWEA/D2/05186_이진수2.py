import sys

sys.stdin = open('./05186_이진수2_sample_input.txt')
T = int(input())  # 테스트케이스의 수
for t in range(1, T + 1):
    N = float(input())  # 둥둥 점
    compare = 0.0
    temp = 0.0
    binary = ""  # 출력할 이진수 문자열
    for i in range(-1, -14, -1):
        temp = 2 ** i  # (1/2)^자연수
        if N >= compare + temp:
            compare += temp  # 이진수 갱신
            binary += "1"  # 이진수가 1
            if N == compare:  # 완성
                break
        else:
            binary += "0"  # 이진수가 0
    else:  # for-else
        binary = 'overflow'  # 12자리로 불충분
    print(f'#{t} {binary}')
