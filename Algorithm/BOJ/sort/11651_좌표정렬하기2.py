N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy.sort(key=lambda xy: (xy[1], xy[0]))
for _ in xy:
    print(*_)
