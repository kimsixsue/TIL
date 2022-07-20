# Control Statement

## control statement

* flowchart로 표현 가능
  
  ### Conditional Statement
* Conditional Expression (== Ternary Operator)
  * ` *true value* if *condition* else *false value*

### 반복문

**[visualization - https://pythontutor.com/](https://pythontutor.com/)**

* enumerate()는 iterable 함수
  * (index, value) 쌍 tuple 객체 반환
    
    ```python
    for index, value in enumerate(iterable, start=0): # start부터 index값 시작
        print(index, value)
    ```
* List Comprehension
  * ` code **for** variable **in** iterable *[if conditional statement]*
    
    ```python
    list_2 = []
    list_2 = i * 2 for number in range(5) # 2, 4, 6, 8
    ```
* Dictionary Comprehension
  * ` {key: value **for** variable **in** iterable *[if conditional statement]*}
    
    ```python
    dict_2 = {}
    dict_2 = {'k': k *2 for k in range(5)} # 1: 2, 2: 4, 3: 6, 4: 8
    ```
* for-else
  * 끝까지 반복 실행한 후 else문 실행
    * break에 의해 도중에 종료될 경우, else 문은 실행되지 않음
    * 테스트 용으로 좋음
* pass
  * 아무것도 하지 않음. 반복문 외에도 쓸 수 있음
    * 잘 안 씀. 자리 채우는 용도로 임시로 넣어두기 좋음

---

## function

### 함수 기초

* Decomposition, Abstraction
* 기본 구조
  * **def**ine&call, input, docstring, scope, output
    
    ```python
    def func_name(parameter):
    """
    Documentation String
    """
    # code block
    return return_value
    ```
    
    ### 함수 Output
    
    ### 함수 Input
    
    ### 함수 Scope 범위
    
    ### 함수 Doc-String 문서화
    
    ### 함수 응용

---

## module

### 모듈과 패키지

### 파이썬 표준 라이브러리

### 사용자 모듈과 패키지

### 가상환경