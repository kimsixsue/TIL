y = {
    3: 'A',
    2: 'B',
    1: 'C',
    0: 'D',
    4: 'E',
}
for _ in range(3):
    t = list(map(int, input().split()))
    print(y[t.count(1)])
