while True:
    s = input()
    if s == '.':
        break
    top = -1
    stack = ['' for _ in range(len(s))]
    for c in s:
        if c == '(' or c == '[':
            top += 1
            stack[top] = c
        elif c == ')':
            if stack[top] == '(':
                stack[top] = ''
                top -= 1
            else:
                top += 1
                stack[top] = c
        elif c == ']':
            if stack[top] == '[':
                stack[top] = ''
                top -= 1
            else:
                top += 1
                stack[top] = c
    if top == -1:
        print('yes')
    else:
        print('no')
