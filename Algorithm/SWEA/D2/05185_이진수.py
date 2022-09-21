import sys

sys.stdin = open('./05185_이진수_sample_input.txt')
convert = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
T = int(input())  # 테스트케이스의 수
for t in range(1, T + 1):
    N, number = input().split()  # 16진수
    N = int(N)  # 자리 수
    binary = ''
    for _ in number:
        binary += convert[_]
    print(f'#{t} {binary}')