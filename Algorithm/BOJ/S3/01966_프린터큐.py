from collections import deque

T = int(input())
for _ in range(T):
    # len(priority), # index
    N, M = map(int, input().split())
    priority = deque(enumerate(map(int, input().split())))  # 1 ~ 9
    index = 0
    while priority:
        for i in range(len(priority)):
            if priority[0][1] < priority[i][1]:
                priority.rotate(-1)
                break
        else:
            index += 1
            if priority[0][0] == M:
                print(index)
                break
            priority.popleft()