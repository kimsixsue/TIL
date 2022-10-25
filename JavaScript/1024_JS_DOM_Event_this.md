[JS_DOM_Event_this](#js_dom_event_this)

1. [DOM](#1-dom)

   + [DOM](#dom)

   + [DOM 조작](#dom-조작)

2. [Event](#2-event)

   + [Event Intro](#event-intro)

   + [Event 실습](#event-실습)

   + [Event 취소](#event-취소)

   + [Event 취소 실습](#event-취소-실습)

   + [Event 종합 실습](#event-종합-실습)

3. [this](#3-this)

- [finish](#finish)

#  JS_DOM_Event_this

## 1. DOM

JavaScript는 웹 페이지에서 다양한 기능을 구현하는 스크립트 언어

### DOM

**Browser APIs**

- 웹 브라우저에 내장된 API로, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나, 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함
- JavaScript로 Browser API들을 사용해서 여러가지 기능을 사용할 수 있음

**DOM**

- Document Object Model 문서 객체 모델
- 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
  - 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움
  - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음
- HTML 문서를 구조화 하여 각 요소를 object 객체로 취급
- 단순한 속성 접근, 메서드 화룡 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능

- DOM은 문서를 논리 트리로 표현
- DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음
- 웹 페이지는 일종의 document 문서
- 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
- DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
- DOM은 웹 페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음

**DOM에 접근하기**

- DOM을 사용하기 위해 특별히 해야 할 일은 없음
- 모든 웹 브라우저는 스크립트 언어가 손쉽게 웹 페이지의 요소에 접근할 수 있도록 만들기 위해 DOM 구조를 항상 사용
- "DOM의 주요 객체"들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음

**DOM의 주요 객체**

- **window** object
  - DOM을 표현하는 창
  - 가장 최상위 객체 ( 작성 시 생략 가능)
  - 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄
- **document** object
  - 브라우저가 불러온 웹 페이지
  - 페이지 컨텐츠의 진입점 역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함하고 있음

### DOM 조작

- Document가 제공하는 기능을 사용해 웹 페이지 문서 조작하기
- DOM 조작 순서
  1. **선택** Select
  2. **조작** Manipulation
     - 생성, 추가, 삭제 등

**선택 관련 메서드**

- document`.querySelector`(selector)
  - 제공한 선택자와 일치하는 element 한 개 선택
  - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null 반환)
- document`.querySelectorAll`(selector)
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  - 제공한 CSS selector를 만족하는 NodeList를 반환

**조작 관련 메서드 (생성)**

- document`.createElement`(tagName)
  - 작성한 tagName의 HTML 요소를 생성하여 반환

**조작 관련 메서드 (입력)**

- Node`.innerText`
  - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)
  - 사람이 읽을 수 있는 요소만 남김
  - 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨

 **조작 관련 메서드 (추가)**

- Node`.appendChild()`
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
  - 한번에 오직 하나의 Node만 추가할 수 있음
  - 추가된 Node 객체를 반환
  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동

**조작 관련 메서드 (삭제)**

- Node`.removeChild()`
  - DOM에서 자식 Node를 제거
  - 제거된 Node를 반환

**조작 관련 메서드 (속성 조회 및 설정)**

- Element`.getAttribute`(attributeName)
  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
- Element`.setAttribute`(name, value)
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

## 2. Event

- **Event**란 프로그래밍하고 있는 시스템에서 일어나는 action 사건 혹은 occurrence 발생인데, 우리가 원한다면 그것들에 어떠한 방식으로 응답할 수 있도록 시스템이 말해주는 것

### Event Intro

**`Event` object**

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- Event 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고, 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음

1. DOM 요소는 Event를 받고("**수신**")
2. 받은 Event를 "**처리**"할 수 있음
   - Event 처리는 주로 `addEventListener()`라는 Event handler 처리기를 사용해 다양한 html 요소에 "**부착**"하게 됨

**Event handler - `addEventListner()`**

```js
// 대상에.(특정 Event가 발생하면, 할 일을 등록하자)
EventTarget.addEventListener(type, listener)
```

- **EventTraget.addEventListner(type, listner[, options])**

  - **~ 하면 ~ 한다.**

  - 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정

  - Event를 지원하는 모든 객체를 EventTarget 대상으로 지정 가능

  - **type**

    - 반응 할 Event 유형을 나타내는 대소문자 구분 문자열

    - input, click, submit

      > https://developer.mozilla.org/docs/Web/Events

  - **listener**
    - 지정된 타입의 Event를 수신할 객체
    - JavaScript function 객체(콜백 함수)여야 함
    - 콜백 함수는 발생한 Event의 데이터를 가진 Event 기반 객체를 유일한 매개변수로 받음

### Event 실습

```js
let countNumber = 0
const btn = document.querySelector('#btn')
console.log(btn)
btn.addEventListener('click', function() {
  console.log('버튼 클릭')
  countNumber += 1
  const counter = document.querySelector('#counter')
  counter.innerText = countNumber
})
```

```js
const btn = document.createElement('button')
btn.innerText = '로그 출력'

const bodyTag = document.querySelector('body')
bodyTag.appendChild(btn)

btn.addEventListener('click', function() {
  console.log('버튼을 클릭하였습니다!')
})
```

```js
const textInput = document.querySelector('#text-input')
textInput.addEventListener('input', function (event) {
  // console.log(event)
  console.log(event.target) // == textInput
  console.log(event.target.value)
  const pTag = document.querySelector('p')
  pTag.innerText = event.target.value
})
```

```js
const input = document.querySelector('input')
input.addEventListener('input', function(event) {
  const h1Tag = document.querySelector('h1')
  h1Tag.innerText = event.target.value
})
const btn = document.querySelector('#btn')
btn.addEventListener('click', function() {
  const h1 = document.querySelector('h1')
  h1.classList.toggle('blue')
})
```

### Event 취소

**event`.preventDefault()`**

- 현재 Event의 기본 동작을 중단
- HTML 요소의 기본 동작을 작동하지 않게 막음

### Event 취소 실습

```js
const h1 = document.querySelector('h1')
h1.addEventListener('copy', function(event) {
  event.preventDefault()
  alert('복사 할 수 없습니다.')
})
```

### Event 종합 실습

> https://lodash.com/

``` js
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
<script>
const button = document.querySelector('#lotto-btn')
button.addEventListener('click', function(event) {
  const ballContainer = document.createElement('div')
  ballContainer.classList.add('ball-container')

  const numbers = _.sampleSize(_.range(1, 46), 6)

  numbers.forEach((number)) => {
    const ball = document.createElement('div')
    ball.innerText = number
    ball.classList.add('ball')
    ballContainer.appendChild(ball)
  }
  const resultDiv = document.querySelector('#result')
  resultDiv.appendChild(ballContainer)
})
</script>
```

```js
const formTag = document.querySelector('form')

const addTodo = function (event) {
  event.preventDefault()
  const inputTag = document.querySelector('.inputData')
  const data = inputTag.value

  if (data.trim()) {
    const liTag = document.createElement('li')
    liTag.innerText = data
    const ulTag = document.querySelector('ul')
    ulTag.appendChild(liTag)
    event.target.reset()
  } else {
    alert('할 일을 입력하세요.')
  }
}
formTag.addEventListener('submit', addTodo)
```

```js
const aTag = document.createElement('a')
aTag.setAttribute('href','https://www.google.com/')
aTag.innerText = 'GOOGLE'
const bodyTag = document.querySelector('body')
bodyTag.appendChild(aTag)

aTag.addEventListener('click', function (event) {
  event.preventDefault()
})
```



## 3. this

**this**

- 어떠한 object를 가리키는 키워드
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
- JavaScript는 해당 **함수 호출 방식**에 따라 this에 바인딩 되는 객체가 달라짐
- 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수를 호출할 때 **함수가 어떻게 호출 되었는지에 따라 동적으로 결정**됨

**this INDEX**

1. 전역 문맥에서의 this
2. 함수 문맥에서의 this
   - 단순 호출
   - Method (객체의 메서드로서)
   - Nested

**전역 문맥에서의 this**

- 브라우저의 전역 객체인 windows를 가리킴
  - 전역객체는 모든 객체의 유일한 최상위 객체를 의미

**함수 문맥에서의 this**

- 함수의 this 키워드는 다른 언어와 조금 다르게 동작
  - this의 값은 **함수를 호출한 방법에 의해 결정**됨
  - 함수 내부에서 this의 값은 함수를 호출한 방법에 의해 좌우됨

1. 단순 호출
   - 전역 객체를 가리킴
   - 전역은 브라우저에서는 window, Node.js는 global을 의미함
2. Method (Function in Object, 객체의 메서드로서)
   - 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩
3. Nested (Function 키워드)
   - forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴
   - 단순 호출 방식으로 사용되었기 때문
   - 이를 해결하기 위해 등장한 함수 표현식이 바로 "화살표 함수"
4. Nested (화살표 함수)
   - 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴
   - 화살표 함수에서 this는 자신을 감싼 정적 범위
   - 자동으로 한 단계 상위의 scope의  context를 바인딩

**화살표 함수**

- 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 가리킴 (Lexical scope this)
- **Lexical scope**
  - 함수를 어디서 호출하는지가 아니라 **어디에 선언**하였는지에 따라 결정
  - Static scope 라고도하며 대부분의 프로그래밍 언어에서 따르는 방식
- 따라서 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장

**this와 addEventListener**

- addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우, addEventListener를 호출한 대상(event.target)을 뜻함
- 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩 됨
- "addEventListener 의 콜백 함수는 function 키워드를 사용하기"

## finish

- DOM
  - DOM 조작
- Event
  - addEventListener
- this
  - "function" vs "arrow function"
