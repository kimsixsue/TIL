N, M = map(int, input().split())
card = list(map(int, input().split()))
top = 3
for a in range(N):
    for b in range(N):
        if a != b:
            for c in range(N):
                if a != c and b != c:
                    temp = card[a] + card[b] + card[c]
                    if top < temp <= M:
                        top = temp
print(top)
