# JavaScript_Basic

## 1. JavaScript 시작하기

### JavaScript를 배워야 하는 이유

**Web 기술의 기반이 되는 언어**

- HTML 문서의 콘텐츠를 **동적으로 변경**할 수 있는 언어

- **다양한 분야로 확장이 가능한 언어**가 됨

### JavaScript의 역사

- Web을 조작하기 위한 언어인 만큼 **Web Browser와도 깊은 연관 관계가 있음**

**웹 브라우저의 역할**

- **HTML/CSS/JavaScript를 이해한 뒤 해석**해서 사용자에게 하나의 화면으로 보여줌

**정리**

- 웹 브라우저는 JavaScript를 해석하는 엔진을 가지고 있음
- 현재의 JavaScript는 이제 시장에서 자리를 잡은 언어이며, 개발에서 큰 축을 담당하는 언어
- 더 이상 jQuery 등의 라이브러리를 사용할 필요가 없음(모든 웹 브라우저가 표준안을 따름)
- 특히, Chrome의 V8의 경우 Javascript를 번역하는 속도가 매우 빠름
  - node.JS, react.JS, electron 등의 내부 엔진으로 사용
  - back-end, mobile, desktop app 등을 모두 JavaScript로 개발이 가능해진

### JavaScript 실행환경 구성

**1. Web Browser로 실행하기**

- HTML 파일에 포함시키기

```html
<body>
  <script>
    console.log('hello, javascript')
  </script>
</body>
```

- 외부 JavaScript 파일 사용하기

  - .js 확장자를 가진 파일에 JavaScript를 작성하고, 해당 파일을 HTML에 포함 가능


  ```html
  </body>
  <script src="hello.js"></script>
  </html>
  ```

- Web Browser에서 바로 입력하기

  - 웹 브라우저의 console에서 바로 JavaScript를 입력해도 된다
  - 특별하게 웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들을 **Vanilla JavaScript**라고 부름
  - 순수한 JavaScript라는 의미(모든 아이스크림의 순정은 Vanilla라는 어원)


2. **Node.JS로 실행하기**
   - 웹 브라우저를 이용하지 않고 JavaScript를 실행할 수 있음

## 2. JavaScript 기초 문법

### **코드 작성법**

**semicolon 세미콜론**

- 자바스크립트는 세미콜론을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
  - ASI (Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)

**들여쓰기와 코드 블럭**

- **JavaScript는 2칸** 들여쓰기를 사용
- **block 블럭**은 if, for, 함수에서 **{ }** 중괄호 내부를 말함
  - JavaScript는 { } 중괄호를 사용해 코드 블럭을 구분

**코드 스타일 가이드**

- Airbnb Style Guide

**주석**

- `//` 한줄 주석과 `/* */` 여러 줄 주석

### 변수와 식별자

**식별자 정의와 특징**

- identifier 식별자는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, $ 달러 또는 _ 밑줄로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능

**식별자 정의와 특징**

- camelCase 카멜 케이스 (lower-cammel–case)
  - 변수, 객체, 함수에 사용
- PascalCase 파스칼 케이스 (upper-camel-case)
  - 클래스, 생성자에 사용
- SNAKE_CASE 대문자 스네이크 케이스
  - constants 상수에 사용

**변수 선언 키워드**

1. `let`
   - 블록 스코프 지역 변수를 선언 (추가로 동시에 값을 초기화)
   - 재할당 가능 & 재선언 불가능
   - 블록 스코프를 갖는 지역 변수를 선언, 선언과 동시에 원하는 값으로 초기화 할 수 있음
2. `const`
   - 블록 스코프 읽기 전용 상수를 선언 (추가로 동시에 값을 초기화)
   - 재할당 불가능 & 재선언 불가능
   - 선언 시 반드시 초기값을 설정 해야 하며, 이후 값 변경이 불가능
