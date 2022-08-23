T = int(input())  # 테스트 케이스 개수
for testcase in range(1, T + 1):
    s = input()  # 길이가 1000이내인 문자열
    stack = [''] * len(s)
    top = -1
    for char in s:
        if stack[top] == char:
            stack[top] = ''
            top -= 1  # 동일하다면 pop
        else:  # push 반복
            top += 1
            stack[top] = char
    print(f'#{testcase} {top + 1}')
