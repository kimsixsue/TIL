## Stack

## 스택

**stack 스택의 특성**

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다.
- 스택에 저장된 자료는 선형 구조를 갖는다.
  - 선형구조: 자료 간의 관계가 1대1의 관계를 갖는다.
  - 비선형구조: 자료 간의 관계가 1대N의 관계를 갖는다.
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출(Last-In-First-Out)이라고 부른다.
  - 예를 들어 스택에 1,2,3 순으로 자료를 삽입한 후 꺼내면 역순으로 즉 3,2,1순으로 꺼낼 수 


#### 스택의 구현

**스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산**

- 자료구조: 자료를 선형으로 저장할 저장소
  - 배열을 사용할 수 있다.
  - 저장소 자체를 스택이라 부르기도 한다.
  - 스택에서 마지막 삽입된 원소의 위치를 `top`이라 부른다.
- 연산
  - 삽입: 저장소에 자료를 저장한다. 보통 `push`라고 부른다.
  - 삭제: 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다. 보통 `pop`이라고 부른다.
  - 스택이 공백인지 아닌지를 확인하는 연산. `isEmpty`
  - 스택의 top에 있는 item(원소)을 반환하는 연산. `peek`

**스택의 삽입/삭제 과정**

- 빈 스택에 원소 A,B,C를 차례로 삽입 후 한번 삭제하는 연산과정

**스택의 `push` 알고리즘**

- `append` 메소드를 통해 리스트의 마지막에 데이터를 삽입

  ```python
  def push(item):
      s.append(item)  # append는 느림
  
      
  top += 1  # push(item)
  stack[top] = item
  ```

**스택의 `pop` 알고리즘**

```python
def pop():
    if len(s) == 0:
        return  # underflow
    else:
        return s.pop(-1)  # s.pop()과 동일
    
if top > -1:  # pop()
    data = stack[top]
    top -= 1
```

#### 스택 구현 고려 사항

**1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어렵다는 단점이 있다.**

**이를 해결하기 위한 방법으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다. 동적 연결리스트를 이용하여 구현하는 방법을 의미한다. 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점을 가진다. 스택의 동적 구현은 생략한다.**

### 스택의 응용1: 괄호검사

**괄호의 종류 : 대괄호 (‘`[`’, ‘`]`’), 중괄호 (‘`{`’, ‘`}`’), 소괄호 (‘`(`’, ‘`)`’)**

**잘못된 괄호 사용의 예**

(a(b)

a(b)c)

a{b(c[d]e}f)

**조건**

1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
3. 괄호 사이에는 포함 관계만 존재한다.

**`스택`을 이용한 괄호 검사**

- `Pop`하여 비교
- **오류!** 괄호 수식이 끝났는데 `스택`에 괄호가 남아 있음

**괄호를 조사하는 알고리즘 개요**

- 문자열에 있는 괄호를 차례대로 조사하면서 여는 괄호를 만나면 스택에 `삽입`하고, 닫는 괄호를 만나면 스택에서 `top` 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지를 검사한다.
- 이 때, `스택`이 비어 있으면 조건 1 또는 조건 2에 위배되고 괄호의 짝이 맞지 않으면 조건 3에 위배된다.
- 마지막 괄호까지를 조사한 후에도 `스택`에 괄호가 남아 있으면, 조건에 위배된다.

### 스택의 응용2: function call

**Function call**

- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
  - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로, 후입선출 구조의 스택을 이용하여 수행순서 관리
  - 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 stack frame에 저장하여 시스템 스택에 삽입
  - 함수의 실행이 끝나면 시스템 스택의 `top` 원소(스택 프레임)를 `pop`(삭제)하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
  - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다. 

## 재귀호출

**자기 자신을 호출하여 순환 수행되는 것**

**함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성**

- 재귀 호출의 예) factorial
  - n에 대한 factorial: 1부터 n까지의 모든 자연수를 곱하여 구하는 연산
  
  ```python
  n! = n * (n - 1)!
  (n - 1)! = (n - 1) * (n - 2)!
  (n - 2)! = (n - 2) * (n - 3)!
  ...
  2! = 2 * 1!
  1! = 1
  ```
  
  - 마지막에 구한 하위 값을 이용하여 상위 값을 구하는 작업을 반복

