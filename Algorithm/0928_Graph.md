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
adjList = [[] for _ in range(V + 1)]          # 인접 리스트
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1        # undirected
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
def dfs_recursive(g, v):
    visited[v] = True  # v 방문 설정
    for each all w in adjacency(g, v):
        if visited[W] is False:
            dfs_recursive(g, w)
```

```python
def dfs(i, n, c):
    if c == 3:  # depth 제한
        return
    else:
        visited[i] = True
        path.append(i)
        for j in range(1, n + 1):
            if adjM[i][j] and visited[j] is False:
                dfs(j, n, c + 1)
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
  def bfs(g, v):  # 그래프 g, 탐색 시작점 v
      queue = list()
      queue.append(v)
      visited[v] = True
      while queue:
          t = queue.pop(0)
          for t와 연결된 모든 선에 대해:
              u = t의 이웃점
              visited[u] is False:
                  queue.append(u)
                  visited(u) = True
  ```
  
  ```python
  def bfs(n):
      q = [1]                  # 큐 생성 + 시작점 enque
      visited = [0] * (n + 1)  # visited 생성
      visited[1] = 1           # 시작점 방문 표시
      while q:                 # 큐가 비어있지 않으면
          t = q.pop(0)
          if visited[t] > 3:
              break
          for i in range(1, n + 1):
              if adj[t][i] == 1 and visited[i] == 0:
                  q.append(i)
                  visited[i] = visited[t] + 1
      cnt = 0
      for i in range(1, n + 1):
          if 1 < visited[i] < 4:
              cnt += 1
      return cnt
  
  
  def bfs2(n):
      q = [1]
      v = [0] * (n + 1)
      v[1] = 1
      cnt = 0
      while q:
          t = q.pop(0)
          cnt += 1
          if v[t] <= 2:  # 상원이의 친구면
              for i in range(1, n + 1):
                  if adj[t][i] == 1 and v[i] == 0:
                      q.append(i)
                      v[i] = v[t] + 1
      return cnt - 1
  
  
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
  def make_set(x):
      p[x] = x
  ```

- Find_set( x ): x를 포함하는 집합을 찾는 연산

  ```python
  def find_set(x):
      while x != p[x]:
          x = p[x]
      return x
  ```

- Union( x, y ): x와 y를 포함하는 두 집합을 통합하는 연산

  ```python
  def union(x, y):  # y의 대표원소를 x의 대표원소로 교체
      p[find_set(y)] = find_set(x)
  ```

- 연산의 효율을 높이는 방법
  - Rank를 이용한 Union
    - 각 노드는 자신을 루트로 하는 subtree의 높이를 Rank 랭크라는 이름으로 저장한다
    - 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다
  - Path compression
    - Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 준다

## 5. Minimum Spanning Tree

그래프에서 최소 비용 문제

1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
2. 두 정점 사이의 최소 비용의 경로 찾기

신장 트리

- n 개의 정점으로 이루어진 무방향 그래프에서 n 개의 정점과 n - 1 개의 간선으로 이루어진 트리

**M**inimum **S**panning **T**ree 최소 신장 트리

- 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

**MST 표현**

- 그래프

- 간선들의 배열

- 인접 리스트

- 부모 자식 관계와 가중치에 대한 배열

  - 트리

    ```python
    V, E = map(int, input().split())
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    adjL = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w
        adjM[v][u] = w  # 가중치가 있는 무방향 그래프
        adjL[u].append((v, w))
        adjL[v].append((u, w))
    ```

**Prim 알고리즘**

- 하나의 정점에서 연결된 간선들 중에서 하나씩 선택하면서 MST를 만들어 가는 방식
  1. 임의 정점을 하나 선택해서 시작
  2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
  3. 모든 정점이 선택될 때 까지 1), 2) 과정을 반복

- 2 disjoint-sets 서로소인 2개의 집합 정보를 유지

  - tree vertices 트리 정점들 - MST를 만들기 위해 선택된 정점들

  - nontree vertices 비트리 정점들 - 선택 되지 않은 정점들

- 알고리즘

  ```python
  def mst_prim(g, r):                            # g : 그래프, r : 시작 정점
      for u in g.v:
          u.key = 큰숫자                          # u.key : u에 연결된 간선 중 최소 가중치
          u.p = None                             # u.p : 트리에서 u의 부모
  
      r.key = 0
      q = g.v                                    # 우선순위 q에 모든 정점 넣는다.
  
      while q != 0:                              # 빈 q가 아닐 동안 반복
          u = extract_min(q)                     # key 값이 가장 작은 정점 가져오기
  
          for v in g.adj[u]:                     # u의 인접 정점들
              if (v in q) and (w(u, v) < v.key): # q에 있는 v의 key값 갱신
                  v.p = u
                  v.key = w(u, v)
  ```

  ```python
  def prim1(r, v):
      mst = [0] * (v + 1)      # mst 포함 여부
      key = [10000] * (v + 1)  # 가중치의 최대값 이상으로 초기화. key[v]는 v가 mst 에 속한 정점과 연결될 때의 가중치
      key[r] = 0               # 시작정점의 key
      for _ in range(v):       # v + 1 개의 정점 중 v개를 선택
          # mst에 포함되지 않은 정점 중(mst[u]==0), key가 최소인 u 찾기
          u = 0
          min_V = 10000
          for i in range(v + 1):
              if mst[i] == 0 and key[i] < min_v:
                  u = i
                  min_v = key[i]
          mst[u] = 1  # 정점 u를 mst에 추가
          # u에 인접인 v에 대해, mst에 포함되지 않은 정점이면
          for v in range(v + 1):
              if mst[v] == 0 and adj_m[u][v] > 0:
                  key[v] = min(key[v], adj_m[u][v])  # u를 통해 mst 에 포함되는 비용과 기존 비용을 비교, 갱신
      return sum(key)  # mst 가중치의 합
  
  
  def prim2(r, v):
      mst = [0] * (v + 1)  # mst 포함 여부
      mst[r] = 1           # 시작정점 표시
      s = 0                # mst 간선의 가중치 합
      for _ in range(V):
          u = 0
          min_v = 10000
          for i in range(v + 1):  # mst 에 포함된 정점i 와 인접한 정점j 중 mst 에 포함되지 않고 가중치가 최소인 정점 u찾기
              if mst[i] == 1:
                  for j in range(V + 1):
                      if mst[j] == 0 and 0 < adj_m[i][j] < min_v:
                          u = j
                          min_v = adj_m[i][j]
          s += min_v
          mst[u] = 1
      return s
      
      
  V, E = map(int, input().split())
  adj_m = [[0] * (V + 1) for _ in range(V + 1)]
  adj_l = [[] for _ in range(V + 1)]
  for _ in range(E):
      u, v, w = map(int, input().split())
      adj_m[u][v] = w
      adj_m[v][u] = w  # 가중치가 있는 무방향 그래프
      adj_l[u].append((v, w))
      adj_l[v].append((u, w))
  print(adj_m)
  print(adj_l)
  # print(prim1(0, V))
  print(prim2(0, V))
  ```

**KRUSKAL 알고리즘**

- 간선을 하나씩 선택해서 MST 를 찾는 알고리즘
  1) 최초, 모든 간선을 가중치에 따라 **오름차순**으로 정렬
  2) 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
     - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
  3) n-1 개의 간선이 선택될 때 까지 2)를 반복

- 알고리즘

  ```python
  def mst_kruskal(g, w):
      a = 0              # 0: 공집합
      for vertex in g.v  # g.v: 그래프의 정점 집합
      	make_set(v)    # g.e: 그래프의 간선 집합
          
      g.e에 포함된 edge.sort(key=lambda edge: edge[가중치 w])
      
      for 가중치가 가장 낮은 간선 (u, v) in g.e 선택(n-1개):
          if find_set(u) != find_set(v):
              a.append({(u, v)})
              p[find_set(v)] = find_set(u)
              
      return a
  ```

  ```python
  def find_set(x):
      while x != rep[x]:  # 대표원소가 아니면
          x = rep[x]      # x가 가리키는 정점으로 이동
      return x
  
  
  V, E = map(int, input().split())  # V 마지막 정점, 0~V번 정점. 개수 (V+1)개
  edge = []
  for _ in range(E):
      u, v, w = map(int, input().split())
      edge.append([u, v, w])
  edge.sort(key=lambda x: x[2])     # 가중치 기준 오름차순 정렬
  rep = [i for i in range(V + 1)]  # 대표원소 초기화
  # N개의 정점이 있으면 사이클이 생기지 않도록 N-1개의 간선을 선택
  # MST 에 포함된 간선의 가중치의 합 구하기
  N = V + 1  # 실제 정점 수, 0~V번 까지의 정점
  cnt = 0    # 선택한 edge의 수
  total = 0  # MST 가중치의 합
  for u, v, w in edge:  # N-1개의 간선 선택 루프
      if find_set(u) != find_set(v):  # 사이클을 형성하지 않으면 선택
          cnt += 1
          total += w  # 가중치의 합
          # union(u, v) 와 동일
          rep[find_set(v)] = find_set(u)  # v의 대표원소를 u의 대표원소로 바꿈
          if cnt == N - 1:  # 간선 수
              break
  print(total)
  ```

## 6. Shortest Path

- 최단 경로 정의
  - 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
- 하나의 시작 정점에서 끝 정점까지의 최단경로
  - dijkstra 다익스트라 알고리즘
    - 음의 가중치를 허용하지 않음
  - Bellman-Ford 벨만-포드 알고리즘
    - 음의 가중치 허용
- 모든 정점들에 대한 최단 경로
  - Floyed-Warshall 플로이드-워샬 알고리즘

**Dijkstra 알고리즘**

- 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식이다.
- s 시작정점에서 t 끝정점 까지의 최단 경로에 정점 x가 존재한다.
- 이때, 최단경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로 구성된다.
- 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사하다.

- 알고리즘

  ```python
  # s: 시작 정점, a: 인접 행렬, d: 거리
  # v: 정점 집합, u: 선택된 정점 집합
  
  def dijkstra(s, a, d):
      u = {s}  # 비용 결정된 정점들
      
      for 모든 정점 v:
          d[v] = a[s][v]  # 시작점 s에서 v에 도착하는 최소비용
      
      while u != v:
          d[w]가 min인 정점 w not in u 를 선택
          u.append(w)
          
          for w에 인접한 모든 정점 v:
              d[v] = min(d[v], d[w] + a[w][v])  # w를 거쳐서 v로 가는 비용
  ```

  ```python
  def dijkstra(n, x):
      for i in range(n + 1):
          d[i] = adj[x][i]
      u = [x]
      for _ in range(n - 1):  # n개의 정점 중 출발을 제외한 정점 선택
          w = 0
          for i in range(1, n + 1):
              if (i not in u) and (d[i] < d[w]):  # 남는 노드 중 비용이 최소인 w
                  w = i
          u.append(w)
          for v in range(1, n + 1):      # 정점 v가
              if 0 < adj[w][v] < 10000:  # w에 인접이면
                  d[v] = min(d[v], d[w] + adj[w][v])
      
  
  T = int(input())
  for tc in range(1, T + 1):
      N, M, X = map(int, input().split())
      adj = [[10000] * (N + 1) for _ in range(N + 1)]
      for i in range(N + 1):
          adj[i][i] = 0
      for _ in range(M):
          x, y, c = map(int, input().split())
          adj[x][y] = c
      d = [0] * (N + 1)
      dijkstra(N, X)
      print(d)
  ```

  ```python
  def dijkstra(s, v):       # 시작정점 s, 마지막 정점 v
      u = [0] * (v + 1)
      u[s] = 1
      for _ in range(v + 1):
          d[_] = adj[s][_]  # 시작 점에서 갈 수 있는 값
      # while len(U) != v:
      for _ in range(v):    # v = 정점개수-1과 같으므로..남은 정점개수와 같음
          min_v = inf
          w = 0
          for i in range(v + 1):
              if u[i] == 0 and min_v > d[i]:
                  min_v = d[i]
                  w = i
          u[w] = 1                     # 선택된 집합에 포함
          for _ in range(v + 1):       # 정점 v가
              if 0 < adj[w][_] < inf:  # w에 인접이면 , 시작정점에서 w를 거쳐 v로 가능 비용과
                  d[_] = min(d[_], d[w] + adj[w][_])  # 시작정점에서 v로 가는 기존 비용을 비교 후 선택
  
  
  inf = 10000
  V, E = map(int, input().split())
  adj = [[inf] * (V + 1) for _ in range(V + 1)]
  for i in range(V + 1):
      adj[i][i] = 0
  for _ in range(E):
      u, v, w = map(int, input().split())
      adj[u][v] = w  # 방향성 그래프
  d = [0] * (V + 1)
  dijkstra(0, V)
  print(d)           # 시작 정점 0에서 각 정점으로 가는 최소 비용
  ```
  
  ```python
  def dijkstra():
      while Q:
          print(Q, D)
          now, dist = Q.pop(0)  # 정점 정보와 거리
          if D[now] < dist:  # 주어진 거리보다 저장된 거리가 더 작으면 skip
              continue
          # 현재 정점의 인접 정점을 선택하여 그 인접 정점을 확인
          for v in range(len(adj_list[now])):
              n_v, n_dist = adj_list[now][v]  # 연결된 정점과 그 거리
              # 현재까지의 거리와 연결된 정점의 거리를 더한 값이
              # 저장된 값보다 작다면 갱신
              if dist + n_dist < D[n_v]:
                  D[n_v] = dist + n_dist
                  Q.append((n_v, D[n_v]))  # 다음 정점과 갱신된 거리를 Queue에 등록
  
  
  INF = 987654321
  V, E = map(int, input().split())
  # 인접 리스트
  adj_list = [[] for _ in range(V + 1)]
  for _ in range(E):
      s, v, d = map(int, input().split())
      adj_list[s].append((v, d))
  D = [INF] * (V + 1)
  D[0] = 0
  for v, d in adj_list[0]:  # 시작 정점에서 인접한 정점 거리 저장
      D[v] = d
  Q = [*adj_list[0]]  # Queue 에 시작점으로 부터 이어진 값을 넣는다.
  dijkstra()
  print(D)
  ```
  
  

