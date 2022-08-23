T = int(input())  # 테스크 케이스의 수
for testcase in range(1, T + 1):
    words = [[''] * 15 for _ in range(5)]
    read = [''] * 75
    for r in range(5):  # 다섯 줄
        para = input()  # 1 <= 문자열 길이 <= 15
        for w in range(len(para)):
            words[r][w] = para[w]
    idx = 0
    for col in range(15):
        length = col
        for row in range(5):
            if words[row][col] != '':
                length += 1
            if (row < length) and (words[row][col] != ''):
                read[idx] = words[row][col]
                idx += 1
    print(f'#{testcase}', ''.join(read))
