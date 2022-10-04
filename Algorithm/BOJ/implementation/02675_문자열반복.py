T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    chars = ''
    for _ in list(S):
        chars += _ * R
    print(chars)
