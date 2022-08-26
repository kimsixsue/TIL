# 1226. 미로1 `D4`

> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD
>

```python
def bfs(row, col, n):
    visited = [[False] * n for _ in range(n)]
    queue = list()
    queue.append((row, col))
    visited[row][col] = True
    while queue:
        row, col = queue.pop(0)
        if maze[row][col] == '3':  # 3은 도착점을 나타낸다.
            return 1  # 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단
        for delta_row, delta_col in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            next_row, next_col = row + delta_row, col + delta_col
            if (0 <= next_row < n) and (0 <= next_col < n) and (maze[next_row][next_col] != '1') \
                    and not visited[next_row][next_col]:  # 1은 벽을 나타내며 0은 길,
                queue.append((next_row, next_col))
                visited[next_row][next_col] = True
    return 0  # 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).


for _ in range(10):
    tcn = input()

    maze = [input() for _ in range(16)]  # 16*16 행렬의 형태로 만들어진 미로

    start_row, start_col = -1, -1
    for row in range(16):
        for col in range(16):
            if maze[row][col] == '2':  # 2는 출발점,
                start_row, start_col = row, col
                break
        if start_row != -1:
            break

    print(f'#{tcn} {bfs(start_row, start_col, 16)}')
```

![](https://github.com/kimsixsue/TIL/blob/master/Algorithm/SWEA/01226_%EB%AF%B8%EB%A1%9C1/README.assets/01226.png?raw=true)