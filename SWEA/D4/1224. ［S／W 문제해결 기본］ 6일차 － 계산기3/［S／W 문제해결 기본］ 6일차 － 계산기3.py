def priority(oper):
    if oper == '(':
        return 0
    if oper == '+':
        return 1
    if oper == '*':
        return 2


for testcase_number in range(1, 11):

    length = int(input())  # 길이
    infix = input()  # 문자열로 이루어진 계산식
    infix_index = postfix_index = 0
    top = -1
    stack = [''] * length
    postfix = [''] * length

    while infix_index < length:
        if infix[infix_index].isdigit():
            postfix[postfix_index] = int(infix[infix_index])
            postfix_index += 1
            infix_index += 1
        elif infix[infix_index] == ')':
            while stack[top] != '(' and top > -1:  # pop 출력
                postfix[postfix_index] = stack[top]
                postfix_index += 1
                stack[top] = 0
                top -= 1
            stack[top] = 0  # pop
            top -= 1
            infix_index += 1
        else:
            while True:
                if (top < 0 and infix[infix_index] != '(') or (
                        top > -1 and priority(infix[infix_index]) > priority(stack[top])):
                    top += 1
                    stack[top] = infix[infix_index]
                    infix_index += 1
                    break
                elif top > -1 and infix[infix_index] != '(':
                    postfix[postfix_index] = stack[top]
                    postfix_index += 1
                    stack[top] = 0
                    top -= 1
                else:
                    top += 1
                    stack[top] = infix[infix_index]
                    infix_index += 1
                    break

    while top >= 0:
        postfix[postfix_index] = stack[top]
        postfix_index += 1
        top -= 1

    stack = [0] * length
    top = -1

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

    print(f'#{testcase_number} {stack[0]}')  # 답
