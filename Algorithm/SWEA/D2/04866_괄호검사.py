check = ['{', '}', '(', ')']
T = int(input())  # 테스트 케이스 개수
for testcase in range(1, T + 1):
    code = input()
    stack = [''] * len(code)
    top = -1
    for char in code:
        if char in check:  # 괄호 {}, ()가 제대로 짝을 이뤘는지 검사
            if (stack[top] == '{' and char == '}') or (stack[top] == '(' and char == ')'):
                stack[top] = ''
                top -= 1
            else:
                top += 1
                stack[top] = char
    if top == -1:
        answer = 1
    else:  # 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
        answer = 0
    print(f'#{testcase} {answer}')
