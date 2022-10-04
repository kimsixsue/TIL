T = int(input())  # len(Test case)
for _ in range(T):
    k = int(input())  # k층
    n = int(input())  # n호
    people = [[0] * n for _ in range(k)]
    for i in range(n):
        people[0][i] = i + 1
    for a in range(1, k):
        for b in range(n):
            people[a][b] = sum(people[a - 1][:b + 1])
    print(sum(people[k - 1][:n]))
