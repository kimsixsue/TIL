T = int(input())  # 테스트 케이스의 수
for testcase in range(1, T + 1):

    bracket = input()  # 쇠막대기와 레이저의 배치를 나타내는 괄호 표현
    length = len(bracket)  # 괄호 문자의 개수 <= 100,000
    i = bar = piece = 0  # index, 쇠막대기 개수, 잘려진 쇠막대기 조각의 총 개수

    while i < length:
        if bracket[i] == '(':
            if bracket[i + 1] == ')':  # '()'
                piece += bar
                i += 2
            else:  # '(('
                bar += 1
                piece += 1
                i += 1
        else:  # ')'
            bar -= 1
            i += 1

    print(f'#{testcase} {piece}')
