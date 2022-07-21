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

* Void function : 명시적인 return 값이 없는 경우 None 반환
  * 주로 **테스트**를 위해 print 이용 *<-> 데이터 처리는 return*
* return 값은 언제나 1개 (튜플 1개도 1개로 취급)

### 함수 Input

```python
def function(parameter): # def
  return 0
function('argument') # call
```

* 선택 argument: 입력하지 않으면 기본값으로

* **Positional Arguments**: 호출 시 위치에 따라 전달
  
  * 부족하면 문제 생김

* Keyword Argument: 변수명으로 argument 전달 가능
  
  * 다음에 Positional Argument를 넣으면 Error 발생.
    
    ```python
    function(a = 1, 2) # 키워드는 보통 마지막에 몰아서 씀
    ```

* Default Arguments Values
  
  ```python
  def function(a, b=0): # 기본값 지정
    return 0
  ```

* **Asterisk(*)** == [시퀀스] 언패킹 연산자
  
  * 정해지지 않은 arguments들을 처리
  * *tuple*이나 *list*를 언패킹

* 가변 인자(*args)
  
  * **positional argument**가 몇개인지 모를 때
  * args는 tuple
    *  return 값 초기화를 tuple[0]으로 하면 오류 방지

* packing == 데이터들을 묶어서 변수에 할당

* unpacking == 요소들을 변수들에 배분 할당
  
  * 변수 개수와 할당할 요소 개수 동일해야
    * 변수에 asterisk를 붙이면, **할당 후 남은 요소**들을 몰아넣음

* 가변 키워드 인자(**kwargs)
  
  * **keyword argument** 수를 알 수 없을 때
  * *dictionary*로 묶여 처리
  * 호출 시 string처럼하면 안됨, *변수나 키워드 인자*처럼

### Python의 Scope (범위)

* global scope: 어디서나 참조 가능한 공간
  * global variable
* local scope: 함수 내부에서만 참조 가능
  * local vairable
* 변수 lifecycle
  * **built-in** scope: 파이썬 실행부터 영원히
  * global scope: 모듈 호출 ~ 인터프리터 종료
  * local scope: 함수 호출 ~ 종료
* **Name Resolution**
  * identifier들은 namespace에 저장됨
  * LEGB Rule: 이름을 찾는 순서
    * **L**ocal scope: 작업중인 곳
    * **E**nclosed scope: local 한 단계 위
    * **G**lobal scope: 최상단 범위
    * **B**uilt-in scope: 정의없이 쓸 수 있는 모든 것
  * 내부에서는 외부에 접근만 가능
* **global** 문
  * 나열된 식별자가 global variable
    * 현재 코드 블록 전체 적용
    * global 뒤에 global에 나열된 식별자 등장 가능
    * 식별자로 parameter 쓸 수 없음
* **nonlocal**
  * global 제외, 가장 가까이 둘러싸고 있는 scope 변수 연결
    * nonlocal 뒤에 nonlocal에 나열된 식별자 등장 가능
    * 식별자로 parameter 쓸 수 없음
    * *이미 존재하는* 식별자와 연결만 가능
* **주의**
  * 가급적 쓰지 않는 것을 권장하며, 값을 수정하려면 항상 argument로 넘기고 return 값을 쓰는 것을 권장

### 함수 응용

* [**Built-in Functions**](https://docs.python.org/ko/3/library/functions.html): 함수와 type 내장
  * **map**(function, iterable)
    * iterable 요소 모두 function 적용, 그 결과를 반환
    * **map** object 반환
  * **filter**(function, iterable)
    * iterable 요소 모두 function 적용, 반환 결과가 **True**인 것들만 반환
    * **filter** object 반환
  * **zip**(*iterables)
    * iterable들을 모아 tuple을 원소로하는 zip object 반환
    * 같은 index끼리 모아 tuple로
      * 2차원 리스트, 가로 세로 바꿈
  * **lambda [parameter] : 표현식**
    * 표현식 계산 결과를 반환
      * return 문 없음
        
        ```python
        def func(a, b)
            return a + b
        
        lambda a, b: a - b if a > b else b - a
        lambda a, b: func(a, b, 100) # 인자 : 표현
        ```
    * 이름이 없어서 익명함수로도 불림
    * *간편 조건문* 가질 수 있음
    * 한번 쓰고 말 것을 간결하게 쓸 수 있음
  * **recursive function**: 스스로를 호출
    * **점화식** 등 알고리즘 설계 구현에 유용
      * 팩토리얼, 피보나치
    * 변수 이용이 적어져, 함수 이용, **가독성**이 좋아짐
    * **base case**(종료 상황) 존재, 수렴하도록 작성
    * *주의 사항*
      * 입력 값과 연산 속도가 반비례 (예외 있기도 함)
      * stack overflow 시 프로그램 동작않음
      * maximum recursion depth가 1000번으로, 호출 횟수가 넘어가면 Recursion Error
      * ```python
        import sys
        print(sys.getrecursionlimit()) # 1000
        sys.setrecursionlimit(31415)
        print(sys.getrecursionlimit())
        ```

---

## module

### 모듈과 패키지

* module == 다양한 기능을 하나의 파일(스크립트)로
  
  * 특정 기능을 하는 코드를 **.py** 단위로 작성
  * *import*문을 통해 내장 모듈을 namespace로 가져와야
  
  - import 문이 쓰인 코드의 위치에 따라 namespace가 결정
  
  - 코드 최상단에 import문을 작성할 경우, Global namespace에 import

* package == 다양한 파일을 하나의 폴더(디렉토리)로
  
  * 특정 기능과 연관있는 module들의 집합
  * 패키지 안에 서브 패키지 포함
  * *package.module* 형태로 모듈을 구조화할 수 있음
  
  ```python
  import module
  from module import var, function, Class
  from package import module as alias 
  import * # 무거울 수 있으니, 지양해야
  ```

* library == 다양한 package를 하나의 묶음으로

* pip == 이것을 관리하는 관리자

* 가상환경 == package의 활용 공간

### 파이썬 표준 라이브러리

**[파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)** : 기본적으로 설치된 모듈과 내장 함수

* **pip**(파이썬 패키지 관리자)
  
  * [**Py**thon **P**ackage **I**ndex](https://pypi.org/) 에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
  * [버전 명시 시] 패키지 설치 가능
  * $ pip **uninstall** some_package : 특정 패키지 삭제
  * $ pip **list** : 패키지 목록
  * $ pip **show** some_package : 특정 패키지 정보
  * **requirements.txt** : 패키지 목록 기록
    * $ pip freeze > requirements.txt 관리
    * $ pip install -r requirements.txt 설치

### 사용자 모듈과 패키지

* 패키지 : 여러 모듈, 하위 패키지로 구조화
  * 모든 폴더에는 ____init__.py__를 만들어 패키지로 인식

### 가상환경

* 외부 패키지와 모듈은 **pip**를 통해 설치
* 프로젝트들이 버전이 다를 수 있음
* 가상환경을 만들면, 프로젝트 별로 독립적으로 패키지를 관리 가능
* 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  1. 가상환경 생성
     * `$ python -m venv <디렉토리>`
     * 해당 디렉토리에 별도 파이썬 패키지가 설치
  2. 실행 환경에서 가상환경 활성화
     * `$ source venv/Scripts/activate`
     * `$ deactive` # 가상환경 비활성화
  3. 해당 폴더에 있는 패키지를 관리/이용