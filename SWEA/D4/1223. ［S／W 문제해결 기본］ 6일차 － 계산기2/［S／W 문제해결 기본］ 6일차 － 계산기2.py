for testcase_number in range(1, 11):  # 총 10개의 테스트 케이스
    length = int(input())  # 테스트 케이스의 길이
    infix = input()  # 문자열 계산식을 구성하는 연산자는 +, * 이며 피연산자인 숫자는 0 ~ 9의 정수만
    infix_index = postfix_index = 0
    top = -1
    stack = [''] * length
    postfix = [''] * length
    # 문자열로 된 계산식을 후위 표기식으로 바꾸면
    while infix_index < length:
        if infix[infix_index] != '+' and infix[infix_index] != '*':
            postfix[postfix_index] = int(infix[infix_index])
            postfix_index += 1
            infix_index += 1
        else:
            while True:
                if infix[infix_index] == '*' and stack[top] == '+' or top < 0:
                    top += 1
                    stack[top] = infix[infix_index]
                    infix_index += 1
                    break
                else:
                    postfix[postfix_index] = stack[top]
                    postfix_index += 1
                    stack[top] = 0
                    top -= 1
    while top >= 0:
        postfix[postfix_index] = stack[top]
        postfix_index += 1
        top -= 1
    stack = [0] * length
    top = -1
    # 변환된 식을 계산
    for token_index in range(length):
        if postfix[token_index] != '+' and postfix[token_index] != '*':
            top += 1
            stack[top] = postfix[token_index]
        else:
            if postfix[token_index] == '*':
                stack[top - 1] *= stack[top]
                stack[top] = 0
            else:
                stack[top - 1] += stack[top]
                stack[top] = 0
            top -= 1
    print(f'#{testcase_number} {stack[top]}')  # 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
