def inorder(n):
    global cnt
    if n:
        inorder(left[n])
        cnt += 1
        answer[cnt] = char[n]
        inorder(right[n])


for tcn in range(1, 11):
    N = int(input())
    info = [list(input().split()) for _ in range(N)]
    node = [0] * (N + 1)
    char = [''] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        node[i + 1] = int(info[i][0])
        char[i + 1] = info[i][1]
        if len(info[i]) >= 3:
            left[i + 1] = int(info[i][2])
        if len(info[i]) >= 4:
            right[i + 1] = int(info[i][3])
    cnt = -1
    answer = [''] * N
    inorder(1)
    print(f'#{tcn}', ''.join(answer))