3. `var`
   - 변수를 선언 (추가로 동시에 값을 초기화)
   - 재할당 가능 & 재선언 가능
   - ES6 이전에 변수를 선언할 때 사용되던 키워드
   - **호이스팅** 되는 특성으로 인해 예기치 못한 문제 발생 가능
     - 따라서 ES6 이후부터는 var 대신 **const와 let을 사용하는 것을 권장**
   - function scope 함수 스코프를 가짐
   - **변수 선언 시 var, const, let 키워드 중 하나를 사용하지 않으면 자동으로 var로 선언됨**

**변수 선언 키워드 정리**

- 어디에 변수를 쓰고 상수를 쓸지 결정하는 것은 프로그래머의 몫
- Airbnb 스타일 가이드에서는 기본적으로 **const 사용을 권장**
  - 재할당해야 하는 경우만 **let**

### 데이터 타입

- JavaScript의 모든 값은 특정한 데이터 타입을 가짐
- 크게 **Primitive type 원시 타입**과 **Refernece type 참조타입**으로 분류됨

**Number**

- 정수 또는 실수형 숫자를 표현하는 자료형
- **NaN**
  - Not-A-Number 숫자가 아님
  - **Number.isNan()** 의 경우 주어진 값의 유형이 Number이고 값이 Nan이면 true, 아니면 false를 반환
- **NaN을 반환하는 경우**
  1. 숫자로서 읽을 수 없음
  2. 결과가 허수인 수학 계산식
  3. 피연산자가 NaN
  4. 정의할 수 없는 계산식
  5. 문자열을 포함하면서 덧셈이 아닌 계산식

**String**

- 문자열을 표현하는 자료형
- 작은 따옴표 또는 큰 따옴표 모두 가능
- 덧셈을 통해 문자열 붙일 수 있음
- Quote를 사용하면 선언 시 줄 바꿈이 안 됨
- 대신 escape sequence를 사용할 수 있기 때문에 \n 를 사용해야 함
- **Tempate Literal**을 사용하면 줄바꿈이 되며, 문자열 사이에 변수도 삽입도 가능
- (단, escape sequence를 사용할 수 없다)

**Template literals 템플릿 리터럴**

