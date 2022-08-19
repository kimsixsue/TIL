N = int(input())
numbers = ''
for i in range(1, N + 1):
    if N % i == 0:
        numbers += str(i) + ' '
print(numbers)
