for testcase in range(1, 11):  # 테스트 케이스 10개
    length, num_str = input().split()  # 10 ≤ 0~9로 구성된 문자열 길이 ≤ 100
    N = int(length)
    password = [''] * N  # len(비밀번호) < N
    top = -1
    while True:
        for n in num_str:
            if n == password[top]:
                password[top] = ''
                top -= 1
            else:
                top += 1
                password[top] = n
        print(f'#{testcase}', ''.join(password))
        break
