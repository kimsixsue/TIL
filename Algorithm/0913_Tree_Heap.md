- [Tree](#tree)
  * [BinaryTree](#binarytree)
    + [Representation](#representation)
    + [ExpressionTree](#expressiontree)
  * [BinarySearchTree](#binarysearchtree)
  * [Heap](#heap)

# Tree

**트리의 개념**

- 비선형 구조
- 원소들 간에 `1:n` 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조

**트리 - 정의**

- **한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다.**

  - 노드 중 최상위 노드를 root 루트라 한다.

  - 나머지 노드들은 `n(>=0)`개의 분리 집합 `T1,…,TN`으로 분리될 수 있다.


- **이들 `T1, …, TN`은 각각 하나의 트리가 되며(재귀적 정의) 루트의 subtree 부 트리라 한다.** 

  - 정점(node, vertex)

  - 단말노드 또는 leaf 잎 노드


**트리 - 용어정리**

- node 노드 - 트리의 원소
- edge 간선 - 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
- root node 루트 노드 - 트리의 시작 노드
- sibling node 형제 노드 - 같은 부모 노드의 자식 노드들
- 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- subtree 서브 트리 - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들

- degree 차수

  - 노드의 차수 : 노드에 연결된 자식 노드의 수.

  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값

  - 단말 노드(리프 노드) : 차수가 0인 노드. 자식 노드가 없는 노드


- level 높이

  - 노드의 높이 : 0 루트에서 노드에 이르는 간선의 수. 노드의 레벨

  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨


## BinaryTree

**모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리**

**각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리**

- left child node 왼쪽 자식 노드
- right child node 오른쪽 자식 노드

**이진트리 - 특성**

- 레벨 i에서의 노드의 최대 개수는 `2**i`개

- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 (`2**(h+1)-1`) 개가 된다.

**이진트리 - 종류**

- **Full Binary Tree 포화 이진 트리**

  - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리

  - 높이가 h일 때, 최대의 노드 개수인 (`2**(h+1)-1`) 의 노드를 가진 이진 트리

  - 루트를 1번으로 하여 `2**(h+1)-1` 까지 정해진 위치에 대한 노드 번호를 가짐


- **Complete Binary Tree 완전 이진 트리**
  - 높이가 h이고 노드 수가 n개일 때 (단,  h+1 <= n < `2**(h+1)-1`  ), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리


- **Skewed Binary Tree 편향 이진 트리**
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
    - 왼쪽 편향 이진 트리
    - 오른쪽 편향 이진 트리


**이진트리 - traversal 순회**

- traversal 순회란 트리의 각 노드를 중복되지 않게 전부 visit 방문 하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다.

- traversal 순회: 트리의 노드들을 체계적으로 방문하는 것

- **3가지의 기본적인 순회방법**

  - 전위순회(preorder traversal): VLR
    - 부모노드 방문 후, 자식노드를 좌,우 순서로 방문한다.

  - 중위순회(inorder traversal) : LVR
    - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문한다.

  - 후위순회(postorder traversal) : LRV
    - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.


- **preorder traversal 전위 순회**

  - 수행 방법
    1) 현재 노드 n을 방문하여 처리한다. -> V
    2) 현재 노드 n의 왼쪽 서브트리로 이동한다 . -> L
    3) 현재 노드 n의 오른쪽 서브트리로 이동한다. -> R

  - 전위 순회 알고리즘


```python
def preorder_traverse(T) :  # 전위순회
    if T :                  # T is not None
        visit(T)            # print(T.item)
        preorder_traverse(T.left)
        preorder_traverse(T.right)
```

- **inorder traversal 중위 순회**

  - 수행 방법
    1) 현재 노드 n의 왼쪽 서브트리로 이동한다. : L
    2) 현재 노드 n을 방문하여 처리한다. : V
    3) 현재 노드 n의 오른쪽 서브트리로 이동한다. : R

  - 중위 순회 알고리즘


```python
def inorder_traverse(T) :  # 중위순회
    if T :                 # T is not None
        inorder_traverse(T.left)
        visit(T)           # print(T.item)
        inorder_traverse(T.right)
```

- **postorder traversal 후위 순회**

  - 수행 방법
    1) 현재 노드 n의 왼쪽 서브트리로 이동한다. : L
    2) 현재 노드 n의 오른쪽 서브트리로 이동한다. : R
    3) 현재 노드 n을 방문하여 처리한다. : V


  - 후위 순회 알고리즘


```python
def postorder_traverse(T) :  # 후위순회
    if T :                   # T is not None
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)             # print(T.item)
```

### Representation

