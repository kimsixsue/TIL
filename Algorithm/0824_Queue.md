# Queue 큐

## 큐

**Queue큐의 특성**

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에서는 삽입만하고, 큐의 앞에서는 삭제만 이루어지는 구조
- FIFO : First In First Out(선입선출구조)
  - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 First In 원소는 가장 먼저 삭제 First Out 된다.

#### 큐의 구조 및 기본연산

**큐의 선입선출 구조**

Front 머리 : 저장된 원소 중 첫 번째 원소 (또는 삭제된 위치). 마지막으로 꺼낸 자리

Rear 꼬리 : 저장된 원소 중 마지막 원소. 마지막 저장 위치

**큐의 기본 연산**

- 삽입 : enQueue / append는 느림 `O(1)`
- 삭제 : deQueue / pop(0)는 많이 느림 `O(N)`

#### 큐의 주요 연산

**큐의 사용을 위해 필요한 주요 연산은 다음과 같음**

| 연산          | 기능                                               |
| ------------- | -------------------------------------------------- |
| enQueue(item) | 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산        |
| deQueue()     | 큐의 front 앞쪽에서 원소를 삭제하고 반환하는 연산  |
| createQueue() | 공백 상태의 큐를 생성하는 연산                     |
| isEmpty()     | 큐가 공백상태인지를 확인하는 연산                  |
| isFull()      | 큐가 포화상태인지를 확인하는 연산                  |
| Qpeek()       | 큐의 front 앞쪽에서 원소를 삭제 없이 반환하는 연산 |

#### 큐의 연산 과정

1) 공백 큐 생성 : createQueue(); `Q = [0] * 1000 ; front = -1; rear = -1`
2) 원소 A 삽입 : enQueue(A); `rear += 1; Q[rear] = A`
3) 원소 B 삽입 : enQueue(B); `rear += 1; Q[rear] = B`
4) 원소 반환/삭제 : deQueue(); `front += 1; `
5) 원소 C 삽입 : enQueue(C); `rear += 1; Q[rear] = C`
6) 원소 반환/삭제 : deQueue(); `front += 1;`
7) 원소 반환/삭제 : deQueue(); `front += 1; front == rear`  # 큐가 비어있음.

### 큐의 구현

**선형큐**

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front: 저장된 첫 번째 원소의 인덱스
  - rear: 저장된 마지막 원소의 인덱스
- 상태 표현
  - 초기 상태 : `front = rear = -1`
  - 공백 상태 : `front == rear`
  - 포화 상태 : `rear == n - 1` (n : 배열의 크기, n - 1 : 배열의 마지막 인덱스)

**초기 공백 큐 생성**

- 크기 n인 1차원 배열 생성; `queue = [0] * n`
- front와 rear를 -1로 초기화

**삽입 : enQueue(item)**

- 마지막 원소 뒤에 새로운 원소를 삽입하기 위해

  - rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
  - 그 인덱스에 해당하는 배열원소 `Q[rear]`에 item을 저장

  ``` python
  def enQueue(item) :
      global rear  # 값을 읽는 것 말고도, 바꾸기 위해
      if isFull() : print("Queue_Full")  # 디버깅
      else :  # 구현 부분
          rear <- rear + 1;
          Q[rear] <- item;
  ```

**삭제 : deQueue()**

- 가장 앞에 있는 원소를 삭제하기 위해

  1) `front` 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
  2) 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능함

  ```python
  deQueue()
  	global front
  	if(isEmpty()) then Queue_Empty();  # 디버깅
      else{
          front <- front + 1;
          return Q[front];
      }
  ```

**공백상태 및 포화상태 검사 : isEmpty(), isFull()**

- 공백상태 : `front == rear`
- 포화상태 : `rear == n - 1` (n : 배열의 크기, n - 1 : 배열의 마지막 인덱스)

```python
def isEmpty() :
    return front == rear

def Full() :
    return rear == len(Q) - 1  # N - 1
```

