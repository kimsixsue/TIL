H, M = map(int, input().split())
if M >= 45:
    M = M - 45
else:
    M = M + 15
    if H > 0:
        H = H - 1
    else:
        H = 23
print(H, M)
