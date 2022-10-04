S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
a = [0 for _ in range(26)]
for _ in range(26):
    a[_] = S.count(alpha[_])
print(*a)
