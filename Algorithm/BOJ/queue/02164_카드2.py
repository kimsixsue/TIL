from collections import deque

N = int(input())
card = deque(range(1, N + 1))
while True:
    if len(card) == 1:
        break
    card.popleft()
    if len(card) == 1:
        break
    card.rotate(-1)
print(card[0])
