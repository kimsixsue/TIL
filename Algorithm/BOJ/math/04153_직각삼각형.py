while True:
    s = input()
    if s == '0 0 0':
        break
    n = sorted(map(int, s.split()))
    if n[0] ** 2 + n[1] ** 2 == n[2] ** 2:
        print('right')
    else:
        print('wrong')
