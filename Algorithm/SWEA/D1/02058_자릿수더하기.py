a = int(input())
s = 0
while True:
    s += a % 10
    a //= 10
    if a == 0:
        break
print(s)
