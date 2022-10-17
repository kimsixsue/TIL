import sys

open = sys.stdin.readline
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
for _ in sorted(xy, key=lambda xy: (xy[0], xy[1])):
    print(*_)