- **배열을 이용한 이진 트리의 표현**

  - 이진 트리에 각 노드 번호를 다음과 같이 부여

  - 루트의 번호를 1로 함

  - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 `2**n` 부터 `2**(n+1) - 1` 까지 번호를 차례로 부여


  - 노드 번호를 배열의 인덱스로 사용


  - 높이가 h 인 이진 트리를 위한 배열의 크기는?

    - 레벨 i의 최대 노드 수는? `2**i`
      $$
      따라서　1 + 2 + 4 + 8 ... + 2^i = ∑2^i = 2^{h+1}-1
      $$



**노드 번호의 성질**

- 노드 번호가 i 인 노드의 부모 노드 번호? `i//2`
- 노드 번호가 i 인 노드의 왼쪽 자식 노드 번호? `2*i`
- 노드 번호가 i 인 노드의 오른쪽 자식 노드 번호? `2*i+1`
- 레벨 n의 노드 번호 시작 번호는? `2**n`

**배열을 이용한 이진 트리의 표현의 단점**

- 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
- 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경 어려워 비효율적

**[참고] 이진 트리의 저장**

**부모 번호를 인덱스로 자식 번호를 저장**

```python
for i : 1 -> N  # 4 <- 간선의 개수 N
	read p, c   # 1 2 1 3 3 4 3 5 <- 부모 자식 순
    	if( c1[p] == 0)
        	c1[p] = c
        else
        	c2[p] = c
```

**자식 번호를 인덱스로 부모 번호를 저장**

```python
for i : 1 -> N  # 4 <- 간선의 개수 N
	read p, c   # 1 2 1 3 3 4 3 5 <- 부모 자식 순
    par[c] = p
```

**루트 찾기, 조상 찾기**

```python
c = 5              # 1 2 1 3 3 4 3 5 <- 부모 자식 순
while( a[c] != 0)  # 루트인지 확인
	c = a[c]
    anc.append(c)  # 조상 목록
root = c
```

```python
def find_root(v):
    for _ in range(1, v + 1):
        if not par[_]:
            return _
	    
def preorder(n):
    global cnt
    if n:
        cnt += 1
        tree[cnt] = n  # append 대신
        preorder(c_left[n])
        preorder(c_right[n])
        
def inorder(n):
    global cnt
    if n:
        inorder(c_left[n])
        cnt += 1
        tree[cnt] = n  # append 대신
        inorder(c_right[n])

def postorder(n):
    global cnt
    if n:
        postorder(c_left[n])
        postorder(c_right[n])
        cnt += 1
        tree[cnt] = n  # append 대신

def f(n):            # global cnt 없이 순회한 정점 수를 return하는 함수
    if not n:        # 서브트리가 비어있으면
       	return 0
    else:
        L = f(c_left[n])
        R = f(c_right[n])
        return L + R + 1

V = int(input())   # 정점 개수, 마지막 정점 번호
E = V - 1
# E = int(input())
# V = E + 1
arr = list(map(int, input().split()))
cnt = -1
tree = [0] * V
par = [0] * (V + 1)     # 자식을 인덱스로 부모 번호 저장
c_left = [0] * (V + 1)  # 부모를 인덱스로 자식 번호 저장
c_right = [0] * (V + 1)
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    par[c] = p
    if not c_left[p]:
        c_left[p] = c
    else:
        c_right[p] = c

root = find_root(V)    
XXXorder(root)
print(*tree)
```

```python
def pre(n):
    if n <= size:
        print(tree[n])
        pre(2 * n)
        pre(2 * n + 1)
        
tree = [0, 'A,' 'B', 'C', 'D', 'E', 'F']  # 완전이진트리
size = len(tree) - 1                      # 마지막 정점 번호
pre(1)
```

**트리의 표현 - 연결리스트**

배열을 이용한 이진 트리의 표현의 단점을 보완하기 위해 연결리스트를 이용하여 트리를 표현할 수 있다.

연결 자료구조를 이용한 이진트리의 표현

- 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결 리스트 노드를 사용하여 구현

| left           | 데이터 | right            |
| -------------- | ------ | ---------------- |
| 왼쪽 자식 노드 |        | 오른쪽 자식 노드 |

### ExpressionTree

수식을 표현하는 이진 트리

Expression Binary Tree 수식 이진 트리라고 부르기도 함.

연산자는 루트 노드이거나 가지 노드

피연산자는 모두 잎 노드

**수식 트리의 순회**

- 중위 순회 : `A / B * C * D + E` (식의 중위 표기법)

- 후위 순회 : `A B / C * D * E +` (식의 후위 표기법)

- 전위 순회 : `+ * * / A B C D E` (식의 전위 표기법)

## BinarySearchTree

탐색작업을 효율적으로 하기 위한 자료구조

모든 원소는 서로 다른 유일한 키를 갖는다.

