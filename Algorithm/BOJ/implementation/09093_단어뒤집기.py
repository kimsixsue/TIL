import sys

input = sys.stdin.readline
T = int(input())  # test case number
for _ in range(T):
    re = list()
    para = list(input().split())
    for _ in para:
        re.append(_[::-1])
    print(*re)
