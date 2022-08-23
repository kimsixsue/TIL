T = int(input())  # 1≤ 테스트 케이스 개수 ≤50
for testcase_num in range(1, T + 1):

    # Forth 라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다.
    code = input().split()  # 정수와 연산자가 256자 이내의 연산코드가 주어진다.
    # 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
    answer = 0
    stack = []

    for char in code:
        if char.isdigit():  # 숫자는 스택에 넣는다.
            stack.append(int(char))
        elif char == '.':  # ‘.’은 스택에서 숫자를 꺼내 출력한다.
            answer = stack.pop()
            if len(stack) >= 1:
                answer = 'error'
            break
        else:  # 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
            if len(stack) >= 2:
                right = stack.pop()
                left = stack.pop()
                if char == '*':
                    stack.append(left * right)
                if char == '/':  # 나눗셈의 경우 항상 나누어 떨어진다.
                    stack.append(left // right)
                if char == '+':
                    stack.append(left + right)
                if char == '-':
                    stack.append(left - right)
            else:  # 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
                answer = 'error'
                break

    # #과 1번부터인 테스트케이스 번호, 빈칸에 이어
    print(f'#{testcase_num} {answer}')  # 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
