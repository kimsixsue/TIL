N = int(input())
number = list(map(int, input().split()))
v = int(input())
count = 0
for _ in number:
    if _ == v:
        count += 1
print(count)
