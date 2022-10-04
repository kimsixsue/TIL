N = int(input())  # len(array) 1 ~ 50
A = list(map(int, input().split()))  # 0 ~ 100
B = list(map(int, input().split()))  # 0 ~ 100

indexed_b = list(enumerate(B))
indexed_b.sort(key=lambda indexed_b: indexed_b[1], reverse=True)
A.sort()  # A를 재배열해서, S를 최소로 만들자
S = 0  # S = A[0] × B[0] + ... + A[N-1] × B[N-1]
for _ in range(N):
    S += A[_] * indexed_b[_][1]
print(S)