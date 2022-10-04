import sys

input = sys.stdin.readline

N = int(input())
q = [-1] * N
front, rear = -1, -1
for _ in range(N):
    c = input().rstrip()
    if c == 'pop':
        if front == rear:
            print(-1)
        else:
            front += 1
            print(q[front])
    elif c == 'size':
        print(rear - front)
    elif c == 'empty':
        if front == rear:
            print(1)
        else:
            print(0)
    elif c == 'front':
        if front == rear:
            print(-1)
        else:
            print(q[front + 1])
    elif c == 'back':
        if front == rear:
            print(-1)
        else:
            print(q[rear])
    else:
        rear += 1
        q[rear] = c.split()[1]
