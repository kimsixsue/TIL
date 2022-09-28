[Graph](#graph)

1. [Graph](#1-graph)

2. [Depth First Search](#2-depth-first-search)

3. [Breadth First Search](#3-breadth-first-search)

4. [Disjoint-sets](#4-disjoint-sets)

5. [Minimum Spanning Tree](#5-minimum-spanning-tree)

6. [Shortest Path](#6-shortest-path)

# Graph

## 1. Graph

그래프는 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현한다.

그래프는 Vertex 정점들의 집합과 이들을 연결하는 Edge 간선들의 집합으로 구성된 자료구조

- |V| : 정점의 개수, |E| : 그래프에 포함된 간선의 개수
- |V| 개의 정점을 가지는 그래프는 최대 |V| (|V| - 1) / 2 간선이 가능

선형 자료구조나 트리 자료구조로 표현하기 어려운 N : N 관계를 가지는 원소들을 표현하기에 용이하다

**그래프 유형**

- Undirected Graph 무향 그래프
- DIrected Graph 유향 그래프
- Weighted Graph 가중치 그래프
- **D**irected **A**cyclic **G**raph 사이클 없는 방향 그래프
- 완전 그래프
  - 정점들에 대해 가능한 모든 간선들을 가진 그래프
- 부분 그래프
  - 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프

**인접 정점**

- Adjacency 인접
  - 두 개의 정점에 간선이 존재(연결됨)하면 서로 인접해 있다고 한다.
  - 완전 그래프에 속한 임의의 두 정점들은 모두 인접해 있다.

**그래프 경로**

- 경로란 간선들을 순서대로 나열한 것
- 경로 중 한 정점을 최대한 한번만 지나는 경로를 **단순경로**라 한다.
- 시작한 정점에서 끝나는 경로를 **Cycle 사이클**이라고 한다.

**그래프 표현**

- 간선의 정보를 저장하는 방식, 멤리나 성능을 고려해서 결정
- Adjacent matrix 인접 행렬
  - |V| x |V| 크기의 2차원 배열을 이용해서 간선 정보를 저장
  - 배열의 배열(포인터 배열)
- Adjacent List 인접 리스트
  - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
- 간선의 배열
  - 간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장

**인접 행렬**

- 두 정점을 연결하는 간선의 유무를 행렬로 표현
  - |V| x |V| 정방 행렬
  - 행 번호와 열 번호는 그래프의 정점에 대응
  - 두 정점이 인접되어 있으면 1, 그렇지 않으면 0으로 표현
  - 무향 그래프
    - i 번째 행의 합 = i 번째 열의 합 = V_i 의 차수
  - 유향 그래프
    - 행 i 의 합 = V_i 의 진출 차수
    - 열 i 의 합 = V_i 의 진입 차수

**인접 리스트**

- 각 정점에 대한 인접 정점들을 순차적으로 표현
- 하나의 정점에 대한 인접 정점들을 각각 노드로 하는 연결 리스트로 저장

```python
V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬
adjList = [[] for _ in range(V + 1)]  # 인접 리스트
for _ in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1  # undirected
    adjList[n1].append(n2)
    adjList[n2].append(n1)  # undirected
```

## 2. Depth First Search

**그래프 순회(탐색)**

- 그래프 순회는 비선형구조인 그래프로 표현된 모든 자료(정점)를 빠짐없이 탐색하는 것을 의미한다.
- 두 가지 방법
  - **D**epth **F**irst **S**earch 깊이 우선 탐색
  - **B**readth **F**irst **S**earch 너비 우선 탐색

**DFS 깊이우선탐색**

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 고이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

**스택**

- 마지막에 삽입한 자료를 가장 먼저 꺼낸다.

**스택의 구현**

- 연산
  - push : 저장소에 자료를 삽입(저장)한다.
  - pop : 저장소에서 자료를 꺼낸다. (삽입한 자료의 역순)
  - isEmpty : 스택이 공백인지 아닌지를 확인하는 연산
  - peek : 스택의 top에 있는 item 원소를 반환하는 연산
- 스택의 push 알고리즘
  - top은 스택에서 마지막 자료의 위치를 가리킨다.

DFS 알고리즘 - 재귀

```python
DFS_Recursive(G, v)
    visited[v] = True  # v 방문 설정
    for each all w in adjacency(G, v):
        if visited[W] != True:
            DFS_Recursive(G, w)
```

```python
def dfs(i, N, c):
    if c == 3:  # depth 제한
        return
    else:
        visited[i] = 1
        for j in range(1, N + 1):
            if adjM[i][j] and visited == 0:
                dfs(j, N, c + 1)
```

DFS 알고리즘 - 반복

```python
# 갈림길 저장
STACK s  # s : 시작 정점
visited[]
DFS(v)
    push(s, v)
    while not isEmpty(s):
        v = pop(s)
        if not visited[v]:  # 스택에 중복으로 들어가있을 수도 있어서
            visit(v)
            for each w in adjacency(v):
                if not visited[w]:
                    push(s, w)
```

```python
STACK s
visited[]
DFS(v)
    push(s, v)
    visited[v] = True
    while NOT isEmpty(s):
        v = pop(s)
        visit(v)
        for each w in adjacency(v):
            if not visited[w]:
                push(s, w)
                visited[v] = True
```

## 3. Breadth First Search

너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출형태의 자료구조인 큐를 활용함

**큐**

- 선입선출구조
- front = rear = -1

**BFS 알고리즘**

- 입력 파라미터: 그래프 G와 탐색 시작점 v

  ```python
  BFS(G, v)  # 그래프 g, 탐색 시작점 v
      큐 생성
      시작점 v를 큐에 삽입
      점 v를 방문한 것으로 표시
      while 큐가 비어있지 않은 경우:
          t = 큐의 첫번째 원소 반환
          for t와 연결된 모든 선에 대해:
              u = t의 이웃점
              u기 방문되지 않은 곳이면:
                  u를 큐에 넣고, 방문한 것으로 표시
  ```

  ```python
  def bfs2(N, M):
      q = [1]
      v = [0] * (N + 1)
      v[1] = 1
      cnt = 0
      while q:
          t = q.pop(0)
          cnt += 1
          if v[t] <= 2:  # 상원이의 친구면
              for i in range(1, N + 1):
                  if adj[t][i] == 1 and v[i] == 0:
                      q.append(i)
                      v[i] = v[t] + 1
      return cnt - 1
  
  
  def bfs(N):
      q = [1]                  # 큐 생성 + 시작점 enque
      visited = [0] * (N + 1)  # visited 생성
      visited[1] = 1           # 시작점 방문 표시
      while q:                 # 큐가 비어있지 않으면
          t = q.pop(0)
          if visited[t] > 3:
              break
          for i in range(1, N + 1):
              if adj[t][i] == 1 and visited[i] == 0:
                  q.append(i)
                  visited[i] = visited[t] + 1
      cnt = 0
      for i in range(1, N + 1):
          if 1 < visited[i] < 4:
              cnt += 1
      return cnt
  
  
  T = int(input())
  for tc in range(1, T + 1):
      N, M = map(int, input().split())
      adj = [[0] * (N + 1) for _ in range(N + 1)]
      for _ in range(M):
          a, b = map(int, input().split())
          adj[a][b] = 1
          adj[b][a] = 1
      ans = bfs(N)
      print(f'#{tc} {ans}')
  ```

## 4. Disjoint-sets

서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다. 다시 말해 교집합이 없다.

집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다. 이를 representative 대표자라 한다.

상호배타 집합을 표현하는 방법

- 연결 리스트
- 트리

상호배타 집합 연산

- Make-Set( x )
- Find-Set( x )
- Union( x, y )
  - x의 대표 원소를 찾고, y의 대표원소를 찾아서, y의 대표원소를 x의 대표원소로 교체

**상호 배타 집합 표현 - 트리**

- a disjoint set 하나의 집합을 하나의 트리로 표현한다.
- 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 된다.

**상호배타 집합에 대한 연산**

- Make-Set( x ): 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

  ```python
  Make-Set(x):
      p[x] = x
  ```

- Find_set( x ): x를 포함하는 집합을 찾는 연산

  ```python
  Find-Set(x):
      while x != p[x]:
          x = p[x]
      return x
  ```

- Union( x, y ): x와 y를 포함하는 두 집합을 통합하는 연산

  ```python
  Union(x, y):
      p[Find-Set(y)] = Find-Set(x)
  ```



## 5. Minimum Spanning Tree



## 6. Shortest Path

