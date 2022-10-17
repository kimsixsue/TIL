N = int(input())
member = [''] * N
for _ in range(N):
    a, n = input().split()
    age, name = int(a), n
    member[_] = (age, name)
for _ in sorted(member, key=lambda a: a[0]):
    print(*_)
