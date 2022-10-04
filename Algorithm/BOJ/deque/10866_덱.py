import sys
from collections import deque

input = sys.stdin.readline

deq = deque()
N = int(input())
for _ in range(N):
    c = input().rstrip()
    length = len(deq)
    if c == 'back':
        if length:
            print(deq[-1])
        else:
            print(-1)
    elif c == 'front':
        if length:
            print(deq[0])
        else:
            print(-1)
    elif c == 'empty':
        if length:
            print(0)
        else:
            print(1)
    elif c == 'size':
        print(length)
    elif c == 'pop_back':
        if length:
            print(deq.pop())
        else:
            print(-1)
    elif c == 'pop_front':
        if length:
            print(deq.popleft())
        else:
            print(-1)
    else:
        push = c.split()
        X = push[1]
        if push[0] == 'push_front':
            deq.insert(0, X)
        else:
            deq.append(X)
