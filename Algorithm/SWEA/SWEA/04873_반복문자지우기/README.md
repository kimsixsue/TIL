# 4873. 반복문자 지우기 `D2`

> https://swexpertacademy.com/main/learn/course/subjectDetail.do?subjectId=AWOVHzyqqe8DFAWg
>
> 9차시 4일차 - 반복문자 지우기

```python
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
```

![04873](README.assets/04873.png)