key(왼쪽 서브트리)<key(루트 노드)<key(오른쪽 서브트리)

왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리다.

중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.

| 왼쪽 서브트리    | 루트 | 오른쪽 서브트리 |
| ---------------- | ---- | --------------- |
| 루트보다 작은 값 |      | 루트보다 큰 값  |

**이진 탐색 트리  - 연산**

- **탐색연산**

  - 루트에서 시작한다.

  - 탐색할 키 값 x를 루트 노드의 키 값과 비교한다.
    - (키 값 x = 루트노드의 키 값)인 경우 : 원하는 원소를 찾았으므로 탐색연산 성공
    - (키 값 x < 루트노드의 키 값)인 경우 : 루트노드의 왼쪽 서브트리에 대해서 탐색연산 수행
    - (키 값 x > 루트노드의 키 값)인 경우 : 루트노드의 오른쪽 서브트리에 대해서 탐색연산 수행

  - 서브트리에 대해서 순환적으로 탐색 연산을 반복한다.


- **삽입 연산**

  1. 먼저 탐색 연산을 수행
     - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인한다.
     - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치가 된다.
  
  
    2. 탐색 실패한 위치에 원소를 삽입한다.
  

**이진 탐색 트리 - 성능**

- **searching 탐색, insertion 삽입, deletion 삭제 시간은 트리의 높이 만큼 시간이 걸린다.**
  - O(h), h : BST의 height 높이
- **평균의 경우**
  - 이진 트리가 균형적으로 생성되어 있는 경우
  - O(log n)
- **최악의 경우**
  - 한쪽으로 치우친 경사 이진트리의 경우
  - O(n)
  - 순차탐색과 시간복잡도가 같다.
- **검색 알고리즘의 비교**
  - 배열에서의 순차 검색 : O(N)
  - 정렬된 배열에서의 순차 검색 : O(N)
  - 정렬된 배열에서의 이진탐색 : O(logN)
    - 고정 배열 크기와 삽입, 삭제 시 추가 연산 필요
  - 이진 탐색트리에서의 평균 : O(logN)
    - 최악의 경우 : O(N)
    - 완전 이진 트리 또는 균형트리로 바꿀 수 있다면 최악의 경우를 없앨 수 있다.
      - 새로운 원소를 삽입할 때 삽입 시간을 줄인다.
      - 평균과 최악의 시간이 같다. O(logn)
    - 해쉬 검색 : O(1)
      - 추가 저장 공간이 필요

## Heap

**완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조**

**max heap 최대 힙**

- 키값이 가장 큰 노드를 찾기 위한 **완전 이진 트리**
- {자식노드의 키값 < 부모노드의 키값}
- 루트 노드 : 키값이 가장 큰 노드

**min heap 최소 힙**

- 키값이 가장 작은 노드를 찾기 위한 **완전 이진 트리**
- {부모노드의 키값 < 자식노드의 키값}
- 루트 노드 : 키값이 가장 작은 노드

**힙 연산 - 삽입**

1. 삽입할 자리 확장

2. 확장한 자리에 삽입할 원소 저장

3. 자리바꾸기 반복

4. 비교할 부모 노드가 없으므로 자리 확정

**힙 연산 - 삭제**

- 힙에서는 루트 노드의 원소만을 삭제할 수 있다.
- 루트 노드의 원소를 삭제하여 반환한다.
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.

1. 루트 노드의 원소 삭제
2. 마지막 노드 삭제
3. 자리바꾸기
4. 자리 확정 

```python
# 최대힙

def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가
    c = last
    p = c // 2      # 완전이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]:  # 부모가 있고, 부모 < 자식 인경우, 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq(q):
    global last
    tmp = heap[1]         # root 백업
    heap[1] = heap[last]  # 삭제할 node의 key를 root에 복사
    last -= 1             # 마지막 node 삭제
    p = 1                 # root에 옮긴 값을 자식과 비교
    c = p * 2             # 왼쪽 자식
    while c <= last:           # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1             # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:  # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c              # 자식을 새로운 부모로
            c = p * 2          # 왼쪽 자식 번호를 계산
        else:                  # 부모가 더 크면
            break			   # 비교 중단,
    return tmp
    
heap = [0] * 100
last = 0
enq(2)  # 숫자들 계속 넣어보기

while last:
    print(deq())
```

**힙을 이용한 우선순위 큐**

- Heap 힙

  - 완전 이진 트리로 구현된 자료구조로서, 키값이 가장 큰 노드나 가장 작은 노드를 찾기에 용이한 자료구조

  - 힙의 키를 우선순위로 활용하여 우선순위 큐를 구현할 수 있다.

    > http://pages.cs.wisc.edu/~vernon/cs367/notes/11.PRIORITY-Q.html
