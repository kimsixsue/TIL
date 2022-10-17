N = int(input())  # len(number)<=100
number = list(map(int, input().split()))  # <=1000
answer = 0
for num in number:
    count = 0
    for n in range(1, num):
        if num % n == 0:
            count += 1
    if count == 1:
        answer += 1
print(answer)