**검색 : Qpeek()**

- 가장 앞에 있는 원소를 검색하여 반환하는 연산
- 현재 front의 한 자리 뒤(`front + 1`)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환

```python
def Qpeek() :
    if isEmpty() : print("Queue_Empty")
    else : return Q[front + 1]
```

## 선형큐

```python
N = 3
q = [0] * N
front = -1
rear = -1

rear += 1        # enqueue(1)
q[rear] = 1

rear += 1        # enqueue(2)
q[rear] = 2

rear += 1        # enqueue(3)
q[rear] = 3

front += 1       # dequeue()
print(q[front])  # 1

front += 1       # dequeue()
print(q[front])  # 2

front += 1       # dequeue()
print(q[front])  # 3
```

### 선형 큐 이용시의 문제점

**잘못된 포화상태 인식**

- 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, `rear = n - 1` 인 상태 즉, 포화상태로 인식하여 더이상의 삽입을 수행하지 않게 됨 `front = 2; rear = 3`

**해결방법 1**

- 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
- 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐 `front = 0; rear = 1`

**해결방법 2**

- 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용.
- 원형 큐의 논리적 구조. `rear[n-1]` 다음을 `rear[0]`으로

## 원형큐

```python
N = 3
q = [0] * N
front = 0
rear = 0

rear = (rear + 1) % N    # enqueue(1)
q[rear] = 1

rear = (rear + 1) % N    # enqueue(2)
q[rear] = 2

rear = (rear + 1) % N    # enqueue(3)
q[rear] = 3

rear = (rear + 1) % N    # enqueue(4)
q[rear] = 4

front = (front + 1) % N  # dequeue()
print(q[front])          # 4

front = (front + 1) % N  # dequeue()
print(q[front])          # 2

front = (front + 1) % N  # dequeue()
print(q[front])          # 3
```

### 원형 큐의 구조

**초기 공백 상태**

- front = rear = 0

**Index의 순환**

- front와 rear의 위치가 배열의 마지막 인덱스인 `n - 1`를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 `0`으로 이동해야 함
- 이를 위해 나머지 연산자 mod를 사용함

**front 변수**

- 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

**삽입 위치 및 삭제 위치**

|        | 삽입 위치               | 삭제 위치                 |
| ------ | ----------------------- | ------------------------- |
| 선형큐 | rear = rear + 1         | front = front + 1         |
| 원형큐 | rear = (rear + 1) mod n | front = (front + 1) mod n |

#### 원형 큐의 연산 과정

1) create Queue; `front = rear = 0;`
2) enQueue(A); `rear = (rear + 1) mod n;`
3) enQueue(B);` rear = (rear + 1) mod n;`
4) deQueue(); `front = (front + 1) mod n;`
5) enQueue(C); `rear = (rear + 1) mod n;`
6) enQueue(D); `rear = (rear + 1) mod n;`  # Queue는 Full, rear 다음이 front

`rear == front` 비어있는 상태, `front == (rear + 1) % N` 가득찬 상태

#### 원형 큐의 구현

**초기 공백 큐 생성**

- 크기 n인 1차원 배열 생성; `Q = [0] * n`
- front와 rear를 0으로 초기화; `front = rear = 0`

**공백상태 및 포화상태 검사 : isEmpty(), isFull()**

- 공백상태 : `front == rear`

- 포화상태 : 삽입할 rear의 다음 위치 == 현재 front

  - (rear + 1) mod n == front

  ```python
  def isEmpty() :
      return front == rear
  
  def isFull() :
      return (rear + 1) % len(cQ) == front
  ```

**삽입 : enQueue(item)**

- 마지막 원소 뒤에 새로운 원소를 삽입하기 위해

  1) rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련함 : rear <- (rear + 1) mod n;
  2) 그 인덱스에 해당하는 배열원소 `cQ[rear]`에 item을 저장

  ```python
  def enQueue(item) :
      global rear
      if isFull() :
          print("Queue_Full")
      else :
          rear = (rear + 1) % len(cQ)
          cQ[rear] = item
  ```

