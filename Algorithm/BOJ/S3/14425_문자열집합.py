N, M = map(int, input().split())
S = dict()
for _ in range(N):
    S[input()] = True
answer = 0
for _ in range(M):
    if input() in S:
        answer += 1
print(answer)
