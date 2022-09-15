import sys

sys.stdin = open('./05177_sample_input.txt')


def enq(n):  # 최소 힙
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


T = int(input())  # 테스트케이스의 수
for t in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().split()))
    last = 0
    heap = [0] * (N + 1)
    for _ in number:
        enq(_)
    answer = 0  # 조상 노드에 저장된 정수의 합
    while N:
        N //= 2
        answer += heap[N]
    print(f'#{t} {answer}')
