K = int(input())
stack = [0] * K
top = -1
for _ in range(K):
    n = input()
    if n == '0':
        stack[top] = 0
        top -= 1
    else:
        top += 1
        stack[top] = n
print(sum(map(int, stack)))
