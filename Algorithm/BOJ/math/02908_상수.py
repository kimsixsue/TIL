A, B = input().split()
X, Y = int(A[::-1]), int(B[::-1])
if X > Y:
    print(X)
else:
    print(Y)
