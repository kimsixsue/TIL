A, B, V = map(int, input().split())
boundary = V - A
x = boundary // (A - B)
y = bool(boundary % (A - B))
day = x + y + 1
print(day)
