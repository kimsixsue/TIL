# Data Structure

## Sequence

### String

- string.find(s)
  
  - 첫 s 위치 반환. **없으면 -1 반환**

- string.index(x)
  
  - 첫 s 위치 반환. **없으면 오류 발생**

- string.isalpha()
  
  - 알파벳 문자 여부
    - 한국어 포함. 유니코드 상 letter. 숫자 아닌 것

- string.title()
  
  - 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환

- string.strip([chars])
  
  - 공백이나 특정 문자를 제거
  - 양쪽을 제거
  - lstrip 왼쪽 제거, rstrip 오른쪽 제거

- 'separator'**.join**([iterable])
  
  - 구분자로 iterable을 합침
  - **+ 연산자보다 빠름**

- string.capitalize()
  
  - 가장 첫 번째 글자를 대문자로 변경

- string.swapcase()
  
  - 대문자 소문자 서로 변경

- isdecimal() ≤ isdigit() ≤ isnumeric()
  
  ### List

- list.insert(i, a)
  
  - list[i]에 항목 a를 삽입

- list.remove(a)
  
  - list 첫번째 a를 제거. **없으면 Error**
  - 대신 새 리스트를 만드는 것도 좋음

- list.pop()
  
  - list 마지막 항목 반환 후 제거
  - list.pop(i)는 list[i]를

- list.extend(m)
  
  - 리스트 끝에 *항목*들을 추가. +=과 동일

- list.reverse()
  
  - list를 거꾸로 정렬

- list.sort()
  
  - 리스트를 정렬. **None** 반환
  - sorted()와 다름

- list.count(a)
  
  - 리스트에서 a 개수 반환

- list.clear()
  
  - 모든 항목을 삭제
    
    ### Tuple

- extend 불가

------------------------------------------

## Unordered

### Set

- set.copy()
  
  - 얕은 복사본을 반환

- set.**add**(a)
  
  - 항목 a가 set에 없다면 추가

- set.pop()
  
  - 랜덤 항목 반환, 해당 항목 제거
  - 비어 있으면 Error

- set.discard(a)
  
  - a가 set에 있으면 삭제

- set.update(t)
  
  - t에 있는 모든 항목 중 set에 없는 항목 추가

- set.isdisjoint(t)
  
  - set가 t의 서로 같은 항목이 없으면 True. 서로소. 교집합이 없는지

- set.issubset(t)
  
  - set가 t의 하위 set인 경우, True

- set.issuperset(t)
  
  - set가 t의 상위 set인 경우, True
    
    ### Dictionary

- dictionary.copy()
  
  - 얕은 복사본을 반환

- **dictionary.get(k, *[,default]*)**
  
  - key k의 값을 반환, default는 None
  - 없을 경우 None
  - **.get(k, v)** 없을 경우 v를 반환

- dictionary.pop(k)
  
  - key k의 값을 반환, k 항목 삭제, 없을 경우 error
  - .pop(k, v) 없을 경우 v를 반환

- dictionary.update(*[other]*)
  
  - dictionary key value 덮어쓰기

------------------------------------------

## Shallow Copy & Deep Copy

### 복사 방법

- Assignment 할당 = 대입 연산자
  
  - 해당 객체에 대한 객체 참조를 복사
  - 해당 주소의 일부 값을 변경하는 경우 이를 **참조하는 모든 변수에 영향**
  - shallow copy

- Shallow copy
  
  - 같은 원소를 가진, 다른 주소를 복사
    - **copy** module의 copy
  - 리스트 내 리스트를 복사하면, **주소를 복사하는 것이라 같이 변함**

- **Deep copy**
  
  - 독립적
    - **슬라이싱**
    - b = **list**(a)
    ```python
    import copy
    list_b = copy.deepcopy(list_a)
    ```
