import bisect

N = int(input())  # len(card)
card = list(map(int, input().split()))
card.sort()
M = int(input())
find = list(map(int, input().split()))
answer = [0] * M
for i in range(M):
    answer[i] = bisect.bisect_right(card, find[i]) - bisect.bisect_left(card, find[i])
print(*answer)
