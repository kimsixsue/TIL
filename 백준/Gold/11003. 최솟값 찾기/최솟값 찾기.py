# https://stackoverflow.com/questions/68630/are-tuples-more-efficient-than-lists-in-python
from collections import deque

N, L = map(int, input().split())  # 1 이상
A = list(map(int, input().split()))  # 정수
D = [0] * N  # min
q = deque()  # A_{i-L+1} ~ A_i
for i in range(N):
    while q and q[0][0] < i - L + 1:
        q.popleft()
    while q and A[i] < q[-1][1]:
        q.pop()
    q.append((i, A[i]))  # tuple
    D[i] = q[0][1]
print(*D)