- 내장된 표현식을 허용하는 문자열 작성 방식
- ES6+ 부터 지원
- Backtick(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있는 이점이 생김
- 표현식을 넣을 수 있는데, 이는 $ 와 중괄호 (`$ {expression}`) 로 표기

**Empty Value**

- 값이 존재하지 않음을 표현하는 값으로 JavaScript에서는 **null**과 **undefined** 가 존재
- 동일한 역할을 하는 이 두개의 키워드가 존재하는 이유는 단순한 JavaScript의 설계 실수
- 큰 차이를 두지 말고 interchangeable 하게 사용할 수 있도록 권장함

**null**

- 변수의 **값이 없음을 의도적으로 표현**할 때 사용하는 데이터 타입

**undefined**

- 값이 정의되어 있지 않음을 표현하는 값
- 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

**null과 undefeined**

- null과 undefined의 가장 대표적인 차이점은 **typeof** 연산자를 통해 타입을 확인 했을 때 가능함
- null 이 원시 타입임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 지금까지 해결하지 못한 것

**Boolean**

- true와 false
- 참과 거짓을 표현하는 값
- 조건문 또는 반복문에서 유용하게 사용
  - 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 **자동 형변환 규칙**에 따라 true 또는 false로 변환됨

**ToBoolean Conversions (자동 형변환)**

> https://tc39.es/ecma262/#sec-toboolean

| 데이터 타입 | false      | true             |
| ----------- | ---------- | ---------------- |
| undefined   | 항상 거짓  | X                |
| null        | 항상 거짓  | X                |
| Number      | 0, -0, NaN | 나머지 모든 경우 |
| String      | 빈 문자열  | 나머지 모든 경우 |
| Object      | X          | 항상 참          |

### 연산자

**비교 연산자**

- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - 소문자가 대문자보다 더 크다

**동등 연산자 `==`**

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 **암묵적 타입 변환**을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- **예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음**

**일치 연산자 `===`**

- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 **암묵적 타입 변환이 발생하지 않음**
  - 엄격한 비교 - 두 비교 대상의 타입과 값 모두 같은 지 비교하는 방식

**논리 연산자**

- and 연산은 `&&` 연산자
- or 연산은 `||` 연산자
- not 연산은 `!` 연산자

**Ternary Operator 삼항 연산자**

- 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 앞의 조건식이 참이면 : (콜론) 앞의 값이 반환되며, 그 반대일 경우 : 뒤의 값이 반환되는 연산자
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능

### 조건문

**조건문의 종류와 특징**

- **if** statement
  - 조건 표현식의 결과값을 boolean 타입을 변환 후 참/거짓을 판단
    - 조건은 **condition 소괄호** 안에 작성
    - 실행할 코드는 **{ } 중괄호** 안에 작성
    - 블록 스코프 생성
- **switch** statement
  - 조건 표현식의 결과값이 **어느 값(case)에 해당하는지 판별**
  - 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
    - 조건이 많아질 경우 if문보다 가독성이 나올 수 있음
  - expression 표현식의 결과값을 이용한 조건문
  - 표현식의 결과값과  case문의 오른쪽 값을 비교
  - break 및 default문은 [선택적]으로 사용 가능
  - break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
  - 블록 스코프 생성
  - Fall-through
    - break를 작성하면 의도한대로 동작

**if / switch**

- 조건이 많은 경우 switch문을 통해 가독성 향상을 기대할 수 있음
- 일반적으로 중첩 else if문은 유지보수하기 힘들다는 문제도 있음

### 반복문

**반복문 종류**

- while

  - 조건문이 참이기만 하면 문장을 계속해서 수행

    ```js
    while (조건문) {
        
    }
    ```

- for

  - 특정한 조건이 거짓으로 판별될 때까지 반복

    ```js
    for ([초기문]; [조건문]; [증감문]) {
        
    }
    
    for (let i = 0; i < 6; i ++) {
        console.log(i)
    }
    ```

    1. 반복문 진입 및 변수 i 선언
    2. 조건문 평가 후 코드 블럭 실행
    3. 코드 블록 싱행 이후 i 값 증가

- for…in

  - object **객체**의 속성을 순회할 때 사용

  - 속성 이름을 통해 반복

  - **객체** 순회 적합

  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음

    ```js
    for (variable in object) {
        
    }
    
    const fruits = { a: 'apple', b: 'banana' }
    
    // for (let key in fruits) {
    for (const key in fruits) {
        console.log(key)
        console.log(fruits[key])
    }
    ```

- for…of

  - 반복 가능한 객체를 순회할 때 사용

  - 속성 값을 통해 반복

  - iterable 순회 적합

  - iterable 반복 가능한 객체의 종류 : Array, Set, String 등

    ```js
    for (variable of object) {
        
    }
    
    const numbers = [0, 1, 2, 3]
    
    // for (let number of numbers) {
    for (const number of numbers) {
        console.log(number)
    }
    ```

**[참고] for…in, for…of 와 const**

- 일반적인 for문의 경우에는 최초 정의한 i 를 재할당 하면서 사용하기 때문에 const를 사용하면 에러 발생
- 다만 for…in, for…of 의 경우에는 재할당이 아니라, 매 반복 시 해당 변수를 새로 정의하여 사용하므로 에러가 발생하지 않음

**조건문과 반복문 정리**

| 키워드 | 종류   | 연관 키워드          | 스코프      |
| ------ | ------ | -------------------- | ----------- |
| if     | 조건문 | -                    | 블록 스코프 |
| switch | 조건문 | case, break, default | 블록 스코프 |
| while  | 반복문 | break, continue      | 블록 스코프 |
| for    | 반복문 | break, continue      | 블록 스코프 |
| for…in | 반복문 | 객체 순회            | 블록 스코프 |
| for…of | 반복문 | iterable 순회        | 블록 스코프 |

## 3. Function

참조 타입 중 하나로써 function 타입에 속함

JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분됨

- function declaration 함수 선언식
- function expression 함수 표현식

### 함수의 정의

**function declaration 함수 선언식**

```js
function 함수명() {
    
}
```

**function expression 함수 표현식**

- 표현식 내에서 함수를 정의하는 방식
- 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의가능

```js
변수키워드 함수명 = function () {
    
}
```

- 표현식에서 함수 이름을 명시하는 것도 가능
- 다만 이 경우 함수 이름은 호출에 사용 되지 못하고 디버깅 용도로 사용됨

**Default arguments 기본 인자**

- 인자 작성 시 `=` 문자 뒤 기본 인자 선언 가능

  ```js
  const greeting = function (name = 'Anonymous') {
    return `Hi ${name}`
  }
  
  greeting()
  ```

**매개변수와 인자의 개수 불일치 허용**

- 매개변수보다 인자의 개수가 많을 경우

  ```js
  const twoArgs = function (arg1, arg2) {
    return [arg1, arg2]
  }
  
  twoArgs(1, 2, 3)  // [1, 2]
  ```

- 매개변수보다 인자의 개수가 적을 경우

  ```js
  const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
  }
  
  threeArgs(1, 2) // [1, 2, undefined]
  ```

**Spread syntax (…)**

- 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를 배열의 경우는 요소, 함수의 경우는 인자로 확장할 수 있음

  1. 배열과의 사용

     ```js
     let parts = ['shoulders', 'knees']
     let lyrics = ['head', ...parts, 'and', 'toes']
     ```

  2. 함수와의 사용 (**Rest parameters**)

     - The rest parameter syntax 를 사용하여 정해지지 않은 수의 매개변수를 배열로 받을 수 있음

     ```js
     const restOpr = function (arg1, arg2, ...restArgs) {
       return [arg1, arg2, restArgs]
     }
     
     restArgs(1, 2, 3, 4, 5)  // [1, 2, [3, 4, 5]]
     ```

### 선언식과 표현식

공통점: **데이터 타입**, 함수 구성 요소 (이름, 매개변수, 바디)

**함수의 타입**

- 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

**호이스팅 - 선언식**

- 함수 선언식으로 정의한 함수는 var 로 정의한 변수처럼 호이스팅이 발생
- 즉 함수 호출 이후에 선언해도 동작

**호이스팅 - 표현식**

- 반면 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

**선언식과 표현식 정리**

|        | declaration 선언식                  | expression 표현식                 |
| ------ | ----------------------------------- | --------------------------------- |
| 차이점 | 익명 함수 불가능<br />호이스팅 있음 | 익명 함수 가능<br />호이스팅 없음 |
| 비고   |                                     | Airbnb Style Guide 권장 방식      |

### Arrow Function

**화살표 함수**

- 함수를 비교적 간결하게 정의할 수 있는 문법

- function 키워드와 중괄호를 이용한 구문을 짧게 사용하기 위해 탄생

  1. **function 키워드 생략가능**
  2. 함수의 매개변수가 하나뿐이라면 `( )` 도 생략 가능
     - **명확성과 일관성을 위해 항상 인자 주위에는`()` 괄호를 포함하는 것을 권장** 
  3. 함수의 내용이 한 줄이라면 `{ }` 와 `return` 도 생략 가능

- 화살표 함수는 항상 익명 함수

  - == 함수 표현식에서만 사용가능

  ```js
  // 1. function 키워드 삭제
  const arrow = (name) => { return `hello, ${name}` }
  
  // 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 { } & return 삭제 가능
  const arrow = (name) => `hello, ${name}`
  ```

  ```js
  // 인자가 없다면? () or _ 로 표시 가능.
  let noArgs = () => 'No args'
  noArgs = _ => 'No args'
  
  // object 를 return 한다면, return 을 명시적으로 적어준다.
  let returnObject = () => { return { key: 'value'} }
  
  // return 을 적지 않으려면 괄호를 붙여야 한다.
  returnObject = () => ({ key: 'value' })
  ```

**즉시 실행 함수 (IIFE, Immediaely Invoked Function Expression)**

- 선언과 동시에 실행되는 함수

- 함수의 선언 끝에 `( )` 를 추가하여 선언되자 마자 실행하는 형태

- `( )` 에 값을 넣어 인자로 넘겨줄 수 있음

- 즉시 실행 함수는 선언과 동시에 실행되기 때문에 같은 함수를 다시 호출할 수 없음

- 이러한 특징을 살려 초기화 부분에 많이 사용

- 일회성 함수이므로 익명함수로 사용하는 것이 일반적

  ```js
  (function(num) { return num ** 3 })(2) // 8
  (num => num **3)(2) // 8
  ```

## 4. Array_Object

- JavaScript의 데이터 타입 중 refernce 참조 타입에 해당 하는 타입은 **array**와 **object**이며, 객체라고 말함
- 객체는 속성들의 collection 모음

### Array

- 키와 속성들을 담고 있는 참조 타입의 **object 객체**

- 순서를 보장하는 특징이 있음

- 주로 대괄호(**[]**)를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능

- 배열의 길이는 **array.length** 형태로 접근 가능

  ```js
  const numbers = [1, 2, 3, 4, 5]
  ```

### Array method 기초

| 메서드          | 설명                                                 | 비고                     |
| --------------- | ---------------------------------------------------- | ------------------------ |
| reverse         | **원본 배열**의 요소들의 순서를 반대로 정렬          |                          |
| push & pop      | 배열의 **가장 뒤에** 요소를 **추가 또는 제거**       |                          |
| unshift & shift | 배열의 **가장 앞에** 요소를 **추가 또는 제거**       |                          |
| includes        | 배열에 특정 값이 존재하는지 판별 후 **참/거짓 반환** |                          |
| indexOf         | 배열에 특정 값이 존재하는지 판별 후 **인덱스 반환**  | 요소가 없을 경우 -1 반환 |
| join            | 배열의 **모든 요소를 구분자를 이용하여 연결**        | 구분자 생략 시 쉼표 기준 |

### Array method 심화

**Array Helper Methods**

- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 **callback 함수**를 받는 것이 특징
  - **callback 함수**: 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수

| 메서드      | 설명                                                         | 비고         |
| ----------- | ------------------------------------------------------------ | ------------ |
| **forEach** | 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행               | 반환 값 없음 |
| **map**     | **콜백 함수의 반환 값**을 요소로 하는 **새로운 배열 반환**   |              |
| **filter**  | **콜백 함수의 반환 값이 참인 요소들만** 모아서 **새로운 배열을 반환** |              |
| **reduce**  | **콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환**    |              |
| find        | 콜백 함수의 **반환 값이 참이면 해당 요소를 반환**            |              |
| some        | 배열의 **요소 중 하나라도 판별 함수를 통과**하면 참을 반환   |              |
| every       | 배열의 **모든 요소가 판별 함수를 통과**하면 참을 반환        |              |

**Array Helper Methods - forEach**

```js
array.forEach((element, index, array) => {
    
})
```

- array.forEach(callback(element[, index[,array]]))
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행
  - 콜백 함수는 3가지 매개변수로 구성
    1. element: 배열의 요소
    2. index: 배열 요소의 인덱스
    3. array: 배열 자체
- return 반환 값 없음

```js
const colors = ['red', 'blue', 'green']

printFunc = function (color) {
  console.log(color)
}
colors.forEach(printFunc)

colors.forEach(function (color) {
  console.log(color)
})

colors.forEach((color) => console.log(color))
```

**Array Helper Methods - map**

```js
array.map((element, index, array) => {
    
})
```

- array.map(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환** 
- 기존 배열 전체를 다른 형태로 바꿀 때 유용

```js
const numbers = [1, 2, 3]

const doubleFunc = function (number) {
  return number * 2
}

const doubleNumbers = numbers.map(doubleFunc)
console.log(doubleNumbers)

const doubleNumbers = numbers.map(function (number) {
  return number * 2
})
console.log(doubleNumbers)

const doubleNumbers = numbers.map((number) => number * 2)
console.log(doubleNumbers)
```

**Array Helper Methods - filter**

```js
array.filter((element, index, array)) => {
    
})
```

- array.filter(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환**
- 기존 배열의 요소들을 필터링할 때 유용

```js
const products = [
  { name: 'cucumber', type: 'vegetable' },
  { name: 'banana', type: 'fruit' },
  { name: 'carrot', type: 'vegetable' },
  { name: 'apple', type: 'fruit' },
]

const fruitFilter = function (product) {
  return product.type === 'fruit'
}

const fruits = products.filter(fruitFilter)

console.log(fruits)

const fruits = products.filter(function (product) {
  return product.type === 'fruit'
})

const fruits = products.filter((product) => product.type === 'fruit')
```

**Array Helper Methods - reduce**

```js
array.reduce((acc, element, index, array) => {
    
}, initialValue)
```

- array.reduce(callback(acc, element, [index[, array]])[, initialValue])
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 결과 값을 반환.
- 즉, 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용(총합, 평균 등)
- map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
- reduce 메서드의 주요 매개변수
  - acc
    - 이전 callback 함수의 반환 값이 누적되는 변수
  - initialValue(optional)
    - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
- reduce의 첫번째 매개변수인 콜백함수의 첫번째 매개변수(`acc`)는 누적된 값(전 단계 까지의 결과)
- reduce의 두번째 매개변수인 `initialValue`는 누적될 값의 초기값, 지정하지 않을 시 첫번째 요소의 값이 됨
- **빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생**

```js
const tests = [90, 90, 80, 77]

const sum = tests.reduce(function (total, x) {
  return total + x
})

const sum = tests.reduce((total, x) => total + x)

const sum = tests.reduce((total, x) => total + x) / tests.length
```

**Array Helper Methods - find**

```js
array.find((element, index, array)) {
    
}
```

- array.find(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
- 찾는 값이 배열에 없으면 undefined 반환

```js
const avengers = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
]

const avenger = avengers.find(function (avenger) {
  return avenger.name === 'Tony Stark'
})

const avenger = avengers.find((avenger) => avenger.name === 'Tony Stark')
```

**Array Helper Methods - some**

```js
array.some((element, index, array) => {
    
})
```

- array.some(callback(element[, index[, array]]))
- 배열의 **요소 중 하나라도** 주어진 판별 함수를 통과하면 참을 반환
- 모든 요소가 통과하지 못하면 거짓 반환
- 빈 배열은 항상 false 반환

```js
const arr = [1, 2, 3, 4, 5]

const result = arr.some((elem) => elem % 2 === 0)
```

**Array Helper Methods - every**

```js
array.every((element, index, array) => {
    
})
```

- array.every(callback(element[, index[, array]]))
- 배열의 **모든 요소가** 주어진 판별 함수를 통과하면 참을 반환
- 하나의 요소라도 통과하지 못하면 거짓 반환
- 빈 배열은 항상 true 반환

```js
const arr = [1, 2, 3, 4, 5]

const result2 = arr.every((elem) => elem % 2 === 0)
```

**배열 순회 비교**

```js
const chars = ['A', 'B', 'C', 'D']

// for loop
for (let idx = 0; idx < chars.length; idx++) {
  console.log(idx, chars[idx])
}

// for ... of
for (const char of chars) {
  console.log(char)
}

// forEach
chars.forEach((char, idx) => {
  console.log(idx, char)
})

chars.forEach(char => {
  console.log(char)
})
```

| 방식        | 특징                                                         | 비고                         |
| ----------- | ------------------------------------------------------------ | ---------------------------- |
| for loop    | 모든 브라우저 환경에서 지원<br />인덱스를 활용하여 배열의 요소에 접근<br />break, continue 사용 가능 |                              |
| for…of      | 일부 오래된 환경에서 **지원X**<br />인덱스 없이 배열의 요소에 바로 접근 가능<br />break, continue 사용 가능 |                              |
| **forEach** | 대부분의 브라우저 환경에서 지원<br />break, continue 사용 **불가능** | Airbnb Style Guide 권장 방식 |

### Object

- 객체는 property 속성의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현

- key는 문자열 타입만 가능
  - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value는 모든 타입(함수 포함) 가능
- 객체 요소 접근은 점(.) 또는 대괄호([])로 가능
  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```js
const me = {
  name: 'jack',
  phoneNumber: '0102345678',
  'samsung products': {
    buds: 'Galaxy Buds pro',
    galaxy: 'Galaxy s99',
  },
}

console.log(me.name)
console.log(me['samsung products'].buds)
```

### Object 관련 문법

**객체 관련 ES6 문법 익히기**

- ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능
  1. **속성명 축약**
  2. 메서드명 축약
  3. 계산된 속성명 사용하기
  4. 구조 분해 할당
  5. 객체 전개 구문(Spread Operator)

**1. 속성명 축약**

- 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 **축약** 가능

```js
const books = ['Learning JavaScript', 'Learning Python']
const magazines = ['Vogue', 'Science']

const bookShop = {
  books,
  magazines,
}
console.log(bookShop)
```

**2. 메서드명 축약**

- 메서드 선언 시 function 키워드 생략 가능

```js
const obj = {
  greeting() {
    console.log('Hi!')
  }
}

obj.greeting()
```

**3. 계산된 속성 (computed property name)**

- 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

```js
const key = 'country'
const value = ['한국', '미국', '일본', '중국']

const myObj = {
  [key]: value,
}

console.log(myObj)
console.log(myObj.country)
```

**4. 구조 분해 할당 (destructing assignment)**

- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

```js
const userInformation = {
  name: 'kim',
  userId: 'Student1234',
  phoneNumber: '010-1234-1234',
  email: 'student@student.com'
}

const name = userInformation.name
const { userId } = userInformation
const { phoneNumber, email } = userInformation
```

**5. Spread syntax (…)**

- 배열과 마찬가지로 전개구문을 사용해 객체 내부에서 객체 전개 가능
- 얕은 복사에 활용 가능

```js
const obj = {b: 2, c: 3, d: 4}
const newObj = {a: 1, ...obj, e: 5}

console.log(newObj)
```

**JavaScriptON (JavaScript Object Notation)**

- Key-Value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 Object는 그 자체로 타입이고, JavaScriptON은 형식이 있는 문자열
- **즉, JavaScriptON을 Object로 사용하기 위해서는 변환 작업이 필요**

JavaScriptON (JavaScript Object Notation) 변환

```js
const JavaScriptObject = {
  coffee: 'Americano',
  iceCream: 'Cookie and cream',
}
```

```js
const objToJavaScripton = JavaScriptON.stringify(JavaScriptObject)

console.log(objToJavaScripton)
console.log(typeof objToJavaScripton)

const JavaScriptonToObj = JavaScriptON.parse(objToJavaScripton)

console.log(JavaScriptonToObj)
console.log(typeof JavaScriptonToobj)
```

## finish

- JavaScrpit 기초 문법

  - 세미콜론

  - 들여쓰기와 코드 블럭

  - 스타일 가이드

  - 변수와 식별자
    - 타입과 연산자
      - 원시 자료형

  - 조건문

  - 반복문

- 함수
  - 선언식과 표현식
  - 화살표 함수
- Array와 Object
  - 배열
    - Array Helper Method
  - 객체
    - ES6+ 객체 문법
