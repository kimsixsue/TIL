[Divide and Conquer/Backtracking](#divide-and-conquer-backtracking)

1. [Divide and Conquer](#1-divide-and-conquer)

2. [Quick sort](#2-quick-sort)

3. [Binary Search](#3-binary-search)
   
4. [Backtracking](#4-backtracking)
   
5. [Tree](#5-tree)

# Divide and Conquer/Backtracking

## 1. Divide and Conquer

병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘이다. 또한, Multi-Core 멀티코어 CPU 나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용된다.

퀵 정렬은 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘이다.

**Merge Sort 병합 정렬**

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

- 분할 정복 알고리즘 활용

  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄.

  - top-down 방식

- 시간 복잡도

  - O(n log n )

- 병합 정렬 과정

  - 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.
  - 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합
  - 부분집합이 1개로 병합될 때까지 반복함

- 알고리즘 : 분할 과정

  ```python
  def merge_sort(m):
      if len(m) == 1:
          return m
      left, right = list(), list()
      middle = len(m) // 2
      for x in m[:middle]:
          left.append(x)
      for x in m[middle:]:
          right.append(x)
      left = merge_sort(left)
      right = merge_sort(right)
      return merge(left, right)
  ```
  
- 알고리즘 : 병합 과정

  ```python
  def merge(left, right):
      result = list()
      while left or right:
          if left and right:
              if left[0] <= right[0]:
                  result.append(left.pop(0))
              else:
                  result.append(right.pop(0))
          elif left:
              result.append(left.pop(0))
          elif right:
              result.append(right.pop(0))
      return result
  ```

## 2. Quick sort

- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.

- 병합 정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, pivot item 기준 아이템 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.

- 각 부분 정렬이 끝난 후, 병합정렬은 “병합”이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다.

- 알고리즘

  ```python
  A = list()
  def quickSort(A, l, r):
      if l < r:
          s = partition(A, l, r)
          quickSort(A, l, s - 1)
          quickSort(A, s + 1, r )
  ```

- Hoare-Partition 알고리즘

  ```python
  A = list()
  def partition(A, l, r):
      p = A[l]  # p : 피봇 값
      i, j = l, r
      while i <= j:
          while i <= j and A[i] <= p:
              i += 1
          while i <= j and p <= A[j]:
              j -= 1
          if i < j:
              A[i], A[j] = A[j], A[i]
  
      A[l], A[j] = A[j], A[l]
      return j
  ```

- 아이디어

  - P 피봇 값들 보다 작은 값은 왼쪽, 큰 값은 오른쪽 집합에 위치하도록 한다.
  - 피봇을 두 집합의 가운데에 위치시킨다.

- 피봇 선택

  - 왼쪽 끝/오른쪽 끝/임의의 세개 값 중에 중간 값

- Lomuto partition 알고리즘

  ```python
  A = list()
  def partition(A, p, r):
      x = A[r]
      i = p - 1
      
      for j in range(p, r):
          if A[j] <= x:
              i += 1
              A[i], A[j] = A[j], A[i]
      A[i + 1], A[r] = A[r], A[i + 1]
      return i + 1
  ```

  ```python
  def partition(l, r):
      pivot = A[l]
      i, j = l, r
      while i <= j and A[i]:
          while i <= j and A[i] <= pivot:
              i  += 1
          while i <= j and A[j] >= pivot:
              j -= 1
          if i < j:
              A[i], A[j] = A[j], A[i]
      A[l], A[j] = A[j], A[l]
      return j
      
  def qsort(l, r):
      if l < r:
          s = partition(l, r)
          qsort(l, s - 1)
          qsort(s + 1, r)
          
          
  A = [7, 2, 5, 3, 4, 5]
  N = len(A)
  qsort(0, N - 1)
  print(A)
  ```
  
  ```python
  def quick(n):
      length = len(n)
      if length <= 1:  #  숫자가 1개 이하일때는 정렬할 필요가 없음
          return n
      left = list()  # 기준값 보다 작은 값을 저장
      right = list()  # 기준값 보다 같거나 큰 값을 저장
      pivot = n[length // 2]  # or 0 or -1
      for i in range(length):
          if i == length // 2:  # 기준 값이 비교되지 않도록 하기 위함
              # left나 right 리스트에 들어갈 필요 없음
              # pivot 값이 기준 값이기 때문에 비교대상으로 이미 정렬이 될 것임
              continue
          if n[i] < pivot:
              left.append(n[i])
          else:  # pivot <= nu[i]
              right.append(n[i])
      return quick(left) + [pivot] + quick(right)
      
  
  numbers = [3, 1, 4, 1, 5, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
  print(f'정렬 전 : ', numbers)
  print('---' * 10)
  numbers = quick_sort(numbers)
  print(f'정렬 후 : ', numbers)
  ```

## 3. Binary Search

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

- 검색 과정
  1. 자료의 중앙에 있는 원소를 고른다.
  2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
  3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  4. 찾고자 하는 값을 찾을 때까지 1 ~ 3 의 과정을 반복한다.

- 알고리즘 : 반복구조

  ```python
  S = list()
  def binarySearch(n, S, key):
      low = 0
      high = n - 1
      
      while low <= high:
          mid = (low + high) // 2
          
          if S[mid] == key:
              return mid
          elif key < S[mid]:
              high = mid - 1
          else:  # s[mid] <= key
              low = mid + 1
      return -1
  ```

- 알고리즘 : 재귀구조

  ```python
  a = list()
  def binarySearch(a, low, high, key):
      if high < low:
          return -1
      else:
          mid = (low + high) // 2
          if key == a[mid]:
              return mid
          elif key < a[mid]:
              return binarySearch(a, low, mid - 1, key)
          else:  # a[mid] <= key
              return binarySearch(a, mid + 1, high, key)
  ```

## 4. Backtracking

**Backtracking 개념**

- 여러 가지 선택지(옵션)들이 존재하는 상황에서 한가지를 선택한다.

- 선택이 이루어지면 새로운 선택지들의 집합이 생성된다.

- 이런 선택을 반복하면서 최종 사태에 도달한다.
  - 올바른 선택을 계속하면 goal state 목표 상태에 도달한다.

- 백트래킹과 깊이 우선 탐색과의 차이

  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임. (**Prunning** 가지치기)

  - 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단.

  - 깊이 우선 탐색을 가하기에는 경우의 수가 너무 많음. 즉, **N!** 가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능한 문제.

  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 Exponential Time 지수함수 시간을 요하므로 처리 불가능

- 백트래킹 기법

  - 어떤 노드의 유망성을 점검한 후에 promising 유망하지 않다고 결정되면 그 노드의 부모로 backtracking 되돌아가 다음 자식 노드로 감.
  - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
  - prunning 가지치기 : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.

- 백트래킹을 이용한 알고리즘은 다음과 같은 절차로 진행된다.

  1. state space tree 상태 공간 트리의 깊이 우선 검색을 실시한다.
  2. 각 노드가 유망한지를 점검한다.
  3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

- 일반 백트래킹 알고리즘

  ```python
  def checknode(node v):
      if promising(v):
          if there is a solution at v:
              write the solution
          else:
              for each child u of v:
                  checknode(u)
  ```

**상태공간트리를 구축하여 문제를 해결**

```python
bool backtrack(선택 집합, 선택한 수, 모든 선택수):
    if 선택한 수 == 모든 선택수:  # 더 이상 탐색할 노드가 없다.
        찾는 솔루션인지 체크
        return 결과

    현재 선택한 상태집합에 포함되지 않는 후보 선택들(노드) 생성
    
    모든 후보 선택들에 대해
        선택 집합에 하나의 후보선택을 추가
        선택한 수 += 1
        결과 = backtrack 호출(선택 집합, 선택한 수, 모든 선택수)
        
        if 결과 == 성공:
            return 성공  # 성공한 경우 상위로 전달
        
    return 실패
```

- {1, 2, 3}  의 (powerset|순열) 을 구하는 백트래킹 알고리즘

  ```python
  def backtrack(a, k, input):  # a, 0, 3
      c = [0 for _ in range(MAXCANDIDATES)]
      ncands = 0
      
      if k == input:
          process_solution(a, k)
      else:
          k += 1
          make_candidates(a, k, input, c, ncands)
          for i in range(ncands):  # 2개 모두 처리
              a[k] = c[i]
              backtrack(a, k, input)
  
  def make_candidates(a, k, n, c, ncands):  # powerset
      c[0] = True
      c[1] = False
      ncands = 2
  
  def make_candidates(a, k, n, c, ncands):  # 순열
      in_perm = [False for _ in range(NMAX)]
      
      for i in range(1, k):
          in_pern[a[i]] = True
          
      ncand = 0
      for i in range(1, n + 1):
          if not in_perm[i]:
              c[ncands] = i
              ncands += 1
      
  def process_solution(a, k):  # powerset
      for i in range(1, k + 1):
          if a[i]:
              print(i)
  
  def process_solution(a, k):  # 순열
      for i in range(1, k + 1):
          print(a[i])
              
  a = [0 for _ in range(MAX)]  # (powerset|순열) 을 저장할 배열
  backtrack(a, 0, 3)  # 3 개의 원소를 가지는 (powerset|순열)
  ```

- list(range(1,11))의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.

  ```python
  def f(i, k, t, s, rs):
      # global cnt
      # cnt += 1
      if i == k:
          if t == s:
              for j in range(10):
                  if bit[j]:
                      print(A[j], end=' ')
              print()
      elif t < s:
          return
      elif s + rs < t:
          return
      else:
          bit[i] = 0
          f(i + 1, k, t, s, rs - A[i])
          bit[i] = 1
          f(i + 1, k, t, s + A[i], rs - A[i])
      return
  
  
  A = [_ for _ in range(1, 11)]
  bit = [0] * 10
  cnt = 0
  f(0, 10, 10, 0, sum(A))
  # print(cnt)
  ```

## 5. Tree

Complete Binary Tree 완전 이진 트리

- 높이가 h이고 노드 수가 n개일 때 (단, 2^h <= n <= 2^{h+1} - 1),

  포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