**삭제 : deQueue(), delete()**

- 가장 앞에 있는 원소를 삭제하기 위해

  1) `front` 값을 조정하여 삭제할 자리를 준비함
  2) 새로운 `front` 원소를 리턴 함으로써 삭제와 동일한 기능함

  ```python
  def deQueue() :
      global front
      if isEmpty() :
          print("Queue_Empty")
      else :
          front = (fron + 1) % len(cQ)
          return cQ[front]
  ```

```python
def is Empty() :
    return front == rear

def isFull() :
    return (rear + 1) % len(cQ) == front
```

## Priority Queue 우선순위 큐

**우선순위 큐의 특성**

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.

**우선순위 큐의 적용 분야**

- 시뮬레이션 시스템
- 네트워크 트래픽 제어
- 운영체제의 테스크 스케줄링

**우선순위 큐의 구현**

- 배열을 위한 우선순위 큐
- 동적할당을 이용하는 링크드 리스트를 이용한 우선순위 큐

**우선순위 큐의 기본 연산**

- 삽입 : enQueue
- 삭제 : deQueue

#### 배열을 이용한 우선순위 큐

**배열을 이용하여 우선순위 큐 구현**

- 배열을 이용하여 자료 저장
- 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
- 가장 앞에 최고 우선순위의 원소가 위치하게 됨

**문제점**

- 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생함
- 이에 소요되는 시간이나 메모리 낭비가 큼

## 큐의 활용 : Buffer 버퍼

**버퍼**

- 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다.

**버퍼의 자료 구조**

- 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다.
- 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용된다.

#### 키보드 버퍼

**키보드 버퍼는 아래와 같이 수행된다**

사용자 키보드 입력 `A P S Enter`

키보드 입력 버퍼 `A P S Enter`

키보드 입력 버퍼에 Enter 키 입력이 들어오면

프로그램 실행 영역 `Enter S P A` => 연산

### Revisit to 사탕

**Queue 를 이용하여 사탕 나눠주기 시뮬레이션을 해 보자**

```python
p = 1   # 처음 줄 설 사람 번호

q = []
N = 20  # 초기 사탕 개수
m = 0   # 나눠준 개수
v = 0

while m < N:
    input()  # 엔터를 칠 때마다 화면에 정보를 출력
    q.append((p, 1, 0))  # 처음 줄 서는 사람
    print(q)
    v, c, my = q.pop(0)
    print(f'큐에 있는 사람 수 {len{q)+1}, 현재 일인당 나눠주는 사탕 수{c}, 현재까지 나눠준 사탕 수{m}')
    m += c
    q.append((v, c + 1, my + c))  # 마이쮸를 받고 다시 서는 사람
    p += 1  # 처음 줄서는 사람 번호
print(f'마지막 받은 사람 : {v}')
```

## BFS (Breadth First Search)

**그래프를 탐색하는 방법에는 크게 두 가지가 있음**

- DFS, Depth First Search 깊이 우선 탐색
  - 재귀, 반복. 재귀의 단계, 스택.
    - 경로의 개수는?
- BFS, Breadth First Search 너비 우선 탐색
  - 반복. 큐. 
    - 확산(출발이 여러 곳)

**너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식**

**인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함**

#### BFS 알고리즘

**입력 파라미터 : 그래프 G와 탐색 시작점 v**

```python
def BFS(G, v) :  # 그래프 G, 탐색 시작점 v
    visited = [0] * (n + 1)  # n : 정점의 개수
    queue = []               # 큐 생성
    queue.append(v)          # 시작점 v를 큐에 삽입
    
    while queue :            # 큐가 비어있지 않은 경우
        t = queue.pop(0)     # 큐의 첫번째 원소 반환
        
        if not visited[t] :  # 방문되지 않은 곳이라면
            
            visited[t] = True  # 방문한 것으로 표시
            
            visit(t)           # 정점 t에서 할 일
            for i in G[t] :    # t와 연결된 모든 정점에 대해
                if not visited[i] :  # 방문되지 않은 곳이라면
                    queue.append(i)  # 큐에 넣기
```

