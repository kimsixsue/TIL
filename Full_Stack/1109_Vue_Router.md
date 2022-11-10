[Vue Router](#vue-router)

1. [UX & UI](#1-ux--ui)
   - [INTRO](#intro)
   - [UX & UI](#ux---ui)
   - [생각하는 UX & UI 디자인](#생각하는-ux--ui-디자인)
   - [Prototyping](#prototyping)
2. [Vue Router](#2-vue-router)
   - [Routing](#routing)
   - [Vue Router](#vue-router-1)
   - [Vue Router 실습](#vue-router-실습)
3. [Navigation Guard](#3-navigation-guard)
   - [전역 가드](#전역-가드)
   - [라우터 가드](#라우터-가드)
   - [컴포넌트 가드](#컴포넌트-가드)
   - [404 Not Found](#404-not-found)
4. [Articles app with Vue](#4-articles-app-with-vue)
   - [Index](#index)
   - [Create](#create)
   - [Detail](#detail)
   - [Delete](#delete)
   - [404 Not Found](#404-not-found-1)

- [finish](#finish)

# Vue Router

## 1. UX & UI

### INTRO

- 비슷한 것끼리 묶거나 내용을 구성해서 인지하는 것이 편하다. 만약 그렇지 않을 경우

  불편하다는 느낌을 받거나 의사결정을 하는데 많은 시간이 걸리기도 한다.

- 이러한 요소들은 유저와 밀접한 부분이기에

  매우 중요하며 모든 서비스에서 반드시 고려되어야 한다.

- 단순한 느낌이나 심미적인 부분만 고려하는 것이 아닌

  **체계적인 설계를 통해 기획**해야 한다.

### UX & UI

**UX (User Experience)**

- 유저와 가장 가까이에 있는 분야, 데이터를 기반으로 유저를 조사하고 분석해서

  개발자, 디자이너가 이해할 수 있게 소통

- 유저가 느끼는 느낌, 태도 그리고 행동을 디자인
  - 로딩이 너무 길어서 사용하고 싶지 않았던 사이트

**좋은 UX를 설계하기 위해서는**

- 사람들의 마음과 생각을 이해하고 정리해서 우리 제품에 녹여내는 과정이 필요
- 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요

**UI (User Interface)**

- 유저에게 보여지는 화면을 디자인

- UX를 고려한 디자인을 반영, 이 과정에서 기능 개선 혹은 추가가 필요한 경우

  Front-end 개발자와 가장 많이 소통

**[참고] Interface**

- 서로 다른 두 개의 시스템, 장치 사이에서 정보나 신호를 주고받는 경우의 접점
  - 즉, 사용자가 기기를 쉽게 동작 시키는데 도움을 주는 시스템
  
  - CLI(command-line interface) 나 GUI (Graphic User Interface) 를
  
    사용해서 컴퓨터를 조작

**좋은 UI를 설계하기 위해서는**

- 예쁜 디자인 즉 심미적인 부분만 중요하다기보다는 사용자가 보다 쉽고

  편리하게 사용할 수 있도록 하는 부분까지 고려되어야 함

- 통일된 디자인을 위한 디자인 시스템, 소통을 위한 중간 산출물, 프로토타입 등이 필요

- UI 디자인에 있어 가장 중요한 것은 **협업**

**디자이너와 기획자 그리고 개발자**

- 많은 회사에서 UX/UI 디자인을 함께하는 디자이너를 채용하거나

  UX는 기획자, UI는 디자이너의 역할로 채용하기도 함

- **UX (직무: UX Researcher, User Researcher)**

- **UI (직무 : Product Designer, Interaction Designer)**

- 개발자는 단순히 기능 개발만 하는 사람이 아니며 제품에 대해 고민하고

  소통하는 능력이 반드시 필요

- 즉 다양한 분야와의 협업이 필수적이기에 기본적인 UX/UI 에 대한 이해가 있어야 함

### 생각하는 UX & UI 디자인

- UX/UI 를 디자인 하는 것은 굉장히 섬세하면서 어려운 작업

**[참고] Can't Unsee** https://cantunsee.space/

- 더 나은 UX/UI 를 고민해볼 수 있는 웹 사이트

**학문으로서의 UX & UI**

- UX와 UI는 단순히 누군가의 직감에 의해서 결정되는 것이 아님

- 하나의 학문으로서 연구되고 있는 분야이며 심리학과도 밀접한 연관이 있음

- UX/UI 그리고 HCI

  - GUI: 유저가 보는 일반적인 시각적인 디자인
  - UI: 유저가 보거나 듣는 등 비시각적인 부분까지 포함한 디자인
  - UX: 유저가 겪는 모든 경험(컴퓨터와 관련이 없는 부분까지도 포함)
  - HCI(Human Computer Interaction): 인간과 컴퓨터 사이의 상호작용에 대한 학문
  
- 점점 더 복잡해지는 기술과 반대로 점점 더 단순하고 대중화 되어야하는

  유저에 대한 경험으로 인해 계속해서 연구되는 중요한 분야

- 예술에 정답이 없듯, 디자인에도 정답이 정해져 있지 않음

- 전세계의 많은 디자이너 또는 연구자들이 데이터에 기반해서 연구한 다양한 가이드 존재

- 예시) Apple의 UI 디자인 원칙 (https://developer.apple.com/kr/design/tips/)

### Prototyping

**Software prototyping**

- 애플리케이션의 프로토타입을 만드는 것
- 즉 개발 중인 소프트웨어 프로그램의 완성되기 전 버전을 만드는 것
- 한 번에 완성 버전이 나올 수 없기에 중간마다 현재 상태를 체크하는 과정

**Prototyping Tool 시장**

- UI/UX 디자인을 prototyping 하기 위한 도구는 굉장히 많고 빠른 패러다임의

  변화로 인해 치열한 경쟁이 계속되고 있음

- 이전까지는 Sketch 라는 툴이 굉장히 많이 사용되었지만,

  현재에는 **Figma** 라는 툴이 약 70%의 시장 점유율을 보이고 있음

**Figma**

- 인터페이스 디자인을 위한 협업 웹 애플리케이션 (2012년 출시)
- **협업**에 중점을 두면서 UI/UX 설계에 초점을 맞춤
- 시장을 지배한 Figma

**Why Figma?**

- 웹 기반 시스템을 가짐 (웹 환경에서 동작)
  - 매우 가벼운 환경에서 실행 가능, 모든 작업 내역이 웹에 저장됨
- **실시간으로 팀원들이 협업**할 수 있는 기능을 제공
- 직관적이고 다양한 디자인 툴을 제공
- Figma 사용자들이 만든 다양한 플러그인이 존재 (VSCode의 확장프로그램 등)
- **대부분의 기능을 무료로 사용**할 수 있음

**Figma 성공의 이유**

- 성능의 희생을 일부 감수하고 웹 기반으로 원활한 협업이 이루어지도록 함

- 기존 서비스들의 모든 불필요한 과정을 생략하고

  **디자인** 그 자체에만 집중 할 수 있게 함

- 이를 따라잡기 위해 시장 업계 1위 Adobe도 Adobe XD라는 프로그램을 앞세우며

  많은 노력을 했지만 경쟁이 불가함을 인정한 Adobe는 결국

- "Adobe, Figma 28조원에 인수 (2022.09)"

**프로젝트를 시작하기 전에**

- 개발부터 시작하지 말고 반드시 충분한 기획을 거칠 것
- 우리가 완성하고자 하는 대략적인 모습을 그려보는 과정이 필요 (프로토타입)
- 이러한 과정을 통해서 기획에서 빠진 화면이나 API 등을 확인할 수 있음
- 설계와 기획이 끝난 후 개발을 시작해야 체계적인 진행이 가능함

**프로젝트와 협업**

- 협업은 프로젝트와 팀이 성공하기 위한 토대

- 어떻게 효과적으로 잘 협업할 수 있는지 다양한 방법과 도구를 찾아보고

  학습하며 여러 프로젝트를 경험하는 과정이 반드시 필요

## 2. Vue Router

### Routing

- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
  - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
- 예시
  - /articles/index/ 에 접근하면 articles의 index에 대한 결과를 보내줌

**Routing in SSR**

- Server 가 모든 라우팅을 통제
- URL로 요청이 들어오면 응답으로 완성된 HTML 제공
- 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

**Routing in SPA / CSR**

- 서버는 하나의 HTML(index.html) 만을 제공

- 이후에 모든 동작은 하나의 HTML 문서 위에서 JavaScript 코드를 활용
  - DOM을 그리는데 필요한 추가적인 데이터가 있다면
  
    axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여
  
    데이터를 가져오고 처리
  
- 즉, **하나의 URL만 가질 수 있음**

**Why routing?**

- 유저의 사용성 관점에서는 동작에 따라 URL이 바뀌는 것이 반드시 필요함
- Routing이 없다면,
  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
  - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - 새로고침 시 처음 페이지로 돌아감
    - 링크를 공유할 시 처음 페이지만 공유 가능
  - 브라우저의 뒤로 가기 기능을 사용할 수 없음

### Vue Router

- Vue의 공식 라우터
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- `routes` 라우트에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
  - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
  - SPA의 단점 중 하나인 **"URL이 변경되지 않는다." 를 해결**
- [참고] MPA (Multiple Page Application)
  - 여러 개의 페이지로 구성된 애플리케이션
  - SSR 방식으로 렌더링

**Vue Router 시작하기**

```bash
$ vue create vue-router-app # Vue 프로젝트 생성
$ cd vue-router-app         # 디렉토리 이동
$ vue add router            # Vue CLI를 통해 router plugin 적용
```

- **기존에 프로젝트를 진행하고 있던 도중에 router를 추가하게 되면 App.vue를 덮어쓰므로**

  **필요한 경우 명령을 실행하기 전에 파일을 백업해두어야 함** 

```bash
? Use history mode for router? (Requires proper server
setup for index fallback in production) (Y,n)
```

- history mode 사용여부 -> Yes

**History mode**

- 브라우저의 History API를 활용한 방식
  - 새로고침 없이 URL 이동 기록을 남길 수 있음
  
- 우리에게 익숙한 URL 구조로 사용 가능
  - 예시) http://localhost:8080/index

- [참고] History mode를 설정하지 않으면
  
  Default 값인 hash mode로 설정됨 (`#` 을 통해 URL을 구분하는 방식)
  
  - 예시) http://localhost:8080#index
  
- App.vue

  - `router-link` 요소 및 `router-view` 가 추가됨

  ```vue
  <template>
    <div id="app">
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link>
      </nav>
      <router-view />
    </div>
  </template>
  ```

- router/index.js 생성

- views 폴더 생성

- 서버 실행하기

**`router-link`**

- a 태그와 비슷한 기능 -> URL을 이동시킴
  - `routes` 에 등록된 컴포넌트와 매핑됨
  
  - 히스토리 모드에서 `router-link` 는 클릭 이벤트를 차단하여
  
    a 태그와 달리 브라우저가 페이지를 다시 로드 하지 않도록 함
  
- 목표 경로는 **`'to'`** 속성으로 지정됨

- 기능에 맞게 HTML에서 a 태그로 rendering 되지만,

  필요에 따라 다른 태그로 바꿀 수 있음

- 개발자 도구 확인

**` router-view`**

- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
- `router-link` 를 클릭하면 `routes` 에 매핑된 컴포넌트를 렌더링.
- 개발자 도구 확인

**src/router/index.js**

- 라우터에 관련된 정보 및 설정이 작성 되는 곳
- `routes` 에 URL과 컴포넌트를 매핑

``` js
import Vue from "vue"
import VueRouter from "vue-router"
import HomeView from "../views/HomeView.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // lazy-loading 방식
    // 첫 로딩에 렌더링 하지않고 해당 라우터가 동작할 때 컴포넌트를 렌더링 한다
    component: () => import("../views/AboutView.vue"),
  },
]
```

**src/Views**

- `router-view` 에 들어갈 component 작성

- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제

  두 폴더로 나뉘어짐

- 각 폴더 안의 `.vue` 파일들이 기능적으로 다른 것은 아님

- 이제 폴더별 컴포넌트 배치는 다음과 같이 진행 (규약은 아님)

- `views/`
  - `routes` 에 매핑되는 컴포넌트,
  
    즉 `<router-view>` 의 위치에 렌더링 되는 컴포넌트를 모아두는 폴더
  
  - 다른 컴포넌트와 구분하기 위해 View 로 끝나도록 만드는 것을 권장
  
  - ex) App 컴포넌트 내부의 AboutView & 컴포넌트
  
- `components/`
  - `routes` 에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
  - ex) HomeView  컴포넌트 내부의 HelloWorld 컴포넌트

### Vue Router 실습

**주소를 이동하는 2가지 방법**

1. 선언적 방식 네비게이션
2. 프로그래밍 방식 네비게이션

**선언적 방식 네비게이션**

- `router-link` 의 **`'to'`** 속성으로 주소 전달
  - `routes` 에 등록된 주소와 매핑된 컴포넌트로 이동

```vue
<!-- App.vue -->

<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view />
  </div>
</template>
```

- Named Routes : 이름을 가지는 `routes`

```js
// router/index.js

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
]
```

- 동적인 값을 사용하기 때문에 `v-bind` 를 사용해야 정상적으로 작동

```vue
<!-- App.vue -->

<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'about' }">About</router-link>
    </nav>
    <router-view />
  </div>
</template>
```

**프로그래밍 방식 네비게이션**

- Vue 인스턴스 내부에서 라우터 인스턴스에 **`$router`** 로 접근 할 수 있음

- 다른 URL로 이동하려면 **`this.$router.push`** 를 사용
  - history stack 에 이동할 URL을 `push` 넣는 방식
  
  - history stack 에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을
  
    클릭하면 이전 URL 로 이동할 수 있음
  
- 결국 **`<router-link :to="...">`** 를 클릭하는 것과

  **`$router.push(...)`** 를 호출하는 것은 같은 동작

- 동작 원리는 선언적 방식과 같음

```vue
<!-- AboutView.vue -->

<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">홈으로!</router-link> |
    <button @click="toHome">홈으로!</button>
  </div>
</template>

<script>
export default {
  name: "AboutView",
  methods: {
    toHome() {
      this.$router.push({ name: "home" })
    },
  },
}
</script>
```

**Dynamic Route Matching**

- 동적 인자 전달
  - URL의 특정 값을 변수처럼 사용할 수 있음
- HelloView.vue 작성 및 route 추가
- route 를 추가할 때 동적 인자를 명시

```js
// router/index.js

import HelloView from "@/views/HelloView.vue"

const routes = [

  {
    path: "/hello/:userName",
    name: "hello",
    component: HelloView,
  },
]
```

```vue
<!-- views/HelloView.vue -->

<template>
  <div>
  </div>
</template>

<script>
export default {
  name: "HelloView",
}
</script>
```

- **`$route.params`** 로 변수에 접근 가능
- `data` 에 넣어서 사용하는 것을 권장

```vue
<!-- views/HelloView.vue -->

<template>
  <div>
    <h1>hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
  name: "HelloView",
  data() {
    return {
      userName: this.$route.params.userName,
    }
  },
}
</script>
```

**Dynamic Route Matching - 선언적 방식 네비게이션**

- App.vue 에서 harry 에게 인사하는 페이지로 이동해보기
- `params` 를 이용하여 동적 인자 전달 가능

```vue
<!-- App.vue -->

<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'about' }">About</router-link>
      <router-link :to="{ name: 'hello', params: { userName: 'kim' } }">
        Hello</router-link> |
    </nav>
    <router-view />
  </div>
</template>
```

**Dynamic Route Matching - 프로그래밍 방식 네비게이션**

- AboutView 에서 데이터를 입력 받아 HelloView 로 이동하여

  입력받은 데이터에게 인사하기

```vue
<!-- AboutView.vue -->

<template>
  <div class="about">

    <input
      type="text"
      @keyup.enter="goToHello"
      v-model="inputData"
    />
  </div>
</template>

<script>
export default {
  name: "AboutView",
  data() {
    return {
      inputData: null,
    }
  },
  methods: {

    goToHello() {
      this.$router.push({
        name: "hello",
        params: { userName: this.inputData },
      })
    },
  },
}
</script>
```

**route 에 컴포넌트를 등록하는 또다른 방법**

- router/index.js 에 컴포넌트를 등록하는 또다른 방식이 주어지고 있음( `about` )

```js
// router/index.js

import HomeView from "../views/HomeView.vue"

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  }, // 기존 방식
]
```

```js
// router/index.js

const routes = [
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutView.vue"),
  }, // Lazy-loading
]
```

**lazy-loading**

- 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림

- 미리 로드를 하지 않고 특정 라우트에 방문할 때

  매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음

  - 모든 파일을 한 번에 로드하지 않아도 되기 때문에

    최초에 로드하는 시간이 빨라짐

  - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심

## 3. Navigation Guard

**네비게이션 가드** https://v3.router.vuejs.org/guide/advanced/navigation-guards.html

- Vue router 를 통해 특정 URL 에 접근할 때

  다른 url 로 redirect 를 하거나 해당 URL 로의 접근을 막는 방법

  - Ex) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함

**네비게이션 가드의 종류**

- **전역 가드 Global Before Guard**
  - 애플리케이션 전역에서 동작
- **라우터 가드 Per-Route Guard**
  - 특정  URL 에서만 동작
- **컴포넌트 가드 In-Component Guards**
  - 라우터 컴포넌트 안에 정의

### 전역 가드

**Global Before Guard**

- 다른 url 주소로 이동할 때 항상 실행
- router/index.js 에 **`router.beforeEach()`** 를 사용하여 설정
- 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
  - **`to`** : 이동할 URL 정보가 담긴 Route 객체
  - **`from`** : 현재 URL 정보가 담긴 Route 객체
  - **`next`** : 지정한 URL 로 이동하기 위해 호출하는 함수
    - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
    - 기본적으로 **`to`** 에 해당하는 URL 로 이동
- URL 이 변경되어 화면이 전환되기 전 **`router.beforeEach()`** 가 호출됨
  - 화면이 전환되지 않고 대기 상태가 됨
- 변경된 URL 로 라우팅하기 위해서는 **`next()`** 를 호출해줘야 함
  - **`next()` 가 호출되기 전까지 화면이 전환되지 않음**

**Global Before Guard 실습**

- '/home' 으로 이동하더라도 라우팅이 되지 않고 로그만 출력됨
- **`next()`** 가 호출되지 않으면 화면이 전환되지 않음

```js
// router/index.js

router.beforeEach((to, from, next) => {
  console.log("to", to)
  console.log("from", from)
  console.log("next", next)
})
```

- **`next()`** 가 호출되어야 화면이 전환됨

```js
// router/index.js

router.beforeEach((to, from, next) => {
  console.log("to", to)
  console.log("from", from)
  console.log("next", next)
  next()
})
```

- About 으로 이동해보기
  - `to` 에는 이동할 url 인 about 에 대한 정보가,
  - `from` 에는 현재 url 인 home 에 대한 정보가 들어있음

**Login 여부에 따른 라우팅 처리**

- Login 이 되어있지 않다면 Login 페이지로 이동하는 기능 추가

```vue
<!-- views/LoginView.vue -->

<template>
  <div>
    <h1>This is Login Page</h1>
  </div>
</template>

<script>
export default {
  name: "LoginView",
}
</script>
```

```js
// router/index.js

import LoginView from "@/views/LoginView"

const routes = [
  
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
]
```

- LoginView 에 대한 라우터 링크 추가

```vue
<!-- App.vue -->

<template>
  <div id="app">
    <nav>
      
      <router-link :to="{ name: 'login' }">Login</router-link> |
    </nav>
```

- HelloView 에 로그인을 해야만 접근할 수 있도록 만들어 보기
- 로그인 여부에 대한 임시 변수 생성
- 로그인이 필요한 페이지를 저장
  - 로그인이 필요한 페이지들의 이름 (라우터에 등록한 `name`) 을 작성
- 앞으로 이동할 페이지(`to`)가 로그인이 필요한 사이트인지 확인

```js
// router/index.js

router.beforeEach((to, from, next) => {

  // 로그인 여부
  const isLoggedIn = true

  // 로그인이 필요한 페이지
  const authPages = ["hello"]

  // 앞으로 이동할 페이지(to)가
  // 로그인이 필요한 사이트인지 확인
  const isAuthRequired = authPages.includes(to.name)
})
```

- isAuthRequired 값에 따라 로그인이 필요한 페이지이고

  로그인이 되어있지 않으면

  - Login 페이지로 이동

- 그렇지 않으면
  - 기존 루트로 이동
  
- `next()` 인자가 없을 경우 `to` 로 이동
  - **`next()` 가 한번만 호출되도록 유의**

```js
// router/index.js

router.beforeEach((to, from, next) => {
  
  if (isAuthRequired && !isLoggedIn) {
    console.log("Login으로 이동!")
    next({ name: "login" })
  } else {
    console.log("to로 이동!")
    next()
  }
})
```

- isLoggedIn 이 true 인 경우 (로그인 상태에서 로그인이 필요한 페이지로 접속)

  - **/hello/harry/** 에 해당하는 컴포넌트가 정상적으로 렌더링

- isLoggedIn 이 false 인 경우 (비로그인 상태에서 로그인이 필요한 페이지로 접속)

  - **/hello/harry/** 를 렌더링하지 않고 Login 페이지로 이동됨

- Home => Login 으로 이동했는데 console 창에 log 가 2개가 찍힌 이유

  - 첫번째 출력은 /hello/harry 로 접속 시도 후 (전역 가드에 막힘)

    전역 가드에서 login 으로 이동 요청 할 때 출력

  - 두번째 출력은 /login 으로 이동 요청 할 때 출력

- **/hello/:userName** 페이지를 제외하고는

  전역 가드에서 기존 주소로 이동하기 때문에 정상적으로 작동

- 로그인이 필요한 페이지에 추가하면 비로그인 시 해당 페이지에 접근 불가

```js
// router/index.js

router.beforeEach((to, from, next) => {

  // 로그인이 필요한 페이지
  const authPages = ["hello", "home", "about"]
```

- 만약 view 들이 여러 개라면 모두 추가해주어야 할까?
  - 반대로 Login 하지 않아도 되는 페이지들을 모아 둘수도 있음

```js
// router/index.js

router.beforeEach((to, from, next) => {

  // const authPages = ["hello", "home", "about"]
  const allowAllPages = ["login"]

  // const isAuthRequired = authPages.includes(to.name)
  const isAuthRequired = !allowAllPages.includes(to.name)

})
```

### 라우터 가드

- Per-Route Guard

- 전체 route 가 아닌 특정 route 에 대해서만 가드를 설정하고 싶을 때 사용

- **`beforeEnter()`**
  
  - route 에 진입했을 때 실행됨
  
  - 라우터를 등록한 위치에 추가
  
  - 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고
  
    다른 경로에서 탐색할 때만 실행됨
  
  - 콜백 함수는 `to, from, next` 를 인자로 받음

**Login 여부에 따른 라우팅 처리**

- 이미 로그인 되어있는 경우 HomeView 로 이동하기
- 라우터 가드를 위해 전역 가드 코드는 주석처리

- 로그인 여부에 대한 임시 변수 생성
- 로그인이 되어있는 경우 home 으로 이동
- 로그인이 되어있지 않은 경우 login 으로 이동

```js
// router/index.js

const isLoggedIn = true

const routes = [
  
  {
    path: "/login",
    name: "login",
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log("이미 로그인함")
        next({ name: "home" })
      } else {
        next()
      }
    },
  },
]
```

- isLoggedIn = true 인 경우 (로그인 상태인 경우)
  - **/login** 으로 접속을 시도하면 Home 으로 이동

- Login 여부에 따른 라우팅 처리
  - Login 을 제외한 다른 페이지로 이동하면 라우터 가드를 따로 설정해주지
  
    않았기 때문에 라우터 가드가 동작하지 않음
  
  - 이런식으로 특정 라우트만 따로 가드를 하고 싶은 경우에는 라우터 가드를 사용
  
  - isLoggedIn = false 로 변경하면 Login 페이지로 정상 이동 가능

### 컴포넌트 가드

- In-Component Guards
- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- **`beforeRouteUpdate()`**
  - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

**Params 변화 감지**

- about 에서 jun 에게 인사하는 페이지로 이동
- navbar 에 있는 Hello 를 눌러 harry 에게 인사하는 페이지로 이동
  - URL 은 변하지만 페이지는 변화하지 않음
- 변화하지 않는 이유
  - 컴포넌트가 재사용되었기 때문
  - 기존 컴포넌트를 지우고 새로 만드는 것보다 효율적
    - 단, lifecycle hook 이 호출되지 않음
    - 따라서 `$route.params` 에 있는 데이터를 새로 가져오지 않음
- **`beforeRouteUpdate()`** 를 사용해서 처리
  - userName 을 이동할 params 에 있는 userName 으로 재할당

```vue
<!-- views/HelloView.vue -->

<script>
export default {
  name: "HelloView",
  data: function () {
    return {
      userName: this.$route.params.userName,
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName
    next()
  },
}
</script>
```

### 404 Not Found

- 사용자가 요청한 리소스가 존재하지 않을 때 응답

```vue
<!-- views/NotFound404.vue -->

<template>
  <div>
    <h1>404 Not Found</h1>
  </div>
</template>

<script>
export default {
  name: "NotFound404",
}
</script>
```

```js
// router/index.js

import NotFound404 from "@/views/NotFound404"

const routes = [
  
  {
    path: "/404",
    name: "NotFound404",
    component: NotFound404,
  },
]
```

- http://localhost:8080/404 확인

- 이렇게 직접 요청하는 방식이 아닌, 요청한 리소스가 존재하지 않을 때

  404 로 이동하도록 하려면 어떻게 해야 할까?

**요청한 리소스가 존재하지 않는 경우**

- 모든 경로에 대해서 404 page 로 `redirect` 시키기
  - 기존에 명시한 경로가 아닌 모든 경로가 404 page 로 `redirect` 됨
  - **이때, `routes` 에 최하단부에 작성해야 함**

```js
// router/index.js

const routes = [
  
  {
    path: "*",
    redirect: "/404",
  },
]
```

**형식은 유효하지만 특정 리소스를 찾을 수 없는 경우**

- 예시) **articles/1/** 로 요청을 보냈지만, 1번 게시글이 삭제된 상태
  - 이때는 `path: '*'` 를 만나 404 page 가 렌더링 되는 것이 아니라
  
    기존에 명시한 **articles/:id/** 에 대한 components 가 렌더링됨
  
  - 하지만 데이터가 존재하지 않기 때문에 정상적으로 렌더링이 되지 않음
  
- 해결책
  - 데이터가 없음을 명시
  - 404 page 로 이동해야 함
  
- Dog API 문서(https://dog.ceo/dog-api/) 를 참고하여

  동적 인자로 강아지 품종을 전달해

  품종에 대한 랜덤 이미지를 출력하는 페이지를 만들어보기

1. Axios 설치
2. DogView 컴포넌트 작성
3. `routes` 에 등록
   - `'*'` 보다 상단에 등록

```bash
$ npm i axios
```

```vue
<!-- views/DogView.vue -->

<template>
  <div>
  </div>
</template>

<script>
export default {
  name: "DogView",
}
</script>
```

```js
// router/index.js

const routes = [
  
  {
    path: "/dog/:breed",
    name: "dog",
    component: DogView,
  },
  {
    path: "*",
    redirect: "/404",
  },
]
```

- Dog api 문서를 참고하여 axios 로직을 작성

```vue
<!-- views/DogView.vue -->

<template>
  <div>
    <img v-if="imgSrc" :src="imgSrc" alt="" /><br />
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "DogView",
  data() {
    return {
      imgSrc: null,
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageSearchUrl = `https://dog.ceo/api/breed/${breed}/images/random`
      axios({
        method: "get",
        url: dogImageSearchUrl,
      })
        .then((response) => {
          console.log(response)
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => console.log(error))
    },
  },
  created() {
    this.getDogImage()
  },
}
```

- /dog/hound 에 접속하면 hound 품종에 대한 랜덤 사진이 출력
- axios 요청이 오는 중 동작하고 있음을 표현하기 위한 로딩 메시지 정의

```vue
<!-- views/DogView.vue -->

<template>
  <div>
    <p v-if="!imgSrc">{{ message }}</p>
    <img v-if="imgSrc" :src="imgSrc" alt="" /><br />
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      imgSrc: null,
      message: "로딩중...",
    }
  },
  
}
</script>
```

- axios 요청이 실패할 경우 자료가 없음을 표현하기

```vue
<!-- views/DogView.vue -->

<script>
axios({
  method: "get",
  url: dogImageSearchUrl,
})
  .then((response) => {
    const imgSrc = response.data.message
    this.imgSrc = imgSrc
  })
  .catch((error) => {
    this.message = `${this.$route.params.breed}은 없는 품종입니다.`
    console.log(error)
  })
</script>
```

- **/dog/abc** 에 접속

**404 Not Found**

- 이전처럼 메세지를 바꿀수도 있지만

  axios 요청이 실패할 경우 404 페이지로 이동 시킬 수도 있음

```vue
<!-- views/DogView.vue -->

<script>
axios({
  method: "get",
  url: dogImageSearchUrl,
})
  .then((response) => {
    const imgSrc = response.data.message
    this.imgSrc = imgSrc
  })
  .catch((error) => {
    this.$router.push("/404")
    console.log(error)
  })
</script>
```

## 4. Articles app with Vue

- 구현기능
  - Index
  - Create
  - Detail
  - Delete
  - 404

**사전 준비**

- 프로젝트 시작

```bash
$ vue create articles
$ cd articles
$ vue add vuex
$ vue add router
```

- App.vue 는 아래 코드만 남김 (CSS 코드 유지)

```vue
<!-- App.vue -->

<template>
  <div id="app">
    <router-view />
  </div>
</template>
```

### Index

- articles 의 목록을 보여주는 index 페이지 작성

**Index 구현**

- `state`

- 게시글의 필드는 id, 제목, 내용, 생성일자

- DB 의 AUTO INCREMENT 를 표현하기 위해

  article_id 를 추가로 정의해줌 (다음 article의 id 로 사용 예정)

```js
// store/index.js

state: {
  article_id: 3,
  articles: [
    {
      id: 1,
      title: "title1",
      content: "content",
      createdAt: new Date().getTime(),
    },
    {
      id: 2,
      title: "title2",
      content: "content2",
      createdAt: new Date().getTime(),
    },
  ],
},
```

- IndexView 컴포넌트 및 라우터 작성

```vue
<!-- views/IndexView.vue -->

<template>
  <div>
    <h1>Articles</h1>
  </div>
</template>

<script>
export default {
  name: "IndexView",
}
</script>
```

```js
// router/index.js

const routes = [
  {
    path: "/",
    name: "index",
    component: IndexView,
  },
]
```

- `state` 에서 불러온 articles 출력하기

```vue
<!-- views/IndexView.vue -->

<template>
  <div>
    <h1>Articles</h1>
    {{ articles }}
  </div>
</template>

<script>
export default {
  name: "IndexView",
  computed: {
    articles() {
      return this.$store.state.articles
    },
  },
}
</script>
```

- ArticleItem 컴포넌트 작성

```vue
<!-- components/ArticleItem.vue -->

<template>
  <div>
  </div>
</template>

<script>
export default {
  name: "ArticleItem",
}
</script>
```

- IndexView 컴포넌트에서 ArticleItem 컴포넌트 등록 및 props 데이터 전달

```vue
<!-- views/IndexView.vue -->

<template>
  <div>
    <h1>Articles</h1>
    <ArticleItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script>
import ArticleItem from "@/components/ArticleItem"

export default {
  name: "IndexView",
  components: {
    ArticleItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
  },
}
</script>
```

- `props` 데이터 선언 및 게시글 출력

```vue
<!-- components/ArticleItem.vue -->

<template>
  <div>
    <p>글 번호 : {{ article.id }}</p>
    <p>제목 : {{ article.title }}</p>
    <hr />
  </div>
</template>

<script>
export default {
  name: "ArticleItem",
  props: {
    article: Object,
  },
}
</script>
```

### Create

- CreateView 컴포넌트 및 라우터 작성

```vue
<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
  </div>
</template>

<script>
export default {
  name: "CreateView",
}
</script>
```

```js
// router/index.js

const routes = [
  
  {
    path: "/create",
    name: "create",
    component: CreateView,
  },
]
```

- Form 생성 및 데이터 정의

```vue
<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form>
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title" /><br />
      <label for="content">내용 : </label>
      <textarea 
        id="content" cols="30" rows="10" 
        v-model="content"
      ></textarea><br />
      <input type="submit" />
    </form>
  </div>
</template>

<script>
export default {
  name: "CreateView",
  data() {
    return {
      title: null,
      content: null,
    }
  },
}
</script>
```

- `v-on:{event}.prevent` 를 활용하여 submit 이벤트 동작을 취소하기

```vue
<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      
    </form>
  </div>
</template>
```

- actions 에 여러 개의 데이터를 넘길 때 하나의 object 로 만들어서 전달

```vue
<!-- views/CreateView.vue -->

<script>
export default {
  
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const payload = {
        title,
        content,
      }
      this.$store.dispatch("createArticle", payload)
    },
  },
}
</script>
```

- **`v-mode.trim`** 을 활용하여 입력 값의 공백을 제거

```vue
<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form>
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title" /><br />
      <label for="content">내용 : </label>
      <textarea
        id="content"
        cols="30"
        rows="10"
        v-model.trim="content"
      ></textarea
      ><br />
      <input type="submit" />
    </form>
  </div>
</template>
```

- 데이터가 없는 경우 `alert` & 데이터가 있는 경우 actions 로 전달

```vue
<script>
export default {
  
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert("제목을 입력해주세요")
      } else if (!content) {
        alert("내용을 입력해주세요")
      } else {
        const payload = {
          title,
          content,
        }
        this.$store.dispatch("createArticle", payload)
      }
    },
  },
}
</script>
```

- `actions` 에서는 넘어온 데이터를 활용하여 article 생성 후 mutations 호출
  - 이때 id 로 article_id 활용

```js
// store/index.js

actions: {
  createArticle(context, payload) {
    const article = {
      id: context.state.article_id,
      title: payload.title,
      content: payload.content,
      createdAt: new Date().getTime(),
    }
    context.commit("CREATE_ARTICLE", article)
  },
},
```

- `mutations` 에서는 전달된 article 객체를 사용해 게시글 작성
  - 다음 게시글을 위해 article_id 값 1 증가

```js
// store/index.js

mutations: {
  CREATE_ARTICLE(state, article) {
    state.articles.push(article)
    state.article_id = state.article_id + 1
  },
},
```

- CreateView 컴포넌트에 Index 페이지로 이동하는 뒤로가기 링크 추가

```vue
<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>

    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>
```

- 게시글 생성 후 Index 페이지로 이동하도록 네비게이터 작성

```js
<!-- views/CreateView.vue -->

<script>
  methods: {
    createArticle() {

      this.$store.dispatch("createArticle", payload)
      this.$router.push({ name: "index" })
    },
  },
```

- IndexView 컴포넌트에 게시글 작성 페이지로 이동하는 링크 추가

```vue
<!-- views/IndexView.vue -->

<template>
  <div>
    <h1>Articles</h1>
    <router-link :to="{ name: 'create' }">게시글 작성</router-link>
    <hr />
    <ArticleItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>
```

### Detail

**Detail  구현**

- DetailView 컴포넌트 및 라우터 작성
- id 를 동적인자로 전달

```vue
<!-- views/DetailView.vue -->

<template>
  <div>
    <h1>Detail</h1>
  </div>
</template>

<script>
export default {
  name: "DetailView",
}
</script>
```

```js
// router/index.js

const routes = [

  {
    path: "/:id",
    name: "detail",
    component: DetailView,
  },
]
```

- article 정의 및 `state` 에서 articles 가져오기

```vue
<!-- views/DetailView.vue -->
<script>
export default {
  data() {
    return {
      article: null,
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
  },
}
</script>
```

- articles 에서 동적인자를 통해 받은 id 에 해당하는 article 가져오기
- 이때, 동적 인자를 통해 받은 id 는 str 이므로 형변환을 해서 비교

```vue
<!-- views/DetailView.vue -->
<script>
methods: {
  getArticleById() {
    const id = this.$route.params.id
    for (const article of this.articles) {
      if (article.id === Number(id)) {
        this.article = article
        break
      }
    }
  }
}
</script>
```

- article 출력

```vue
<!-- views/DetailView.vue -->

<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article.id }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성시간 : {{ article.createdAt }}</p>
  </div>
</template>
```

- `created` lifecycle hook을 통해

  인스턴스가 생성되었을 때 article 을 가져오는 함수 호출

```vue
<!-- views/DetailView.vue -->
<script>
methods: {
  getArticleById(id) {
    for (const article of this.articles) {
      if (article.id === Number(id)) {
        this.article = article
        break
      }
    }
  }
},
  created() {
    this.getArticleById(this.$route.params.id)
  }
</script>
```

**만약 서버에서 데이터를 가져왔다면?**

- state 를 통해 데이터를 동기적으로 가져오지만, 실제로는 서버로부터 가져옴
  - 데이터를 가져오는데 시간이 걸림
- `created` 를 주석처리하고 데이터가 서버로부터 오는데 시간이 걸림을 가정해보자

```vue
<!-- views/DetailView.vue -->

<script>
export default {
  // created() {
  //   this.getArticleById(this.$route.params.id)
  // },
}
```

- 그런데 article 이 `null` 이기 때문에 id 등의 속성을 가져올 수 없음
- optional chaining(**`?.`**)을 통해 article 객체가 있을 때만 출력되도록 수정
- created 주석을 다시 해제

```vue
<!-- views/DetailView.vue -->

<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>글 작성시간 : {{ article?.createdAt }}</p>
  </div>
</template>

<script>
export default {
  created() {
    this.getArticleById(this.$route.params.id)
  },
}
```

**[참고] [Optional Chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)** 

- Optional chaining (**`?.`**) 앞의 평가 대상이 undefined 나 null 이면

  에러가 발생하지 않고 undefined 를 반환 (ES2020 에서 추가된 문법)

```vue
<script>
const userInfo = {
  name: {
    last: "Stark",
  },
  address: {
    city: "Seoul",
  },
  getInfo() {
    console.log(this.name)
  },
}

// Optional chaining 미사용
const myCity = userInfo.address && userInfo.address.city

// Optional chaining 사용
const myCity = userInfo.address?.city

// Optional chaining 사용 (메서드 호출 시)
userInfo.getInfo?.()
</script>
```

**Date in JavaScript**

- JavaScript 에서 시간을 나타내는 `Date` 객체는 1970년 1월 1일 UTC(협정 세계시)

  자정과의 시간 차이를 밀리초로 나타내는 정수 값을 담음

  - **`Data().toLocaleString()`** 을 사용하여 변환

- 로컬시간으로 변환해주는 `computed` 값 작성 및 출력

```vue
<!-- views/DetailView.vue -->

<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
<!-- <p>글 작성시간 : {{ article?.createdAt }}</p> -->
    <p>작성시간 : {{ articleCreatedAt }}</p>
  </div>
</template>

<script>
export default {
  computed: {

    articleCreatedAt() {
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString()
      return createdAt
    },
  },
}
```

- DetailView 컴포넌트에 뒤로가기 링크 추가

```vue
<!-- views/DetailView.vue -->

<template>
  <div>
    
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>
```

- 각 게시글을 클릭하면  detail 페이지로 이동하도록 ArticleItem 에 이벤트 추가
- `v-on` 이벤트 핸들러에도 인자 전달 가능

```vue
<!-- components/ArticleItem.vue -->

<template>
  <div @click="goDetail(article.id)">
    <p>글 번호 : {{ article.id }}</p>
    <p>제목 : {{ article.title }}</p>
    <hr />
  </div>
</template>

<script>
export default {
  methods: {
    goDetail(id) {
      this.$router.push({ name: "detail", params: { id } })
    },
  },
}
</script>
```

### Delete

**Delete 구현**

- DetailView 컴포넌트에 삭제 버튼을 만들고, mutations 를 호출

```vue
<!-- views/DetailView.vue -->

<template>
  <div>
    
    <button @click="deleteArticle">삭제</button><br />
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  methods: {
    deleteArticle() {
      this.$store.commit("DELETE_ARTICLE", this.article.id)
    },
  },
}
</script>
```

- `mutations` 에서 id 에 해당하는 게시글을 지움

```js
// store/index.js

mutations: {
  DELETE_ARTICLE(state, id) {
    state.articles = state.articles.filter((article) => {
      return !(article.id === id)
    })
  }
},
```

- 삭제 후 index 페이지로 이동하도록 네비게이션 작성

```vue
<!-- views/DetailView.vue -->

<script>
export default {
  methods: {
    deleteArticle() {
      this.$store.commit("DELETE_ARTICLE", this.article.id)
      this.$router.push({ name: "index" })
    },
  },
}
</script>
```

### 404 Not Found

**404 페이지 구현**

- NotFound404 컴포넌트 및 라우터 작성
- Detail 에 대한 route 보다 먼저 등록해줘야 함
  - 또한, /404 로 등록하면 404 번째 게시글과 혼동할 수 있게 됨

```vue
<!-- views/NotFound404.vue -->

<template>
  <div>
    <h1>404 Not Found</h1>
  </div>
</template>

<script>
export default {
  name: "NotFound404",
}
</script>
```

```js
// router/index.js

const routes = [
  
  {
    path: "/404-not-found",
    name: "NotFound404",
    component: NotFound404,
  },
  {
    path: "/:id",
    name: "detail",
    component: DetailView,
  },
]
```

- DetailView 컴포넌트에 id 에 해당하는 article 이 없으면 404 페이지로 이동

```vue
<!-- views/DetailView.vue -->

<script>
export default {
  methods: {
    getArticleById(id) {
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article
          break
        }
      }
      if (!this.article) {
        this.$router.push({ name: "NotFound404" })
      }
    },
  },
}
</script>
```

- 요청한 리소스가 존재하지 않는 경우

  없는 id 가 아닌 전혀 다른 요청에도 대비하여 404 page 로 `redirect` 시키기

  - **`$router.push`** 와 마찬가지로 `name` 을 이용하여 이동할 수 있음
    - **최하단에 작성해야 함**

```js
// router/index.js

const routes = [

  {
    path: "*",
    redirect: { name: "NotFound404" },
  },
]
```

## finish

- [UX & UI](#1-ux--ui)
- [Vue Router](#2-vue-router)
- [Navigation Guard](#3-navigation-guard)
- [Articles app with Vue](#4-articles-app-with-vue)
