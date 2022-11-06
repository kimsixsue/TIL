def cal(node):
    global result
    if not tree[node][0] in oper:
        return tree[node][0]
    else:
        left = cal(tree[node][1])
        right = cal(tree[node][2])
        if tree[node][0] == '+':
            result = left + right
        elif tree[node][0] == '-':
            result = left - right
        elif tree[node][0] == '*':
            result = left * right
        elif tree[node][0] == '/':
            result = left // right
        return result


oper = ['+', '-', '*', '/']
for tc in range(1, 11):
    N = int(input())
    tree = [[[] for _ in range(3)] for _ in range(N + 1)]
    for i in range(N):
        node_info = input().split()
        node_num = int(node_info[0])
        node_data = node_info[1]
        if node_data not in oper:
            tree[node_num][0] = int(node_data)
        else:
            tree[node_num][0] = node_data
        if len(node_info) == 4:
            tree[node_num][1] = int(node_info[2])
            tree[node_num][2] = int(node_info[3])
    result = 0
    cal(1)
    print(f'#{tc} {result}')
