- [OOP](#oop)
  * [Object-Oriented Programming](#object-oriented-programming)
    + [OOP 기초](#OOP 기초)
      - [Instance](#instance)
      - [Class](#class)
      - [Object](#object)
      - [OOP method](#oop-method)
  * [OOP의 핵심 개념](#OOP의 핵심 개념)
    + [Abstraction 추상화](#Abstraction 추상화)
    + [Inheritance 상속](#Inheritance 상속)
    + [Polymorphism 다형성](#Polymorphism 다형성)
    + [Encapsulation 캡슐화](#Encapsulation 캡슐화)
  * [에러/예외 처리 Error/Exception Handling](#에러/예외 처리 Error/Exception Handling)
    + [에러와 예외](#에러와 예외)
    + [예외 처리](#예외 처리)

# OOP

## Object-Oriented Programming

정보와 행동을 가진(묶은) Object들과 object 간의 소통

흘러가는 절차 지향을 벗어난 방법론.
- 정보와 행동 분리, **추상화**된 구조(인터페이스)
  - 복잡한 것 숨겨도 필요한 것 쓸 수 있음

장점
- 클래스 단위로 모듈화. 일을 나누기 쉬움.
- 필요한 부분만 **수정하기 쉬움** 

단점
- 설계하는데 시간과 노력이 많이 듦
- 실행 속도가 상대적으로 느림. 사람이 편해서 컴퓨터가 힘듦

### OOP 기초

#### Instance

Class로 만든 Object. 하나하나의 실체

#### Class

공통된 object들의 분류를 정의.
- 단어들의 첫글자가 대문자(PascalCase = UpperCamelCase)
- 기본적으로 정의되어 있는 클래스: list, int, tuple, set, dictionary 등

#### Object

**Object는 특정 type의 *instance***

- 파이썬에서 모든 것이 Object 객체

**Object**: **속성**(정보, 변수)과 **행동**(동작, 함수-메서드)으로 구성된 **모든 것**

Object 특징

- type : 어떤 operator와 method가 가능한가
- **attribute** : Object의 속성(상태, 데이터, 정보)
- **method**: 특정 Object의 조작법(행위, 함수, 기능)

object의 설계도(class)를 갖고, object(instance)를 생성

object 비교

- `==`: 값이 같은가
- `is`: 객체가 같은가

OOP 속성

- 속성: 상태, 데이터, 정보 저장하는 **변수**

- **인스턴스 변수**
  
  - 각 인스턴스들이 **개인**적으로 갖는 고유한 attribute
  - 생성자 메서드(__ init __)에서 self.변수명으로 정의
  - 인스턴스가 생성된 이후 instance.변수명으로 접근 및 할당

- **class 변수**
  
  - 같은 클래스의 모든 인스턴스가 **공유**하는 같은 attribute 값
  - 클래스 선언 내부에서 정의
  - classname.변수명으로 접근 및 할당
  - 변경할 때는 항상 **클래스.클래스변수** 형식으로 변경

#### OOP method

- method : 특정 데이터 type(또는 **클래스**)의 object에 공통적으로 적용 가능한 behavior (행위, **함수**)

- **Instance Method 인스턴스 메서드**
  
  - *인스턴스 변수*를 처리, 제어. 개별행동. 개인용.
    
    - 클래스 변수, 인스턴스 변수 둘 다 사용이 가능
  
  - 클래스 내부에 정의되는 메서드의 기본
    
    - `.pop()`, `.clear()`, `.copy()`, `.index`(), `.remove`(), `.update`() 등
  
  - method 호출 시, 항상 첫 인자로 **instance** 자기**자신**인 **`self`**가 전달
    
    - `self`: 파이썬의 암묵적인 규칙 convention
  
  - **Magic(Special) Method**
    - Double underscore(= 던더)가 있는 메서드
    
    - 특정 상황에 자동으로 불리는 메서드
    
    - 객체의 특수 조작 행위를 지정(함수, 연산자 등)
      
      - **`__init__`** constructor 생성자 method
        - 인스턴스 변수들의 초기값(인스턴스의 속성)을 설정
        - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
        
      - **`__del__`** destructor 소멸자 method
        - 인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출되는 메서드
        
      - **`__str__(self)`** : 해당 객체의 print 출력 형태를 문자열 return 값으로 지정
        - print 함수를 호출할 때, 자동으로 호출
        - 어떤 인스턴스를 출력하면 `__str__`의 return 값이 출력
        
      - **`__repr__(self)`** : 객체 표현을 return
      
      - `__gt__`(self, other) : greater than 부등호 연산자
      
      - `__eq__`(self, other) : equal ==
      
      - `__doc__` :  docstring
  
- **class method**
  
  - 클래스가 사용할 메서드
  
  - 클래스는 클래스 변수만 사용. 클래스 변수를 컨트롤. 공용.
  
  - 호출 시, 첫번째 인자로 `cls`(클래스)가 전달됨
  
  - **`@classmethod`** 데코레이터를 사용하여 정의
    - @데코레이터(함수명) 형태로 함수 위에 작성
    - 함수를 어떤 함수로 *꾸며서* 새로운 기능을 부여
    - 순서대로 적용되기 때문에 작성 순서가 중요
    - 쉽게 *여러 함수*를 원하는대로 변경할 수 있음
  
- **static method**
  
  - 클래스가 사용할 메서드
  - 인스턴스와 클래스의 속성과 무관한 메서드
  - `@staticmethod` 데코레이터를 사용하여 정의
  - **호출시, 어떠한 인자도 전달되지 않음**
  - 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드
    - 객체나 클래스 상태를 수정할 수 없음
  - 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속됨
    - 주로 해당 클래스를 한정하는 용도로 사용

- **인스턴스와 클래스 간의 namespace**
  
  - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
  
  - 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

- **비교 정리**
  
    - **instance가 할 행동은 모두 instance method**로 한정 지어서 설계
    
  - 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스 (변수)를 조작. 개인용.
  
  - instance에서 클래스 메서드와 스태틱 메서드는 호출하지 않음
    
    - instance는 3가지 method 모두에게 접근
    - `cls`(클래스 자체)와 그 attribute에 접근할 필요가 있다면 **class method**로 정의
  
  - 클래스를 의미하는 cls 매개 변수를 통해 클래스 (변수)를 조작. 공용
  
  - class에서 인스턴스 메서드는 호출하지 않음
    
    - class는 3가지 메서드 모두에 접근 가능
  
  - class와 class attribute에 접근할 필요가 없다면 **static method**로 정의
    
    - 객체 상태나 클래스 상태를 수정할 수 없음
      - static method는 자동으로 전달되는 인자가 없음

## OOP의 핵심 개념

추상화, 상속, 다형성, 캡슐화

### Abstraction 추상화

**세부적인 내용은 감추고, 필요한 부분만 표현하는 것**

- 현실 세계를 프로그램 설계에 반영하기 위해 사용됩니다.
- 여러 class가 공통적으로 사용할 attribute 및 method를 추출하여 기본 class로 작성하여 활용

### Inheritance 상속

- 두 클래스 사이 **부모 - 자식 관계**를 정립하는 것

- 클래스는 상속이 가능함

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음, 코드 재사용성이 높아짐

- 파이썬의 모든 클래스는 object로부터 상속됨

- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함

- 상속관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색

- **다중 상속**
  
  - 두 개 이상의 클래스를 상속 받는 경우
    - 상속받은 모든 클래스의 요소를 활용 가능함
    - 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

- **상속 관련 함수와 메서드**
  
  - `issubclass`(*class, classinfo*)
    - class가 classinfo의 subclass면 return **True**
    
  - `isinstance`(*object, classinfo*)
    - object가 classinfo의 instance거나 subclass인 경우 return **True**
  
- **`super()`**
  
  - 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
    
    - 자식 클래스에 method를 추가로 구현할 수 있음
    
    - 초기화의 중복 제거
      
      ```python
      class Parent:
        def __init__(self, etc):
          self.etc = etc
      
      class Child(Parent):
        def __init__(self, etc, extra):
          super().__init__(etc)
          self.extra = extra
      ```

- **M**ethod **R**esolution **O**rder 메서드
  
  - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
  - 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면, 인스턴스 -> 자식 클래스 -> 부모클래스로 확장

### Polymorphism 다형성

여러 모양을 뜻하는 그리스어

**동일한 메서드가 클래스에 따라 다르게 행동**할 수 있음을 의미

즉, 서로 다른 클래스에 속해있는 객체들이 *동일한 메시지에 대해 각기 다른 방식으로 응답할 수 있음*

**Method Overriding**

- 상속받은 메서드를 **재정의**할 수도 있음
- 상속받은 클래스에서 **같은 이름의 메서드**로 덮어씀
- `__init__`,` __str__` 의 메서드를 정의하는 것 역시, 메서드 오버라이딩
  - 부모 클래스의 메서드를 실행시키고 싶은 경우 `super()`를 활용

### Encapsulation 캡슐화

객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단

파이썬에서 암묵적으로는 존재하지만, 언어적으로는 존재하지 않음

**접근제어자 종류**

- Public Access Modifier

- Protected Access Modifier

- Private Access Modifier

**Public Member**

- 언더바가 없이 시작하는 메서드나 속성들
- 어디서나 호출이 가능, 하위 클래스에서 메서드 오버라이딩을 허용
- 일반적으로 작성되는 *메서드와 속성의 대다수를 차지*

**Protected Member**

- *언더바 1개*로 시작하는 메서드나 속성들
- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
- 하위 클래스에서 메서드 오버라이딩을 허용

**Private Member**

- *언더바 2개*로 시작하는 메서드나 속성들
- 본 클래스 내부에서만 사용이 가능
- 하위클래스 상속 및 호출이 불가능 (오류)
- 외부 호출이 불가능 (오류)

**getter** 메서드와 **setter** 메서드

- 변수에 접근할 수 있는 메서드를 별도로 생성
  
  - **getter** 메서드 : 변수의 값을 *읽는* 메서드
    - **`@property`** 데코레이터를 사용
    
  - **setter** 메서드 : 변수의 값을 *설정*하는 성격의 메서드
    
    - **`@`변수`.setter`**를 사용

## 에러/예외 처리 Error/Exception Handling

소프트웨어에서 발생하는 문제를 버그라고 부름

**디버깅** de bugging

- 잘못된 프로그램을 수정하는 것

- 에러 메시지가 발생하는 경우
  
  - 해당하는 위치를 찾아 메시지를 해결

- 로직 에러가 발생하는 경우
  
  - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우

- 오류 발생 주로 *제어가 되는 시점, 조건/반복, 함수*

- `print` 함수 활용
  - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
  
- 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
  
  - breakpoint, 변수 조회 등

- [Python tutor](https://pythontutor.com/) 활용 (단순 파이썬 코드인 경우)

- 뇌컴파일, 눈디버깅

### 에러와 예외

- **Syntax Error 문법 에러**
  
  - 파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
  - 줄에러 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시
    - Invalid syntax 문법 오류
    - assign to literal 잘못된 할당
    - **E**nd **O**f **L**ine
    - **E**nd **O**f **F**ile

- **Exception 예외**
  
  - 실행 도중 예상치 못한 exception(상황)을 맞이하면, 프로그램 실행을 멈춤
    
    - 문장이나 표현식이 문법적으로 올바르더라도, 실행시 발생하는 에러
  
  - 실행 중에 감지되는 에러들을 Exception이라고 부름
  
  - 여러 type으로 나타나고, 타입이 메시지의 일부로 출력됨
  
  - 사용자 정의 예외를 만들어 관리할 수 있음
  
  - 모든 내장 예외는 **Exception** Class를 상속받아 이뤄짐
    
    > **[built-in-exceptions](https://docs.python.org/ko/3/library/exceptions.html)**
    
    - KeyboardInterrupt
      
      - 임의로 프로그램을 종료하였을 때
    
    - **ZeroDivisionError**
      
      - division by zero
    
    - **ImportError**
      
      - cannot import name from (/usr/lib/python3.9/ .py)
    
    - **ModuleNotFoundError**
      
      - No module named '
    
    - **IndexError**
      
      - index out of range
    
    - **KeyError**
      
      - 해당 키가 존재하지 않는 경우
    
    - **NameError**
      
      - name is not defined
    
    - IndentationError
      
      - expected an indented block
      - unexpected indent
    
    - **TypeError**
      
      - unsupported operand type(s) for: and
      - type doesn't define method
      - expected arguments, got
      - missing required positional arguments:
      - takes positional arguments but were given
      - must be a sequence. For dicts or sets, use sorted(d).
    
    - ValueError
      
      - invalid literal for with base 10:
      - is not in range

### 예외 처리

**try** statement / **except** clause을 이용

더 빠른 것은 `if`문

**`try`**문

- 오류가 발생할 가능성이 있는 **코드를 실행**함
- 예외가 발생되지 않으면, **except 없이 실행이 종료**

**`except`** 절

- try 문에서 예외가 발생하면 **남은 부분을 수행하지 않고**, 실행함
- 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
- **에러가 순차적으로 수행**되므로, 가장 작은 범주부터 예외 처리를 해야함
- 괄호가 있는 튜플로 여러 개의 예외를 지정 가능

`else`

- try 문에서 예외가 발생하지 않으면 실행함

`finally` (선택사항)

- 예외 발생 여부와 관계없이 반드시 실행함
- try문을 떠날 때, 최종 정리문(clean-up)

`as` 에러 메시지 처리 

- as 키워드를 활용하여, 원본 에러 메시지를 사용할 수 있음
  - 예외를 다른 이름에 대입
  - **except** 예외 **as** err:

**Exception Raising 예외 발생시키기**

- **raise**를 통해 예외를 강제로 발생 가능
  - **`raise`** <에러>('메시지')

> [`assert` 문](https://docs.python.org/ko/3/reference/simple_stmts.html#the-assert-statement)

- 예외를 발생

- 일반적으로 상태를 검증하는데(디버깅 용도)로 사용

- 검증식이 거짓일 경우, AssertionError가 발생
  
  ```python
  assert False, 'ERROR MESSAGE"
  ```