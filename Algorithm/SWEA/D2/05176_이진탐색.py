import sys

sys.stdin = open('./05176_sample_input.txt')


def inorder(n):
    global num
    if n <= N:
        inorder(n * 2)
        bst[n] = num
        num += 1
        inorder(n * 2 + 1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())  # N 까지의 자연수
    bst = [0] * (N + 1)
    num = 1
    inorder(num)
    print(f'#{t} {bst[1]} {bst[N // 2]}')
