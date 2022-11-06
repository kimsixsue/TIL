hex_dec = ['A', 'B', 'C', 'D', 'E', 'F']
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


def check_pwd(password):
    odd, even = 0, 0
    for _ in range(8):
        if _ % 2:  # 짝수 자리
            even += password[_]
        else:  # 홀수 자리 * 3
            odd += password[_]
    if (even + 3 * odd) % 10:  # 비정상
        return 0
    else:
        return even + odd


def insert_cut(binary):
    binary = binary.rstrip('0')  # 우측 0 trim
    right = len(binary)
    thickness = check_thickness(binary)
    binary_converted = binary[right - 56 * thickness:]
    already.add((binary_converted, thickness))
    remain = binary[:right - 56 * thickness].rstrip('0')
    if remain:
        insert_cut(remain)
    return binary_converted, thickness


def check_thickness(binary):
    right = len(binary)
    t_right = [1 for _ in range(3)]  # 우측 암호부터 탐색
    t_start = binary[right - 1]
    t_index = 0
    for _ in range(right - 2, right - 47, -1):
        if t_index > 2:
            break
        if t_start == binary[_]:
            t_right[t_index] += 1
        else:
            t_index += 1
        t_start = binary[_]
    t_right.sort()
    thickness = 1
    for d in range(2, t_right[0] + 1):
        for i in range(3):
            if t_right[i] % d:
                break
        thickness = d
    return thickness


def convert_to_pwd(binary_converted, thickness):
    password = ['' for _ in range(8)]
    for _ in range(8):  # 암호
        ch = binary_converted[_ * 7:_ * 7 + 7]
        if thickness == 1:
            password[_] = garbage[ch]
        else:
            temp_b = ''
            ch = binary_converted[_ * 7 * thickness:_ * 7 * thickness + 7 * thickness]
            for group in range(0, 7 * thickness, thickness):
                temp_b += ch[group]
            password[_] = garbage[temp_b]
    return password


T = int(input())  # 전체 테스트 케이스의 수
for C in range(1, T + 1):
    N, M = map(int, input().split())
    rect = [input() for _ in range(N)]
    candi = sorted(set(rect))[1:]  # set 로 만들어버리면 압축이 된다.
    already = set()  # 중복 확인
    answer = 0
    for can in candi:  # 1개씩 추출
        dec = ''  # 2진수로
        for c in can:
            if c.isdigit():
                temp = bin(int(c))[2:]
                length = len(temp)
                temp = (4 - length) * '0' + temp  # 0 채우기
                dec += temp
            else:
                for _ in range(6):
                    if c == hex_dec[_]:
                        temp = bin(int(str(10 + hex_dec.index(c))))[2:]
                        length = len(temp)
                        temp = (4 - length) * '0' + temp  # 0 채우기
                        dec += temp
                        break
        res_chunk = insert_cut(dec)
    count = 0
    for _ in already:
        pwd = convert_to_pwd(*_)
        answer += check_pwd(pwd)
        # C:13, 39 중 35개만 남음
    print(f'#{C} {answer}')
