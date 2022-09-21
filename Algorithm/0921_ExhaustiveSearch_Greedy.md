[ExhaustiveSearch_Greedy](#exhaustivesearch-greedy)

1. [Iteration_Recursion](#1-iteration-recursion)

2. [ExhaustiveSearch](#2-exhaustivesearch)

3. [Permutation](#3-permutation)

4. [Subset](#4-subset)

5. [Combination](#5-combination)

6. [GreedyAlgorithm](#6-greedyalgorithm)

7. [Activity-selection problem](#7-activity-selection-problem)

8. [baby-gin](#8-baby-gin)

# ExhaustiveSearch_Greedy

## 1. Iteration_Recursion

- 반복과 재귀는 유사한 작업을 수행할 수 있다.

- 반복은 수행하는 작업이 완료될 때 까지 계속 반복
  - 루프 (for, while 구조)

- 재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법

  - 하나의 큰 문제를 해결할 수 있는(해결하기 쉬운) 더 작은 문제로 쪼개고 결과들을 결합한다.

  - 재귀 함수로 구현

- 반복구조

  - **초기화**
    - 반복되는 명령문을 실행하기 전에 (한번만) 조건 검사에 사용할 변수의 초기값 설정
  - **check control expression 조건검사**
  - **반복할 명령문 action 실행**
  - **loop update 업데이트**
    - infinite loop 무한 루프가 되지 않게 조건이 false 거짓이 되게 한다.

- 반복을 이용한 선택정렬

  ```python
  def SelectionSort(A):
      right = len(A)
      for left in range(right - 1):
          min_left = left
          for i in range(left + 1, right):
              if A[i] < A[min_left]:
                  min_left = i
          A[min_left], A[left] = A[left], A[min_left]
  ```

- 재귀적 알고리즘

  - 재귀적 정의는 두 부분으로 나뉜다.
  - 하나 또는 그 이상의 basis case or rule 기본 경우
    - 집합에 포함되어 있는 원소로 induction을 생성하기 위한 seed 시드 역할
  - 하나 또는 그 이상의 inductive case or rule 유도된 경우
    - 새로운 집합의 원소를 생성하기 위해 결합되어지는 방법

- recursive function 재귀 함수

  - 함수 내부에서 직접 혹은 간접적으로 자기 자신을 호출하는 함수.
  - 일반적으로 재귀적 정의를 이용해서 재귀 함수를 구현한다.
  - 따라서, basis part 기본부분과 inductive part 유도 부분으로 구성된다.
  - 재귀적 프로그램을 작성하는 것은 반복 구조에 비해 간결하고 이해하기 쉽다.
    - 그러나, 재귀에 대해 익숙하지 않은 개발자들은 재귀적 프로그램이 어렵다고 느낀다.
  - 함수 호출은 프로그램 메모리 구조에서 스택을 사용한다. 따라서 재귀 호출은 반복적인 스택의 사용을 의미하며 메모리 및 속도에서 성능저하가 발생한다.

  ```python
  def selection_sort(depth):
      if depth == length - 1:
          return
      mini = depth
      for i in range(depth, length):
          if number[mini] > number[i]:
              mini = i
      number[depth], number[mini] = number[mini], number[depth]
      selection_sort(depth + 1)
  
  
  number = [2, 4, 6, 1, 9, 8, 7, 0]
  length = len(number)
  selection_sort(0)
  print(number)
  ```

- 팩토리얼 재귀 함수

  - 재귀적 정의

    - Basis rule:
      - N <= 1 경우, n = 1
    - Inductive rule:
      - N > 1, n! = n * (n - 1)!

  - n! 에 대한 재귀함수

    ```python
    def fact(n):
        if n <= 1:    # Basis part
            return 1
        else:         # Inductive part
            return n * fact(n - 1)
    ```

**반복 또는 재귀?**.

- 해결할 문제를 고려해서 반복이나 재귀의 방법을 선택
- 재귀는 문제 해결을 위한 알고리즘 설계가 간단하고 자연스럽다.
  - 추상 자료형(List, tree 등)의 알고리즘은 재귀적 구현이 간단하고 자연스러운 경우가 많다.
- 일반적으로, 재귀적 알고리즘은 Iterative 반복 알고리즘보다 더 많은 메모리와 연산을 필요로 한다.
- **입력 값 n이 커질수록 재귀 알고리즘은 반복에 비해 비효율적일 수 있다.**

|                | Recursion 재귀                                               | Iteration 반복                                               |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 종료           | 재귀 함수 호출이 종료되는 base case 베이스 케이스            | 반복문의 종료 조건                                           |
| 수행 시간      | (상대적) 느림                                                | 빠름                                                         |
| 메모리 공간    | (상대적) 많이 사용                                           | 적게 사용                                                    |
| 소스 코드 길이 | 짧고 간결                                                    | 길다                                                         |
| 소스 코드 형태 | 선택 구조(if…else)                                           | 반복 구조(for, while)                                        |
| 무한 반복시    | 스택 오버플로우                                              | CPU를 반복해서 점유                                          |
| $2^k$ 연산     | def Power_of_2(k)  # Output: 2**k<br />    if k == 0:<br />        return 1<br />    else:<br />        return 2 * Power_of_2(k - 1) | def Power_of_2(k)  # Output: 2**k<br />    i = 0<br />    power = 1<br />    while i < k:<br />        power *= 2<br />        i += 1<br />    return power |

## 2. ExhaustiveSearch

**brute-force 고지식한 방법**

- brute-force는 문제를 해결하기 위한 간단하고 쉬운 접근법이다.

  - 컴퓨터의 force를 의미한다.

- brute-force 방법은 대부분의 문제에 적용 가능하다.

- 상대적으로 빠른 시간에 문제 해결(알고리즘 설계)을 할 수 있다.

- 문제에 포함된 자료(요소, 인스턴스)의 크기가 작다면 유용하다.

- 학술적 또는 교육적 목적을 위해 알고리즘의 효율성을 판단하기 위한 척도로 사용된다.

- Brute-force 탐색 (sequential search)

  - 자료들의 리스트에서 키 값을 찾기 위해 첫 번째 자료부터 비교하면서 진행한다.

    ```python
    def SequentialSearch( A[0 .. n], k ):
        A[n] = k
        i = 0
        while A[i] != k:
            i += 1
        if i < n:
            return i
        else:
            return -1
    ```

**완전 검색으로 시작하라**

- 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 작다.
  - 완전검색은 입력의 크기를 작게 해서 간편하고 빠르게 답을 구하는 프로그램을 작성한다.
  
- 이를 기반으로 그리디 기법이나 동적 계획법을 이용해서 효율적인 알고리즘을 찾을 수 있다.

- 검정 등에서 주어진 문제를 풀 때, **우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직**하다.

- 완전 검색을 통한 Baby-gin 접근

- 고려할 수 있는 모든 경우의 수 생성하기
  - 6개의 숫자로 만들 수 있는 모든 숫자 나열 (중복 포함)
  
    ```python
    def perm(depth):
        global flag
        if depth == 6:
            total = 0
            if per[0] == per[1] and per[1] == per[2]:
                total += 1
            if per[0] + 1 == per[1] and per[1] + 1 == per[2]:
                total += 1
            if per[3] == per[4] and per[4] == per[5]:
                total += 1
            if per[3] + 1 == per[4] and per[4] + 1 == per[5]:
                total += 1
            if total == 2:
                flag = True
        else:
            for number in range(6):
                if not checked[number]:
                    per[depth] = arr[number]
                    checked[number] = 1
                    perm(depth + 1)
                    checked[number] = 0
    
    
    for _ in range(int(input())):
        flag = False
        arr = list(map(int, input()))
        checked = [0] * 6
        per = [0] * 6
        perm(0)
        print(flag)
    ```
  
- 완전 검색
  - 많은 종류의 문제들이 특정 조건을 만족하는 경우나 요소를 찾는 것이다.
  - 또한, 이들은 전형적으로 permutation 순열, combination 조합, 그리고 subsets 부분집합과 같은 Combinatorial Problems 조합적 문제들과 연관된다.
  - 완전 검색은 조합적 문제에 대한 brute-force 방법이다.

## 3. Permutation

- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것

- 서로 다른 n개 중 r개를 택하는 순열은 아래와 같이 표현한다.

  $_nP_r$

- 그리고 nPr 은 다음과 같은 식이 성립한다.

  $_nP_r$ = (n-0) * (n-1) * (n-2) * ... * (n-r+1)

- nPn = n! 이라고 표기하며 Factorial이라 부른다.

  n! = n * (n-1) * (n-2) * ... * 2 * 1

- 다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련 있다.
  - 예> TSP(Traveling Salesman Problem)
- N 개의 요소들에 대해서 n! 개의 순열들이 존재한다.
  - 12! = 479,001,600
  - n > 12 인 경우, 시간 복잡도 폭발적으로 ↑

**순열 생성 방법**

- Lexicographic-Order 사전적 순서

  - {1, 2, 3}, n = 3 인 경우 다음과 같이 생성된다.
  - [1 2 3] [1 3 2] [2 1 3] [2 3 1] [3 1 2] [3 2 1]

- Minimum-exchange requirement 최소 변경을 통한 방법

  - 각각의 순열들은 이전의 상태에서 단지 두 개의 요소들 교환을 통해 생성
  - [**1** 2 **3**] [**3 2** 1] [2 **3 1**] [**2** 1 **3**] [**3 1** 2] [1 3 2]

- 재귀 호출을 통한 순열 생성

  ```python
  # p[]: 데이터가 저장된 배열
  # k: 원소의 개수, n: 선택된 원소의 수
  
  def perm(n, k):
      if n == k:
      	print(p)  # 원하는 작업 수행
      else:
          for i in range(n, k):
              p[n], [i] = p[i], p[n]
              perm(n + 1, k)
              p[n], [i] = p[i], p[n]
              
              
  p = [1, 2, 3, 4, 5]
  perm(0, 5)
  ```

**[참고]**

- 사용할 숫자를 배열 a에 저장한다.

- 사용된 숫자의 위치를 표시할 배열 used를 준비한다.

- 왼쪽부터 사용하지 않은 숫자를 찾으면 표시하고, 숫자를 복사한다.

- 다음 자리를 정하기 위해 재귀호출을 한다.

- 숫자 자리를 모두 결정했으면 출력한다.

  ```python
  # p[]: 순열을 저장하는 배열, arr[]: 순열을 만드는데 사용할 숫자 배열
  # n: 원소의 개수, i: 선택된 원소의 수
  # used[N - 1]: 사용 여부, p: 결과 저장 배열
  
  def perm(n, k, r):
      if n == r:
          print(p)
      else:
          for i in range(k):     # 모든 원소에 대해
              if not used[i]:    # 사용된 적이 없으면
                  p[n] = arr[i]  # 순열에 사용
                  used[i] = 1    # 사용됨으로 표시
                  perm(n + 1, k, r)
                  used[i] = 0    # 다른 자리에서 사용 가능
                  
                  
  N = 4
  R = 3
  arr = [i for i in range(1, N + 1)]
  used = [0] * N
  p = [0] * R
  # p[0] = 1
  # used[1] = 1
  # perm(1, N, R)
  perm(0, N, R)
  ```

  ```python
  def array_sum(i, k):
      global minV
      if i == k:  # 인덱스 i == 원소의 개수
          s = 0   # 모든 l행에서 p[l] 열을 골랐을 때의 합
          for l in range(k):
              s += arr[l][p[l]]
          if minV > s:
              minV = s
      else:
          for j in range(i, k):
              p[i], p[j] = p[j], p[i]
              f(i + 1, k)
              p[i], p[j] = p[j], p[i]
  
              
  T = int(input())
  for tc in range(1, T + 1):
      N = int(input())
      arr = [list(map(int, input().split())) for _ in range(N)]
      p = [i for i in range(N)]
      minV = N * 10
      array_sum(0, N)
      print(f'#{tc} {minV}')
  ```

```python
def array_sum(i, k, s):
    global minV
    if i == k:  # 인덱스 i == 원소의 개수
        if minV > s:
            minV = s
    elif s >= minV:
        return
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i + 1, k, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]

            
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    minV = N * 10
    array_sum(0, N, 0)
    print(f'#{tc} {minV}')
```

## 4. Subset

- 집합에 포함된 원소들을 선택하는 것이다.
- 다수의 중요 알고리즘들이 원소들의 그룹에서 최적의 부분 집합을 찾는 것이다.
  - 예> knapsack 배낭 짐싸기
- N 개의 원소를 포함한 집합
  - 자기 자신과 공집합 포함한 power set 모든 부분집합의 개수는 $2^n$ 개
  - 원소의 수가 증가하면 부분집합의 개수는 지수적으로 증가

**부분 집합 생성 방법**

- 바이너리 카운팅을 통한 Lexicographic Order 사전적 순서

  - 부분집합을 생성하기 위한 가장 자연스러운 방법이다.
  - Binary Counting 바이너리 카운팅은 사전적 순서로 생성하기 위한 가장 간단한 방법이다.

- Binary Counting 바이너리 카운팅

  - 원소 수에 해당하는 N개의 비트열을 이용한다.

  - n번째 비트값이 1이면 n번째 원소가 포함되었음을 의미한다.

    | 10진수 | 이진수 | {A, B, C, D} |
    | ------ | ------ | ------------ |
    | 0      | 0000   | {}           |
    | 1      | 0001   | {A}          |
    | 2      | 0010   | {B}          |
    | 3      | 0011   | {B, A}       |
    | 4      | 0100   | {C}          |
    | 5      | 0101   | {C, A}       |
    | 6      | 0110   | {C, B}       |
    | 7      | 0111   | {C, B, A}    |
    | 8      | 1000   | {D}          |
    | 9      | 1001   | {D, A}       |
    | 10     | 1010   | {D, B}       |
    | 11     | 1011   | {D, B, A}    |
    | 12     | 1100   | {D, C}       |
    | 13     | 1101   | {D, C, A}    |
    | 14     | 1110   | {D, C, B}    |
    | 15     | 1111   | {D, C, B, A} |

  ```python
  arr = [3, 6, 7, 1, 5, 4]
  n = len(arr)
  for i in range(1 << n):   # 1 << n: 부분집합의 개수
      for j in range(n):    # 원소의 수만큼 비트를 비교함
          if i & (1 << j):  # i의 j번째 비트 == 1 이면
              print('%d' % arr[j], end='')  # j번째 원소 출력
          print
  ```
  
  ```python
  def f(i, k):
      if i == k:
          # print(bit)
          for j in range(k):
              if bit[j]:
                  print(arr[j], end = ' ')
          print()
      else:
          bit[i] = 0
          f(i+1, k)
          bit[i] = 1
          f(i+1, k)
  
  arr = [3, 6, 7]
  n = len(arr)
  bit = [0] * n
  f(0, n)
  ```

## 5. Combination

- 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 combination 조합이라고 부른다.

- 조합의 수식

  $$
  \begin{aligned}
  &_nC_r = \frac {n!}{(n-r)!r!} \quad ,(n \geq r) \\
  &_nC_r = _{n-1}C_{r-1} + _{n-1}C_r \quad \to 재귀적 표현 \\
  &_nC_0 = 1
  \end{aligned}
  $$
  
- 재귀 호출을 이용한 조합 생성 알고리즘

  ```python
  # an[] : n개의 원소를 가지고 있는 배열
  # tr[] : r개의 크기의 배열, 조합이 임시 저장될 배열
  
  def comb(n, r):
      if r == 0:
          print(tr)
      elif n < r:
          return
      else:
          tr[r - 1] = an[n - 1]
          comb(n - 1, r - 1)
          comb(n - 1, r)
  ```

**[참고]**

- n개에서 r개를 고르는 조합 (재귀)

  ```python
  # n개에서 r개를 고르는 조합
  # s 선택할 수 있는 구간의 시작
  
  def nCr(n, r, s):
      if r == 0:
          print(*comb)
      else:
          for i in range(s, n - r + 1):
              comb[r - 1] = A[i]
              nCr(n, r - 1, i + 1)
  ```

## 6. GreedyAlgorithm

- 탐욕 알고리즘은 최적해를 구하는 데 사용되는 근시안적인 방법
- 일반적으로, 머리속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 된다.
- 여러 경우 중 하나를 선택 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.
- 각 선택 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, **그것이 최적이라는 보장은 없다.**
- 일단, 한번 선택된 것은 번복하지 않는다. 이런 특성 때문에 대부분의 탐욕 알고리즘들은 단순하며, 또한 제한적인 문제들에 적용된다.
- optimization 최적화 문제란 가능한 해들 중에서 가장 좋은(최대 또는 최소) 해를 찾는 문제이다.

 **탐욕 알고리즘의 동작 과정**

1) 해 섵택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 Solution Set 부분해 집합에 추가한다.
2) 실행 가능성 검사 : 새로운 부분 해 집합이 실행가능한지를 확인한다. 곧, 문제의 제약 조건을 위반하지 않는 지를 검사한다.
3) 해 검사 : 새로운 부분 해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1의 해 선택부터 다시 시작한다.

- 탐욕 기법을 적용한 거스름돈 줄이기

  1) 해 선택 : 여기에서는 멀리 내다볼 것 없이 가장 좋은 해를 선택한다. 단위가 큰 동전으로만 거스름돈을 만들면 동전의 개수가 줄어들므로 현재 고를 수 있는 가장 단위가 큰 동전을 하나 골라 거스름돈에 추가한다.
  2) 실행 가능성 검사 : 거스름돈이 손님에게 내드려야 할 액수를 초과하는지 확인한다. 초과한다면 마지막에 추가한 동전을 거스름돈에서 빼고, 1로 돌아가서 현재보다 한 단계 작은 단위의 동전을 추가한다.
  3) 해 검사 : 거스름돈 문제의 해는 당연히 거스름돈이 손님에게 내드려야 하는 액수와 일치하는 셈이다. 더 드려도, 덜 드려도 안되기 때문에 거스름돈을 확인해서 액수에 모자라면 다시 1로 돌아가서 거스름돈에 추가할 동전을 고른다.

  - 최적해를 반드시 구한다는 보장이 없다.

**knapsack 배낭 짐싸기**

- 도둑은 부자들의 값진 물건들을 훔치기 위해 보관 창고에 침입하였다.

- 도둑은 훔친 물건을 배낭에 담아 올 계획이다. 배낭은 담을 수 있는 물건의 총 W 무게가 정해져 있다.

- 창고에는 n 여러 개의 물건들이 있고 각각의 물건에는 무게와 값이 정해져 있다.

- 경비원들에게 발각되기 전에 배낭이 수용할 수 있는 무게를 초과하지 않으면서, 값이 최대가 되는 물건들을 담아야 한다.

- Knapsack 문제의 정형적 정의

  - $S = \{ item_1 , item_2 , ... , item_n \} ,$ 물건들의 집합

  - $w_i : item_i$ 의 무게, $P_i = item_i$ 의 값

  - W : 배낭이 수용가능 한 총 무게

  - 문제 정의

    $$
    \sum\nolimits_{item_i \in A}^{}w_i \le W  를  만족하면서
    \sum\nolimits_{item_i \in A}^{}P_i  가  최대가  되도록
    A \subseteq S  가  되는  A  를  결정하는  문제
    $$

- Knapsack 문제 유형
  - 0-1 Knapsack
    - 배낭에 물건을 통째로 담야아 하는 문제.
    - 물건을 쪼갤 수 없는 경우.
  - Fractional Knapsack
    - 물건을 부분적으로 담는 것이 허용되는 문제.
    - 물건을 쪼갤 수 있는 경우.

- 0-1 Knapsack에 대한 완전 검색 방법
  - 완전 검색으로 물건들의 집합 S에 대한 모든 부분집합을 구한다.
  - 부분집합의 총무게가 W를 초과하는 집합들은 버리고, 나머지 집합에서 총 값이 가장 큰 집합을 선택할 수 있다.
  - 물건의 개수가 증가하면 시간 복잡도가 지수적으로 증가한다.
    - 크기 n인 부분합의 수 $2^n$

- 0-1 Knapsack에 대한 탐욕적 방법
  - 값이 비싼 물건부터 채운다.
  - 무게가 가벼운 물건부터 채운다.
  - kg 무게 당 값이 높은 순서로 물건을 채운다.
  - 탐욕적 방법으로 최적해를 구하기 어렵다.
- Fractional Knapsack 문제
  - 물건의 일부를 잘라서 담을 수 있다.

## 7. Activity-selection problem

- $s_i$ 시작시간과  $f_i$ 종료시간이 있는 n개의 활동들의 집합 $A = \{A_1,A_2,...,A_n \}, 1 \le i \le n$ 에서 non-overlapping 서로 겹치지 않는 최대갯수의 활동들의 집합 S를 구하는 문제
- 양립 가능한 활동들의 크기가 최대가 되는 $S_{0,n+1}$ 의 부분집합을 선택하는 문제
  - 종료 시간 순으로 활동들을 정렬한다.
  - $S_{0,n+1}$ 는 $a_0$ 의 종료 시간부터 $a_{n+1}$ 의 시작시간 사이에 포함된 활동들
  - $S_{0,n+1} = \{a_1, a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9,a_{10} \} = S$

- 탐욕 기법의 적용
  - 공집합이 아닌 subproblem 하위 문제 $S_{i,j}$ 가 있고 $S_{i,j}$ 에 속한 활동 $a_m$ 은 종료 시간이 가장 빠른 활동이다.
  - 그렇다면,
    1. subproblem 하위문제 $S_{i,j}$ 에서 종료 시간이 가장 빠른 활동 $a_m$ 을 선택한다.
    2. $S_{i,m}$ 은 공집합이므로, $a_m$ 을 선택하면 공집합이 아닌 하위 문제 $S_{m,j}$ 가 남는다.
    3. 1, 2 과정을 반복한다.
  - $S_{i,j}$ 를 풀기 위해
    1. 종료 시간이 가장 빠른 $a_m$ 선택. locally optimal choice 탐욕적 선택
    2. $S_{i,j} = \{a_m\} \cup S_{m,j}$ 의 해집합. 탑다운 방식의 문제 해결

- 탐욕 기법을 적용한 반복 알고리즘

  ```python
  # A : 활동들의 집합
  # S : 선택된 활동(회의)들 집합
  # s[i] : 시작시간
  # f[i] : 종료시간
  # 1 <= i <= n
  
  A.sort(f)  # by finish time
  S = {A_1}
  j = 1
  for i in range(2, n +1):
      if s[i] >= f[j]:
          S += {A[i]}
          j = i
  ```

  - 종료 시간이 빠른 순서로 활동들을 정렬한다.
  - $A_1$ 첫 번째 활동을 선택한다.
  - $A_1$ 선택한 활동의 종료시간보다 빠른 시작 시간을 가지는 활동을 모두 제거한다.
  - 남은 활동들에 대해 앞의 과정을 반복한다.

- 재귀 알고리즘

  ```python
  # A : 정렬된 활동 들의 집합
  # S : 선택된 활동(회의)들 집합
  # s[i] : 시작시간
  # f[i] : 종료시간
  # 1 <= i <= n + 1
  
  def Recursive_Selection(i, j):
      m = i + 1
    
      while m < j and s[m] < f[i]:  # 종료 시간이 가장 빠른 활동 선택
          m += 1  
          
      if m < j:
          return {a[m]} + Recursive_Selection(m, j)
      else:
          return {}  # 공집합
  ```

**탐욕 알고리즘의 필수 요소**

- greedy choice property 탐욕적 선택 속성

  - 탐욕적 선택은 최적해로 갈 수 있음을 보여라.

    -> 즉, 탐욕적 선택은 항상 안전하다.

- optimal substructure property 최적 부분 구조

  - 최적화 문제를 정형화하라

    -> 하나의 선택을 하면 풀어야 할 하나의 하위 문제가 남는다.

- **[원문제의 최적해 = 탐욕적 선택 + 하위 문제의 최적해]** 임을 증명하라.

- 탐욕 기법과 동적 계획법의 비교

  | 탐욕 기법                                                    | 동적 계획법                                             |
  | ------------------------------------------------------------ | ------------------------------------------------------- |
  | 매 단계에서, 가장 좋게 보이는 것을 빠르게 선택한다.<br />-> local optimal choice 지역 최적 선택 | 매 단계의 선택은 해결한 하위 문제의 해를 기반으로 한다. |
  | 하위 문제를 풀기 전에 (탐욕적) 선택이 먼저 이루어진다.       | 하위 문제가 우선 해결된다.                              |
  | Top-down 방식                                                | Bottom-up 방식                                          |
  | 일반적으로, 빠르고 간결하다.                                 | 좀더 느리고, 복잡하다.                                  |

- 대표적인 탐욕 기법의 알고리즘들

  | 알고리즘                 | 목적                                                         | 설명                                                         |        |
  | ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ |
  | Prim                     | N 개의 노드에 대한 MST 최소 신장 트리를 찾는다.              | 서브트리를 확장하면서 MST를 찾는다.                          | 그래프 |
  | Kruskal                  | N 개의 노드에 대한 MST 최소 신장 트리를 찾는다.              | 싸이클이 없는 서브 그래프를 확장하면서 MST를 찾는다.         | 그래프 |
  | Dijkstra                 | 주어진 정점에서 다른 정점들에 대한 최단 경로를 찾는다.       | 주어진 정점에서 가장 가까운 정점을 찾고, 그 다음을 정점을 반복해서 찾는다. | 그래프 |
  | Huffman<br />tree & code | 문서의 압축을 위해 문자들의 빈도수에 따라 코드값을 부여한다. | 출현 빈도가 낮은 문자부터 선택해서 이진 트리를 완성하고 코드값을 부여한다. | 문자열 |

## 8. baby-gin

- 탐욕 기법을 통한 Baby-gin 문제 해결

- 완전검색 아닌 방법으로 풀어보자.
  - 6개의 숫자는 6자리의 정수 값으로 입력된다.
  - counts 배열의 각 원소를 체크하여 run과 triplet 및 baby-gin 여부를 판단한다.
- 풀이
  - run 조사 후 run 데이터 완전 삭제
  - triplet 조사 후 triplet 데이터 완전 삭제

- 알고리즘 예

  ```python
  def f(i, k):
      if i == k:
          tri, run = 0, 0
          if card[0] == card[1] and card[1] == card[2]:
              tri += 1
          if card[0] + 1 == card[1] and card[1] + 1 == card[2]:
              run += 1
          if card[3] == card[4] and card[4] == card[5]:
              tri += 1
          if card[3] + 1 == card[4] and card[4] + 1 == card[5]:
              run += 1
          if run + tri == 2:
              return 1
          else:
              return 0
      else:
          for j in range(i, k):
              card[i], card[j] = card[j], card[i]
              if f(i + 1, k):
                  return 1
              card[i], card[j] = card[j], card[i]
  		return 0
      
              
  T = int(input())
  for tc in range(1, T + 1):
      card = list(map(int, input()))
      ans = f(0, 6)
      if ans:
          print(f'#{tc} Baby Gin')
      else:
          print(f'#{tc} Lose')
  ```

  ```python
  i, inp, tri, run = 0, 0, 0, 0
  inp = input_6_numbers()
  c = [0 for _ in range(12)]
  
  while i < 6:
      c[in % 10] += 1
      inp /= 10
      i += 1
      
  i = 0
  while i < 10:
      if c[i] >= 3:  # triplet
          c[i] -= 3
          tri += 1
          continue  # i 그대로
      if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:  # run
          c[i] -= 1
          c[i + 1] -= 1
          c[i + 2] -= 1
          run += 1
          continue  # i 그대로
      i += 1
      
  if run + tri == 2:
      print('baby gin')
  else:
      print('lose')
  ```

  ```python
  T = int(input())
  for tc in range(1, T + 1):
      card = int(input())
      c = [0] * 12
      
      i = 0
      while i < 6:
          c[card % 10] += 1
          caard //= 10
          i += 1
          
      i = 1
      while i < 10:
          if c[i] >= 3:
              c[i] -= 3
              tri += 1
              continue
          if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
              c[i] -= 1
              c[i + 1] -= 1
              c[i + 2] -= 1
              run += 1
              continue
          i += 1
          
      if run + tri == 2:
          print(f'#{tc} Baby Gin')
      else:
          print(f'#{tc} Lose')
  ```

  

