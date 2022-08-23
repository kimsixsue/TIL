a, b = map(int, input().split())
# 가위는 1, 바위는 2, 보는 3
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print('B')
elif (a == 2 and b == 1) or (a == 3 and b == 2) or (a == 1 and b == 3):
    print('A')