**0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열을 피보나치라 한다**

- 0, 1, 1, 2, 3, 5, 8, 13, …

**피보나치 수열의 i번 째 값을 계산하는 함수 F를 정의 하면 다음과 같다.**

- F_0 = 0, F_1 = 1
- F_i = `F_i-1` + `F_i-2` for i>=2

**위의 정의로부터 피보나치 수열의 i번째 항을 반환하는 함수를 재귀함수로 구현할 수 있다.**

**피보나치 수를 구하는 재귀함수**

```python
def fibo(n):
    if n < 2:
        return n  # base case와 return
    else:
        return fibo(n - 1) + fibo(n - 2)
```

## Memoization

**앞의 예에서 피보나치 수를 구하는 함수를 재귀함수로 구현한 알고리즘은 문제점이 있다.**

**“엄청난 중복 호출이 존재한다”는 것이다.**

**피보나치 수열의 Call Tree** : O(`2**n`), 중복 호출의 예

**memoization 메모이제이션은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술이다. 동적 계획법의 핵심이 되는 기술이다.**

**앞의 예에서 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면(memoize), 실행시간을 O(n)으로 줄일 수 있다.**

**Memoization 방법을 적용한 알고리즘은 다음과 같다.**

```python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다;
# memo[0]을 0으로 memo[1]는 1로 초기화 한다;

def fibo(n):
    if memo[n] == -1:
        memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


memo = [-1] * 101
memo[0] = 0
memo[1] = 1
for i in range(100):
    print(i, fibo(i))
```

## Dynamic Programming

Dynamic Programming 동적 계획 알고리즘은 그리디 알고리즘과 같이 **최적화 문제**를 해결하는 알고리즘이다.

**동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.**

**피보나치 수 DP 적용**

- 피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 **최적 부분 구조**로 이루어져 있다.

1) **문제를 부분 문제로 분할한다.**
   - Fibonacci(n) 함수는 Fibonacci(n-1)과 Fibonacci(n-2)의 합
   - Fibonacci(n-1) 함수는 Fibonacci(n-2)과 Fibonacci(n-3)의 합
   - Fibonacci(2) 함수는 Fibonacci(1)과 Fibonacci(0)의 합
   - Fibonacci(n)은 Fibonacci(n-1), Fibonacci(n-2), … Fibonacci(2), Fibonacci(1), Fibonacci(0) 의 부분집합으로 나뉜다
2) **부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구한다.**
3) **그 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.**

| 테이블 인덱스 | 저장되어 있는 값 |
| ------------- | ---------------- |
| [0]           | 0                |
| [1]           | 1                |
| [2]           | 1                |
| [3]           | 2                |
| [4]           | 3                |
| …             | …                |
| [n]           | fibo(n)          |

**피보나치 수 DP 적용 알고리즘**

```python
def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return


table = [0] * 101
fibo_dp(100)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {table[N]}')
```

**DP의 구현 방식**

- recursive 방식: fib1(): Memoization - Top-down
- iterative 방식: fib2(): Tabulation - Bottop-up
- memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적이다.
- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문이다.



## DFS 깊이우선탐색

**비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.**

**두 가지 방법**

- Depth First Search 깊이 우선 탐색
- Breadth First Search 너비 우선 탐색

**시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법**

**가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용**

#### DFS 알고리즘

1) **시작 정점 v를 결정하여 방문한다.**

2) **정점 v에 인접한 정점 중에서**
   - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 `push`하고 정점 w를 방문한다. 그리고 w를 v로 하여 `다시 2)를 반복한다.`
   
   - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 `pop`하여 받은 가장 마지막 방문 정점을 v로 하여 `다시 2)를 반복한다.`
   
3) **스택이 공백이 될 때까지 `2)를 반복한다.`**

```python
visited[], stack[] 초기화
DFS(v):
    # 초기화
    시작점 v 방문;
    visited[v] <- true;
    # 반복
    while {
        if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
        	push(v);
        	v <- w;  (w에 방문)
        	visited[w] <- true;
        else
        	if (스택이 비어 있지 않으면)
        		v <- pop(stack);
        	else
        		break
    }
end DFS()
```

#### DFS 예