```python
def BFS(G, v) :  # 그래프 G, 탐색 시작점 v
    visited = [0] * (n + 1)  # n : 정점의 개수
    queue = []               # 큐 생성
    queue.append(v)          # 시작점 v를 큐에 삽입
    
    visited[v] = 1           # 방문한 것으로 표시
    
    while queue :            # 큐가 비어있지 않은 경우
        t = queue.pop(0)     # 큐의 첫번째 원소 반환
        
        visit(t)               # 정점 t에서 할 일
        for i in G[t] :        # t와 연결된 모든 정점에 대해
            if not visited[i] :   # 방문되지 않은 곳이라면
                queue.append(i)   # 큐에 넣기
                
                visited[i] = visited[t] + 1  # n 으로부터 1만큼 이동
```

#### BFS 예제

**초기 상태**

- Visited 배열 초기화
- Q 생성
- 시작점 `enqueue`

**A점부터 시작**

- `dequeue` : A
- A 방문한 것으로 표시
- A의 인접점 `enqueue`  # B C D

**탐색 진행**

| dequeue     | Visited              | enqueue            | Q         |
| ----------- | -------------------- | ------------------ | --------- |
| dequeue : B | B 방문한 것으로 표시 | B의 인접점 enqueue | C D E F   |
| dequeue : C | C 방문한 것으로 표시 | C의 인접점 enqueue | D E F     |
| dequeue : D | D 방문한 것으로 표시 | D의 인접점 enqueue | E F G H I |
| dequeue : E | E 방문한 것으로 표시 | E의 인접점 enqueue | F G H I   |
| dequeue : F | F 방문한 것으로 표시 | F의 인접점 enqueue | G H I     |
| dequeue : G | G 방문한 것으로 표시 | G의 인접점 enqueue | H I       |
| dequeue : H | H 방문한 것으로 표시 | H의 인접점 enqueue | I         |
| dequeue : I | I 방문한 것으로 표시 | I의 인접점 enqueue |           |

**Q가 비었으므로 탐색 종료**



```python
def bfs(v, N):  # v 시작정점, N 마지막 정점
    visited = [0] * (N + 1)   # visited 생성
    q = list()                # 큐 생성
    q.append(v)               # 시작점 인큐
    visited[v] = 1            # 시작점 처리 표시
    while q:                  # 큐가 비어있지 않으면
        v = q.pop(0)          # 디큐
        print(v)              # visit(v)
        for w in adjList[v]:  # 인접하고 미방문( 인큐되지 않은) 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1


V, E = map(int, input().split())
N = V + 1  # N 정점 개수
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
bfs(0, V)
```

```python
def bfs(v, N, t):  # v 시작, N 마지막 정점번호, t 찾는 정점
    visited = [0] * (N + 1)
    q = list()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:  # visit(v)
            return visited[99]  # 목표 발견
        for w in adjList[v]:  # v에 인접하고 방문안한 w 인큐, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0


T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i * 2], arr[i * 2 + 1]
        adjList[a].append(b)  # 단방향

    print(f'#{tc} {bfs(0, 99, 99)}')  # 시작, 마지막정점, 목표 정점번호
```

```python
def bfs(N):
    visited = [[0] * N for _ in range(N)]
    q = list()
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if (0 <= ni < N) and (0 <= nj < N) and (maze[ni][nj] != 1) and (visited[ni][nj] == 0):
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {bfs(N)}')
```

```python
def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = list()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:  # 3번인가???
            return visited[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if (0 <= ni < N) and (0 <= nj < N) and (maze[ni][nj] != 1) and (visited[ni][nj] == 0):
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return -1


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

    print(f'#{tc} {bfs(sti, stj, N)}')
```

