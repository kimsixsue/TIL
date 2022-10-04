x, y, w, h = map(int, input().split())
left = x
down = y
right = abs(x - w)
up = abs(y - h)
print(min(left, right, down, up))
