from collections import deque

N, K = map(int, input().split())
number = deque(range(1, N + 1))
josephus = [0 for _ in range(N)]
for i in range(N):
    number.rotate(-K + 1)
    josephus[i] = number.popleft()
print(f"<{str(josephus).strip('[]')}>")
