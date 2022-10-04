T = int(input())
for _ in range(T):
    s = input()
    stack = [''] * len(s)
    top = -1
    for c in s:
        if c == '(':
            top += 1
            stack[top] = c
        elif c == ')':
            if top == -1:
                break
            stack[top] = ''
            top -= 1
    else:
        if top == -1:
            print('YES')
            continue
        else:
            print('NO')
            continue
    print('NO')