```python
# A~G -> 0~6
adjList = [[1, 2],     # 0
           [0, 3, 4],  # 1
           [0, 4],     # 2
           [1, 5],     # 3
           [1, 2, 5],  # 4
           [3, 4, 6],  # 5
           [5]]        # 6


def dfs(v, n):
    top = -1
    print(v)           # 방문
    visited[v] = 1     # 시작점 방문 표시
    while True:
        for w in adjList[v]:     # if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1         # push(v);
                stack[top] = v
                v = w            # visited[w] <- true;
                print(v)         # 방문
                visited[w] = 1   # v <- w; (w에 방문)
                break
        else:                    # w가 없으면
            if top != -1:        # 스택이 비어있지 않은 경우
                v = stack[top]   # pop
                top -= 1
            else:                # 스택이 비어있으면
                break            # while


N = 7
visited = [0] * N  # visited 생성
stack = [0] * N    # stack 생성
dfs(0, N)
```

```python
V = 7  # 정점의 개수
# 모든 경로를 받기
edge_list = list(map(int, input().split(', ')))
E = len(edge_list) // 2  # 간선의 개수

# 인접 행렬
# graph = ([0] * (V + 1) ) * (V + 1)
graph = [[0] * (V + 1) for _ in range(V + 1)]
for idx in range(E):
    # graph[시작점][끝점] = 1
    # graph[끝점][시작점] = 1
    frm = edge_list[idx * 2]
    to = edge_list[idx * 2 + 1]
    graph[frm][to] = 1
    graph[to][frm] = 1

visited = [False] * (V + 1)
now = 1
stack = [now]
result = [now]
while stack:
    # 1. 방문 한다.
    visited[now] = 1
    # 2. 인접 정점을 확인한다.
    for nxt in range(V + 1):
        # 3. 인접 정점을 이미 방문했는지 확인한다.
        if graph[now][nxt] == 1 and visited[nxt] == 0:
            # 4. 이동한다.
            # 4-1. 이전 경로를 stack 넣는다.
            stack.append(now)
            # 4-2. 방문 정점을 변경한다.
            now = nxt
            result.append(nxt)  # 방문정점을 추가
            break
    else:  # 모든 정점이 방문되었다면 stack에서 pop
        now = stack.pop()

print('-'.join(map(str, result)))
```

```python
def DFS(now):
    # 1. 방문표시
    visited[now] = 1
    result.append(now)  # 방문 경로 체크
    # 2. 인접 정점 확인
    for nxt in range(V + 1):
        if graph[now][nxt] == 1 and visited[nxt] == 0:
            # 3. 이동가능하다면 이동
            DFS(nxt)


V = 7  # 정점의 개수
# 모든 경로를 받기
edge_list = list(map(int, input().split(', ')))
E = len(edge_list) // 2  # 간선의 개수

# 인접 행렬
# graph = ([0] * (V + 1) ) * (V + 1)
graph = [[0] * (V + 1) for _ in range(V + 1)]
for idx in range(E):
    # graph[시작점][끝점] = 1
    # graph[끝점][시작점] = 1
    frm = edge_list[idx * 2]
    to = edge_list[idx * 2 + 1]
    graph[frm][to] = 1
    graph[to][frm] = 1

visited = [False] * (V + 1)
result = []
DFS(1)

print('-'.join(map(str, result)))
```

```python
def dfs(i, j, N):
    global answer
    if maze[i][j] == 3:
        answer += 1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 벽으로 둘러쌓인 미로
                dfs(ni, nj, N)
        visited[i][j] = 0
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # '2'
                sti, stj = i, j
                break
        if sti != -1:
            break
    answer = 0  # 경로의 수
    visited = [[0] * N for _ in range(N)]
    dfs(sti, stj, N)
    print(answer)
```

```python
def dfs(i, j, s, N):
    global minV
    if maze[i][j] == 3:
        if minV > s + 1:
            minV = s + 1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 벽으로 둘러쌓인 미로
                dfs(ni, nj, s + 1, N)
        visited[i][j] = 0
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # '2'
                sti, stj = i, j
                break
        if sti != -1:
            break
    answer = 0  # 경로의 수
    minV = N * N
    visited = [[0] * N for _ in range(N)]
    dfs(sti, stj, 0, N)
    if minV == N * N:
        minV = -1
    print(f'#{tc} {minV}')
```

