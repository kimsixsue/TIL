number = [int(input()) for _ in range(10)]
s = set()
for _ in range(10):
    s.add(number[_] % 42)
print(len(s))
