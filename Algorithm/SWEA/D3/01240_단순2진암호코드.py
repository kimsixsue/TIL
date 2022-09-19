import sys

sys.stdin = open('./01240_단순2진암호코드_input.txt')
garbage = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


def check_dec(n):
    bit = 0
    check = 0
    test = n
    while test:
        if bit % 2:  # 홀수 자리의 합 x 3
            check += 3 * (test % 10)
        else:  # 짝수 자리의 합 x 3
            check += test % 10
        test //= 10
        bit += 1
    if check % 10:
        return 0  # 암호가 아니다
    else:  # 10의 배수
        bit = 0
        check = 0
        while n:
            check += n % 10
            n //= 10
            bit += 1
        return check  # 자리 합


TCN = int(input())  # 전체 테스트 케이스의 수
for t in range(1, TCN + 1):
    N, M = map(int, input().split())
    rect = [input() for _ in range(N)]
    rect.sort()  # 0이 아닌 곳이 암호코드
    preprocess = str(rect[-1]).rstrip('0')  # 암호코드만
    length = len(preprocess)
    start = length - 56  # 56자리 암호
    preprocess = preprocess[start:]  # 56자리 암호코드
    number = ['' for _ in range(8)]
    password = 0
    for _ in range(8):  # 8등분
        number[_] = preprocess[_ * 7:_ * 7 + 7]
        password += garbage[number[_]] * 10 ** (7 - _)  # 숫자로
    print(f'#{t} {check_dec(password)}')
