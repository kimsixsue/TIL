T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H:
        Y = N % H
        XX = N // H + 1
    else:
        Y = H
        XX = N // H
    if XX <= 9:
        print(str(Y) + '0' + str(XX))
    else:
        print(str(Y) + str(XX))
