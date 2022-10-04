A, B = map(int, input().split())
number = list(range(min(A, B) + 1, max(A, B)))
print(len(number))
print(*number)
