T = int(input())
for t in range(T):
    score = 0
    count = 0
    s = input()
    for _ in range(len(s) - 1):
        if s[_] == 'O':
            count += 1
        else:
            score += count * (count + 1) // 2
            count = 0
    if s[-1] == 'O':
        count += 1
    score += count * (count + 1) // 2
    print(score)
