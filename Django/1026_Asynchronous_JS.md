[Asynchronous_JS](#asynchronous_js)

1. [동기와 비동기](#1-동기와-비동기)
   - [동기 Synchronous](#동기-synchronous)
   - [비동기 Asynchronous](#비동기-asynchronous)
2. [JavaScript의 비동기 처리](#2-javascript의-비동기-처리)
3. [Axios 라이브러리](#3-axios-라이브러리)
   - [Axios 기본 구조](#axios-기본-구조)
4. [Callback과 Promise](#4-callback과-promise)
   - [콜백 함수 Callback Function](#콜백-함수-callback-function)
   - [Promise 프로미스](#promise-프로미스)
5. [AJAX](#5-ajax)
   - [비동기 적용하기](#비동기-적용하기)

- [finish](#finish)

# Asynchronous_JS

JavaScript에서의 비동기 처리

## 1. 동기와 비동기

### 동기 Synchronous

- 모든 일을 **순서대로 하나씩** 처리하는 것
- 순서대로 처리한다 == 이전 작업이 끝나면 다음 작업을 시작한다
- 요청과 응답을 동기식으로 처리한다면, 요청을 보내고 응답이 올때까지 기다렸다가 다음 로직을 처리

### 비동기 Asynchronous

- 작업을 시작한 후 **결과를 기다리지 않고** 다음 작업을 처리하는 것 (병렬적 수행)
- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

> https://developer.mozilla.org/ko/docs/Web/API/setTimeout

**비동기를 사용하는 이유**

- **사용자 경험**
  - 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨
  - **비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로**, 사용자 경험에 긍정적인 효과를 볼 수 있음

## 2. JavaScript의 비동기 처리

**Single Thread 언어, JavaScript**

- **JavaScript는 한번에 하나의 일만 수행할 수 있는 Single Thread 언어**로 동시에 여러 작업을 처리할 수 없음
- **JavaScript는 하나의 작업을 요청한 순서대로 처리**할 수 밖에 없다.

**JavaScript Runtime**

- JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요함
- 특정 언어가 동작할 수 있는 환경을 Runtime 런타임이라 함
- JavaScript에서 **비동기와 관련한 작업은 브라우저 또는 Node 환경에서 처리**
- 브라우저 환경에서의 비동기 동작
  1. JavaScript Engine의 **Call Stack**
     - 요청이 들어올 때마다 순차적으로 처리하는 Stack(LIFO) 기본적인 JavaScript의 Single Thread 작업 처리
  2. **Web API**
     - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경으로 시간이 소요되는 작업을 처리 (setTimeout, DOM Event, AJAX 요청 등)
  3. **Task Queue**
     - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
  4. **Event Loop**
     - Call Stack과 Task Queue를 지속적으로 모니터링
     - Call Stack이 비어 있는지 확인 후 비어 있다면, Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

**비동기 처리 동작 방식**

- 브라우저 환경에서의 JavaScript의 비동기

1. 모든 작업은 **Call Stack**(LIFO)으로 들어간 후 처리된다.
2. 오래 걸리는 작업이 Call Stack으로 들어오면 **Web API**로 보내 별도로 처리하도록 한다.
3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 **Task Queue**(FIFO)에 순서대로 들어간다.
   - **Event Loop**가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된 작업을 Call Stack으로 보낸다.

**정리**

JavaScript는 한 번에 하나의 작업을 수행하는 Single Thread 언어로 동기적 처리를 하지만, 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 된다.

## 3. Axios 라이브러리

**Axios**

- JavaScript의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능하나 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고, browser 환경은 CDN을 이용해서 사용할 수 있음

> https://axios-http.com/kr/docs/intro
>
> https://github.com/axios/axios

### Axios 기본 구조

```django
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script> // 요청에 사용될 서버 URL 필수
  axios.get('요청할 URL') // method를 지정하지 않으면 GET방식이 기본값
    .then(성공하면 수행할 콜백함수)
    .catch(실패하면 수행할 콜백함수)
</script>
```

- get, post 등 여러 method 사용가능
- `then`을 이용해서 성공하면 수행할 로직을 작성
- `catch`를 이용해서 실패하면 수행할 로직을 작성

```html
<button>토끼</button>
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  console.log("토끼는 깡총")
  const catImageSearchURL = "https://api.thebunnyapi.com/v1/images/search"
  const btn = document.querySelector("button")
  btn.addEventListener("click", function () {
    axios
      .get(bunnyImageSearchURL)
      .then(function (response) {
      imgElem = document.createElement("img")
      imgElem.setAttribute("src", response.data[0].url)
      document.body.appendChild(imgElem)
    })
      .catch(function (error) {
      console.log("실패")
    })
    console.log("깡총")
  })
</script>
```

**결과 비교**

- 동기식 코드는 위에서부터 순서대로 처리가 되기때문에 첫번째 print가 출력되고 이미지를 가져오는 처리를 기다렸다가 다음 print 가 출력되는 반면,
- 비동기식 코드 (JavaScript)는 바로 처리가 가능한 작업(console.log)은 바로 처리하고, 오래 걸리는 작업인 이미지를 요청하고 가져오는 일은 요청을 보내 놓고 기다리지 않고 다음 코드로 진행 후 완료가 된 시점에 결과 출력이 진행됨
- 버튼을 여러 번 누르면 먼저 로딩되는 이미지부터 나오는 것을 볼 수 있다.

**정리**

- axios는 비동기로 데이터 통신을 가능하게 하는 라이브러리
- 같은 방식으로 우리가 배운 Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 수 있음

## 4. Callback과 Promise

**비동기 처리의 단점**

- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 **작업이 완료되는 순서에 따라 처리**한다는 것
- 그런데 이는 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점이 있음, 이와 같은 단점은 **실행 결과를 예상하면서 코드를 작성할 수 없게 함**
  - 콜백 함수를 사용하자

### 콜백 함수 Callback Function

**콜백 함수란?**

- **다른 함수의 인자로 전달되는 함수**를 콜백 함수라고 한다.
- 동기, 비동기 상관없이 사용 가능
- 시간이 걸리는 **비동기 작업이 완료된 후 실행할 작업을 명시하는 데 사용**되는 콜백 함수를 **비동기 콜백(asynchonous callback)**이라 부름

**콜백 함수를 사용하는 이유**

- 명시적인 호출이 아닌 특정한 조건 혹은 행동에 의해 호출되도록 작성할 수 있음
- "~면" 조건으로 이후 로직을 제어할 수 있음
- **비동기 처리를 순차적으로 동작할 수 있게 함**
- 비동기 처리를 위해서는 콜백 함수의 형태가 반드시 필요함

**콜백 지옥 (Callback Hell)**

- 콜백 함수는 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
- 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용하는데, 이 과정을 작성하다 보면 비슷한 패턴이 계속 발생하게 됨
- 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제를 Callback Hell 콜백 지옥이라 하며, 그때의 코드 작성 형태가 마치 "피라미드와 같다"고 해서 "Pyramid of doom 파멸의 피라미드"라고도 부름

**정리**

- 콜백 함수는 비동기 작업을 순차적으로 실행할 수 있게 하는 반드시 필요한 로직
- 비동기 코드를 작성하다 보면 콜백 함수로 인한 callback hell 콜백 지옥은 반드시 나타나는 문제
  - 코드의 가독성을 해치고
  - 유지 보수가 어려워짐

### Promise 프로미스

- Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- "작업이 끝나면 실행 시켜줄게"라는 promise 약속
- **비동기 작업의 완료 또는 실패를 나타내는 객체**
- Promise 기반의 클라이언트가 `Axios` 라이브러리
  - "Promise based HTTP client for the browser and node.js"
  - 성공에 대한 약속 `then()`
  - 실패에 대한 약속 `catch()`

**then & catch**

- `then(callback)`
  - 요청한 작업이 성공하면 callback 실행
  - callback은 **이전 작업의 성공 결과를 인자로 전달 받음**
- `catch(callback)`
  - then()이 하나라도 실패하면 callback 실행
  - callback은 이전 작업의 실패 객체를 인자로 전달 받음
- then과 catch 모두 항상 promise 객체를 반환, 즉 계속해서 **chaining을 할 수 있음**
- **axios로 처리한 비동기 로직이 항상 promise 객체를 반환**, 그래서 then을 계속 이어 나가면서 작성할 수 있던 것

```js
axios.get('요청할 URL').then(...).then(...).catch(...)
axios.get('요청할 URL') // Promise 객체 return
  .then(성공하면 수행할 1번 콜백함수)
  .then(1번 콜백함수가 성공하면 수행할 2번 콜백함수)
  .then(2번 콜백함수가 성공하면 수행할 3번 콜백함수)

  .catch(실패하면 수행할 콜백함수)
```

```js
// promise 방식
work1()
  .then(function (result1) {
    // work2
    return result2
  })
  .then(function (result2) {
    // work3
    return result3
  })
  .catch(function (error) {
    // error handling
  })
```

- promise 방식은 비동기 처리를 마치 우리가 일반적으로 위에서 아래로 적는 방식처럼 코드를 작성할 수 있음

**Promise가 보장하는 것 (vs 비동기 콜백)**

- 비동기 콜백 작성 스타일과 달리 Promise가 보장하는 특징

1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
   - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 `. then()` 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. `.then()`을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining)
   - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
   - Chaining은 Promise의 가장 뛰어난 장점

## 5. AJAX

- 비동기 통신을 이용하면 화면 전체를 새로고침 하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능
- 비동기 통신 웹 개발 기술을 Asynchronous Javascript and XML (AJAX) 라 함
- **AJAX의 특징**
  1. 페이지 새로고침 없이 서버에 요청
  2. 서버로부터 응답(데이터)을 받아 작업을 수행
- 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios

### 비동기 적용하기

> https://axios-http.com/kr/docs/intro

**follow 팔로우**

- 각각의 템플릿에서 script 코드를 작성하기 위한 block tag 영역 작성

```django
<!-- base.html -->

<body>
  {% block script %} {% endblock script %}
</body>
```

- axios CDN 작성

```django
<!-- accounts/profile.html -->

{% block script %}
<!-- jsDelivr CDN 사용하기: -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script></script>
{% endblock script %}
```

- form 요소 선택을 위해 id 속성 지정 및 선택
- 불필요해진 action과 method 속성은 삭제 (요청은 axios로 대체되기 때문)

```django
<!-- accounts/profile.html -->

<form id="follow-form"></form>
<script>
  const form = document.querySelector("#follow-form")
</script>
```

- form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소

```django
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector("#follow-form")
  form.addEventListener("submit", function (event) {
    event.preventDefault()
  })
</script>
```

- axios로 POST 요청 보내기

```django
<!-- accounts/profile.html -->
<script>
  const form = document.querySelector("#follow-form")
  form.addEventListener("submit", function (event) {
    event.preventDefault()
    axios({
      method: "post", // 요청을 생성할때 사용되는 메소드
      url: `/accounts/${userId}/follow/`, // 요청에 사용될 서버 URL 필수
    })
  })
</script>
```

1. **url에 작성할 user pk 가져오기 (HTML -> JavaScript)**

   ```django
   <form id="follow-form" data-user-id="{{ person.pk }}"></form>
   <script>
  const form = document.querySelector("#follow-form")
     form.addEventListener("submit", function (event) {
    event.preventDefault()
       const userId = event.target.dataset.userId
       axios({
         method: "post", // 요청을 생성할때 사용되는 메소드
         url: `/accounts/${userId}/follow/`, // 요청에 사용될 서버 URL 필수
    })
     })
</script>
   ```
   
   **`data-*` attributes**
   
   - 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환 할 수 있는 방법
   
     > [https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-\*](https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*)
  >
     > https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/Use_data_attributes

     ```django
  <div data-my-id="my-data"></div>
     <script>
       const myId = event.target.dataset.myId
     </script>
  ```
   
   - data-test-value 라는 이름의 특성을 지정했다면, JavaScript에서는 element.dataset.testValue 로 접근할 수 있음
   
   - 속셩명 작성 시 주의사항
   
     - 대소문자 여부에 상관없이 xml로 시작하면 안 됨
  - 세미콜론을 포함해서는 안됨
     - 대문자를 포함해서는 안됨

2. **csrktoken 보내기**

   - hidden 타입으로 숨겨져있는 csrf 값을 가진 input 태그를 선택해야 함

   > https://docs.djangoproject.com/en/3.2/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-or-csrf-cookie-httponly-is-true

   ```django
   <!-- accounts/profile.html -->
   <script>
     const form = document.querySelector("#follow-form")
     const csrftoken = document.querySelector(
       "[name=csrfmiddlewaretoken]"
     ).value
   </script>
   ```

   - AJAX로 csrfktoken을 보내는 방법

     > https://docs.djangoproject.com/en/3.2/ref/csrf/#setting-the-token-on-the-ajax-request
   
     ```django
     <!-- accounts/profile.html -->
     <script>
       const form = document.querySelector("#follow-form")
       const csrftoken = document.querySelector(
         "[name=csrfmiddlewaretoken]"
       ).value
       form.addEventListener("submit", function (event) {
         event.preventDefault()
         const userId = event.target.dataset.userId
         axios({
           method: "post", // 요청을 생성할때 사용되는 메소드
           url: `/accounts/${userId}/follow/`, // 요청에 사용될 서버 URL 필수
           headers: { // 사용자 지정 헤더
             "X-CSRFToken": csrftoken,
           },
         })
       })
     </script>
     ```

- 팔로우 버튼을 토글하기 위해서는 현재 팔로우가 된 상태인지 여부 확인이 필요

- axios 요청을 통해 받는 response 객체를 활용해 view 함수를 통해서 팔로우 여부를 파악 할 수 있는 변수를 담아 JSON 타입으로 응답하기

- 팔로우 여부를 확인하기 위한 is_followed 변수 작성 및 JSON 응답

  ```python
  # accounts/views.py
  
  from django.contrib.auth import get_user_model
  from django.http import JsonResponse
  from django.shortcuts import redirect
  from django.views.decorators.http import require_POST
  
  
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
          User = get_user_model()
          me = request.user
          you = User.objects.get(pk=user_pk)
          if me != you:
              if you.followers.filter(pk=me.pk).exists():
                  you.followers.remove(me)
                  is_followed = False
              else:
                  you.followers.add(me)
                  is_followed = True
              context = {
                  'is_followed': is_followed,
              }
              return JsonResponse(context)
          return redirect('accounts:profile', you.username)
      return redirect('accounts:login')

- view 함수에서 응답한 is_followed를 사용해 버튼 토글하기

  ```django
<!-- accounts/profile.html -->

<script>
  axios({
    method: "post", // 요청을 생성할때 사용되는 메소드
    url: `/accounts/${userId}/follow/`, // 요청에 사용될 서버 URL 필수
    headers: { // 사용자 지정 헤더
      "X-CSRFToken": csrftoken,
    },
  }).then(function (response) {
    const isFollowed = response.data.is_followed
    const followBtn = document.querySelector(
      "#follow-form > input[type=submit]"
    )
    if (isFollowed === true) {
      followBtn.value = "언팔로우"
    } else {
      followBtn.value = "팔로우"
    }
  })
</script>
  ```

- **팔로워 & 팔로잉 수 비동기 적용**

  - 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성

    ```django
    <!-- accounts/profile.html -->
    
    {% extends 'base.html' %} {% block content %}
    <h1>{{ person.username }}님의 프로필</h1>
    <div>
      팔로워 :
      <span id="followers-count">{{ person.followers.all|length }}</span> /
      팔로잉 :
      <span id="followings-count">{{ person.followings.all|length }}</span>
    </div>
    
    <script>
      axios({
        method: "post", // 요청을 생성할때 사용되는 메소드
        url: `/accounts/${userId}/follow/`, // 요청에 사용될 서버 URL 필수
        headers: {
          // 사용자 지정 헤더
          "X-CSRFToken": csrftoken,
        },
      }).then(function (response) {
        const followersCountTag = document.querySelector("#followers-count")
        const followingsCountTag = document.querySelector("#followings-count")
      })
    </script>
    ```
    
  - 팔로워, 팔로잉 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달

    ```python
    # accounts/views.py
    
    from django.http import JsonResponse
    from django.shortcuts import redirect
    from django.views.decorators.http import require_POST
    
    
    @require_POST
    def follow(request, user_pk):
    
                context = {
                    'is_followed': is_followed,
                    'followers_count': you.followers.count(),
                    'followings_count': you.followings.count(),
                }
                return JsonResponse(context)
            return redirect('accounts:profile', you.username)
        return redirect('accounts:login')
    ```

  - view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경하기

    ```django
    <!-- accounts/profile.html -->
    
    <script>
      axios({
        method: "post", // 요청을 생성할때 사용되는 메소드
        url: `/accounts/${userId}/follow/`, // 요청에 사용될 서버 URL 필수
        headers: { // 사용자 지정 헤더
          "X-CSRFToken": csrftoken,
        },
      }).then(function (response) {
        const followersCountTag = document.querySelector("#followers-count")
        const followingsCountTag = document.querySelector("#followings-count")
        followersCountTag.innerText = followersCount
        followingsCountTag.innerText = followingsCount
      })
    </script>
    ```

**최종 코드**

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %} {% block content %}
<h1>{{ person.username }}님의 프로필</h1>
<div>
  팔로워 :
  <span id="followers-count">{{ person.followers.all|length }}</span> /
  팔로잉 :
  <span id="followings-count">{{ person.followings.all|length }}</span>
</div>

{% if request.user != person %}
<div>
  <form id="follow-form" data-user-id="{{ person.pk }}">
    {% csrf_tokne %} {% if request.user in person.followers.all %}
    <input type="submit" value="언팔로우" />
    {% else %} <input type="submit" value"팔로우"> {% endif %}
  </form>
</div>
{% endif %}

<script>
  const form = document.querySelector("#follow-form")
  const csrftoken = document.querySelector(
    "[name=csrfmiddlewaretoken]"
  ).value

  form.addEventListener("submit", function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId

    axios({
      method: "post", // 요청을 생성할때 사용되는 메소드
      url: `/accounts/${userId}/follow/`, // 요청에 사용될 서버 URL 필수
      headers: { // 사용자 지정 헤더
        "X-CSRFToken": csrftoken,
      },
    })
      .then(function (response) {
        const isFollowed = response.data.is_followed
        const followBtn = document.querySelector(
          "#follow-form > input[type=submit]"
        )
        if (isFollowed === true) {
          followBtn.value = "언팔로우"
        } else {
          followBtn.value = "팔로우"
        }
        const followersCountTag = document.querySelector("#followers-count")
        const followingsCountTag =
          document.querySelector("#followings-count")
        const followersCount = response.data.followers_count
        const followingsCount = response.data.followings_count
        followersCountTag.innerText = followersCount
        followingsCountTag.innerText = followingsCount
      })
      .catch(function (error) {
        console.log(error)
      })
  })
</script>
```

```python
# accounts/views.py

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

**like 좋아요**

- 좋아요 비동기 적용은 `forEach()` & `querySelectorAll()`
  - index 페이지 각 게시글에 좋아요 버튼이 있기 때문

```django
<!-- articles/index.html -->

{% extends 'base.html' %} 

{% block content %}

<h1>Articles</h1>
{% if request.user.is_authenticated %}
<a href="{% url 'articles:create' %}">CREATE</a>
{% endif %}
<hr />

{% for article in articles %}
<p>
  <b>작성자 :
    <a href=" {% url 'accounts:profile' article.user %}">
      {{ article.user }}
    </a>
  </b>
</p>
<p>글 번호 : {{ article.pk }}</p>
<p>글 제목 : {{ article.title }}</p>
<p>글 내용 : {{ article.content }}</p>
<div>
  <form class="like-forms" data-article-id="{{ article.pk }}">
    {% csrf_token %} {% if request.user in article.like_users.all %}
    <input type="submit" id="like-{{ article.pk }}" value="좋아요 취소" />
    {% else %}
    <input type="submit" id="like-{{ article.pk }}" value="좋아요 취소" />
    {% endif %}
  </form>
  <p>
    <span id="like-count-{{ article.pk }}">
      {{ article.like_users.all|length }}
    </span>
    명이 이 글을 좋아합니다.
  </p>
</div>
<a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
<hr />
{% endfor %} 

{% endblock content %} 

{% block script %}
<script>
  const forms = document.querySelectorAll(".like-forms") // 좋아요 form 태그를 선택
  // 속성 선택자를 이용해서 {% csrf_token %} 의 csrf_token 데이터를 가져옴
  const csrftoken = document.querySelector(
    "[name=csrfmiddlewaretoken]"
  ).value

  forms.forEach(function (form) {
    // 이벤트 리스너를 달아준다.
    form.addEventListener("submit", function (event) {
      event.preventDefault() // submit 동작이 되지 않도록, 서버요청X
      const articleId = event.target.dataset.articleId
      // csrf 토큰을 같이 넣어서 전달해야 함
      // 왜냐면 form 요청을 preventDefault 로 요청을 막았기 때문에
      // form 에 작성된 csrf 토큰이 추가된 요청이 이루어 지는 것이 아니고
      // 따로 axios 로 요청을 하는 것이기 때문에
      // 이 axios 는 csrf 토큰 정보가 없는 상태
      axios({
        method: "post", // 요청을 생성할때 사용되는 메소드
        url: `/articles/${articleId}/likes/`, // 요청에 사용될 서버 URL 필수
        headers: { // 사용자 지정 헤더
          "X-CSRFToken": csrftoken,
        }, // csrf token 값을 header로 전달
      })
        .then(function (response) {
          // response.data 에는 좋아요 눌렸는지 여부를 확인할 수 있는 data가 있음
          const isLiked = response.data.is_liked
          const likeBtn = document.querySelector(`#like-${articleId}`)
          // data 를 이용해서 좋아요가 눌렸는지 DOM 조작을 통해 수정
          if (isLiked === true) {
            likeBtn.value = "좋아요 취소"
          } else {
            likeBtn.value = "좋아요"
          }
          // 좋아요 카운트 변경
          // 응답에서 좋아요 카운트를 얻어와서 DOM 조작
          const likeCnt = response.data.like_cnt // 좋아요 사람 수
          const likeCntText = document.querySelector(
            `#like-count-${articleId}`
          )
          likeCntText.innerText = likeCnt
        })
        .catch(function (error) {
          console.log(error)
        })
    })
  })
</script>
{% endblock script %}
```

```python
# articles/views.py

from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .models import Article


@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        # article을 좋아하는 유저에 request.user가 있으면
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            is_liked = False  # 좋아요가 눌린 상태
        else:
            article.like_users.add(request.user)
            is_liked = True  # 좋아요가 눌린 상태
        context = {
            'is_liked': is_liked,
        }
        return JsonResponse(context)
    return redirect('accounts:login')
```

## finish

- 동기와 비동기
- JavaScript의 비동기 처리
  - Call Stack, Web API, Task Queue, Event Loop
- Axios 라이브러리
  - then & catch
- Async Callback과 Promise

- AJAX
