def fib(f):
    fibo = [0 for _ in range(21)]  # 0 ~ 20
    fibo[0] = 0
    fibo[1] = 1
    for _ in range(2, n + 1):
        fibo[_] = fibo[_ - 1] + fibo[_ - 2]
    return fibo[f]


n = int(input())  # 0 ~ 20
print(fib(n))
