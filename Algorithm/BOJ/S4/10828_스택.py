import sys

input = sys.stdin.readline

N = int(input())  # 1 <= 명령의 수
stack = [-1] * N
top = -1
for _ in range(N):
    command = input().rstrip()
    if command == 'size':
        print(top + 1)
    elif command == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
    elif command == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            stack[top] = -1
            top -= 1
    else:
        top += 1
        stack[top] = command.split()[1]
