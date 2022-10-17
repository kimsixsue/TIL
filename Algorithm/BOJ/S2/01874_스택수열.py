n = int(input())  # 1~100000
index = -1
answer = [''] * n * 2
top = -1
stack = [0] * n
count = 0
for _ in range(n):
    number = int(input())  # 1~n 중복 없이
    while count < number:
        index += 1
        answer[index] = '+'  # push
        count += 1
        top += 1
        stack[top] = count
    if stack[top] == number:
        index += 1
        answer[index] = '-'  # pop
        stack[top] = 0
        top -= 1
    else:  # 불가능한 경우
        print("NO")
        break
else:  # 한번에 출력해줘야
    for _ in answer:
        print(_)
