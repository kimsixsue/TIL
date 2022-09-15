import sys

sys.stdin = open('05178_sample_input.txt')


def prnt_node(n):
    if n > N:
        return 0
    elif node_value[n]:
        return node_value[n]
    else:
        node_value[n] = prnt_node(n * 2) + prnt_node(n * 2 + 1)
        return node_value[n]


T = int(input())  # 테스트케이스의 수
for t in range(1, T + 1):
    N, M, L = map(int, input().split())  # 노드, 리프, 출력
    leaf = [list(map(int, input().split())) for _ in range(M)]
    node_value = [0] * (N + 1)  # 1번부터 N 번까지
    for leaf, value in leaf:  # 리프 노드 저장 값
        node_value[leaf] = value
    prnt_node(L)
    print(f'#{t} {node_value[L]}')
