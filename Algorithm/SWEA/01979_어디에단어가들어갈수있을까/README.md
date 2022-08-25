# 1979. 어디에 단어가 들어갈 수 있을까 `D2`

> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq

```python
T = int(input())  # 테스트 케이스의 개수
for testcase in range(1, T + 1):

    N, K = map(int, input().split())  # 5 ≤ 퍼즐 N ≤ 15, 2 ≤ 단어 K ≤ N

    # 전처리로 padding 을 만들어줍니다.
    puzzle = [[0] * (N + 2) for _ in range(N + 2)]  # padding: 1
    for _ in range(1, N + 1):
        puzzle[_][1: N + 1] = list(map(int, input().split()))
    trans = [[0] * (N + 2) for _ in range(N + 2)]  # 전치 행렬
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            trans[row][col] = puzzle[col][row]

    # 1 이 K개만 연속하려면 양 옆이 0 이면 됩니다. 이를 위해 padding 을 만들었습니다.
    want = [0] + [1] * K + [0]  # 흰색 부분은 1, 검은색 부분은 0
    count = 0  # 특정 행이나 열에서 연속해서 1이 K개만 나오면, count += 1

    for row in puzzle[1:-1]:  # 가로
        for cases in range(1, N - K + 2):
            if row[cases - 1: cases + K + 1] == want:
                count += 1
    for row in trans[1:-1]:  # 세로
        for cases in range(1, N - K + 2):
            if row[cases - 1: cases + K + 1] == want:
                count += 1

    print(f'#{testcase} {count}')
```

![01979.png](./01979.png)