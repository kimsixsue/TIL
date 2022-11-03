[Vue CLI](#vue-cli)

1. [Vue CLI](#1-vue-cli)
   - [Node.js](#nodejs)
   - [Vue CLI](#vue-cli-1)
   - [Vue CLI 프로젝트 구조](#vue-cli-프로젝트-구조)
2. [SFC](#2-sfc)
   - [Component](#component)
   - [SFC](#sfc)
   - [Vue component](#vue-component)
   - [Vue component 실습](#vue-component-실습)
3. [Pass Props & Emit Events](#3-pass-props--emit-events)

   - [Data in components](#data-in-components)

   - [Pass Props](#pass-props)

   - [Emit Event](#emit-event)


* [finish](#finish)

# Vue CLI

## 1. Vue CLI

### Node.js

- 자바스크립트는 브라우저를 조작하는 유일한 언어
- 자바스크립트를 구동하기 위한 런타임 환경인 Node.js 로 인해 브라우저가 아닌 환경에서도 구동할 수 있게 됨
  - Chrome V8 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경을 제공
  - Browser만 조작 가능했으나, Server-Side-Programming 또한 가능해짐

**NPM (Node Package Manage)**

- 자바스크립트 패키지 관리자
  - 다양한 의존성 패키지를 관리
- Node.js의 기본 패키지 관리자
- Node.js 설치 시 함께 설치됨

### Vue CLI

- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 프러그인, GUI, Babel 등 다양한 tool 제공

**Vue CLI Quick Start**

- 설치

  ```bash
  $ npm install -g @vue/cli
  ```

- 프로젝트 생성

  - vscode terminal에서 진행

  ```bash
  $ vue create vue-cli
  ```

- Vue 버전 선택(Vue 2)

- 출력된 명령어 실행

  - 프로젝트 디렉토리로 이동

    ```bash
    $ cd vue-cli
    ```

  - 프로젝트 실행

    ```bash
    $ npm run serve
    ```

### Vue CLI 프로젝트 구조

**node_modules**

- node.js 환경의 여러 의존성 모듈
- `.gitignore` 에 넣어 주어야 하며, Vue 프로젝트를 생성하면 자동으로 추가됨

**node_modules - `Babel`**

- "JavaScript compiler"
- 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구
- 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
  - 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생
  - 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구
  - 원시 코드(최신 버전)를 목적 코드(구 버전)으로 옮기는 번역기가 등장하면서 더 이상 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있음

**node_modules - `Webpack`**

- "static module bundler"
- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
- modules with dependencies => bundle your scripts => static assets
- 의존성을 Webpack 이 담당해 주므로 개발자는 `npm install` 을 사용해 다양한 모듈을 한 번에 설치하고 각 모듈을 사용해 개발에 집중할 수 있음
  - `package-lock.json` 디렉토리에서 `$ npm install`

**`Module`**

- 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
- 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이 module 즉, js 파일 하나가 하나의 모듈
- 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨
- 여러 모듈 시스템
  - ESM(ECMA Script Module), AMD, CommonJS, UMD

**Module 의존성 문제**

- 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
  - Webpack은 이 모듈 간의 의존성 문제를 해결하기 위해 등장

**`Bundler`**

- 모듈 의존성 문제를 해결해주는 작업이 Bundling
- 이러한 일을 해주는 도구가 Bundler이고, Webpack은 다양한 Bundler 중 하나
- 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개)로 만들어짐
- Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게 됨
- snowpack, parcel, rollup.js 등의 webpack 이외에도 다양한 모듈 번들러 존재
- **Vue CLI는 이러한 Babel, WebPack 에 대한 초기 설정이 자동으로 되어 있음**

**package.json**

- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함

**package-lock.json**

- node_modules 에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
- 사용 할 패키지의 버전을 고정
- 개발 과정 간의 의존성 패키지 충돌 방지

**public/index.html**

- Vue 앱의 뼈대가 되는 html 파일
- Vue 앱과 연결될 요소가 있음

```html
<div id="app"></div>
```

**src/**

- src/assets
  - 정적 파일을 저장하는 디렉토리
- src/components
  - 하위 컴포넌트들이 위치
- src/App.vue
  - 최상위 컴포넌트
  - public/index.html 과 연결됨
- src/main.js
  - webpack 이 빌드를 시작할 때 가장 먼저 불러오는 entry point
  - public/index.html 과 src/App.vue 를 연결시키는 작업이 이루어지는 곳
  - Vue 전역에서 활용 할 모듈을 등록할 수 있는 파일

## 2. SFC

### Component

- UI 를 독립적이고 재 사용 가능한 조각들로 나눈 것
  - 즉, 기능 별로 분화한 코드 조각
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree 로 구성하는 것이 보편적임
  - Vue에서는 src/App.vue 를 root node 로 하는 tree의 구조를 가짐
- 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공

- 웹 서비스는 여러 개의 컴포넌트로 이루어져 있음

- 하나의 컴포넌트를 만들어주면 반복되는 UI를 쉽게 처리할 수 있음

  > https://v2.vuejs.org/v2/guide/components.html#Organizing-Components

**Componet based architecture 특징**

- 관리가 용이
  - 유지/보수 비용 감소
- 재사용성
- 확장 가능
- 캡슐화
- 독립적

### SFC

**component in Vue**

- 이름이 있는 재사용 가능한 Vue instance
- `new Vue()` 로 만든 인스턴스

**SFC (Single File Component)**

- 하나의 `.vue` 파일이 하나의 `Vue instance` 이고, 하나의 `컴포넌트` 이다
- Vue instance 에서는 HTML, CSS, JavaScript 코드를 한번에 관리

  - 이 Vue instance 를 기능 단위로 작성하는 것이 핵심

- 컴포넌트 기반 개발의 핵심 기능

**정리**

- HTML, CSS, 그리고 JavaScript 를`.vue` 라는 확장자를 가진 파일 안에서 관리하며 개발
- 이 파일을 Vue instance, 또는 Vue component 라고 하며, 기능 단위로 작성
- Vue CLI 가 Vue 를 Component based 하게 사용하도록 도와줌

### Vue component

**Vue component 구조**

- HTML 템플릿
  - HTML의 body 부분
  - 눈으로 보여지는 요소 작성
  - 다른 컴포넌트를 HTML 요소처럼 추가 가능
- JavaScript 스크립트
  - JavaScript 코드가 작성되는 곳
  - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성 됨
- CSS 스타일
  - CSS가 작성되며 컴포넌트의 스타일을 담당

**Vue component 구조 정리**

- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
- root에 해당하는 최상단의 component가 `App.vue`
- 이 App.vue 를 index.html 과 연결
- 결국 index.html 파일 하나만을 rendering
  - 이게 바로 SPA

### Vue component 실습

**현재 구조**

- Vue CLI 를 실행하면 이미 HelloWorld.vue 라는 컴포넌트가 생성되어 있고 App.vue 에 등록되어 사용되고 있음
  - `npm run serve` 명령어를 진행 했을 때 나온 화면의 대부분이 HelloWorld.vue

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue/js App" />
  </div>
</template>
```

**MyComponent.vue**

```vue
<!-- MyComponent.vue -->
<template>
  <div>
    <h1>This is my component</h1>
  </div>
</template>

<script>
export default {
  name: "MyComponent",
}
</script>

<style></style>
```

1. src/components/ 안에 생성
2. script 에 이름 등록
3. template 에 요소 추가
   - **template 안에는 반드시 하나의 요소만 추가 가능**
     - **비어 있어도 안됨**
     - **해당 요소 안에 추가 요소를 작성해야 함**

**component 등록 3 단계**

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <!-- 3. 보여주기 -->
    <HelloWorld msg="Welcome to Your Vue/js App" />
  </div>
</template>

<script>
// 1. 불러오기
import HelloWorld from "./components/HelloWorld"

export default {
  name: "App",
  components: {
    // 2. 등록하기
    HelloWorld,
  },
}
</script>
```

1. 불러오기
   - **`import {instance name} from {위치}`**
   
   - instance name은 instance 생성 시 작성한 name
   
   - `@` 는 src 의 shortcut
   
     ```json
     "compilerOptions": {
       "paths": {
         "@/*": [
           "src/*"
     ```
   
   - `.vue` 생략 가능

```vue
<!-- App.vue -->
<script>
import HelloWorld from "./components/HelloWorld"
// 1. 불러오기
import MyComponent from "@/components/MyComponent"

export default {
  name: "App",
  components: {
    HelloWorld,
    MyComponent, // 2. 등록하기
  },
}
</script>
```

2. 등록하기

3. 보여주기

   - 닫는 태그만 있는 요소처럼 사용

     - 로고와 기존 컴포넌트 사이에 위치

     ```vue
     <!-- App.vue -->
     <template>
       <div id="app">
         <img alt="Vue logo" src="./assets/logo.png" />
         <MyComponent />
         <!-- 3. 보여주기 -->
         <HelloWorld msg="Welcome to Your Vue/js App" />
       </div>
     </template>
     ```

**자식 컴포넌트 작성**

```vue
<!-- MyComponent.vue -->
<template>
  <div class="border">
    <!-- 추가 -->
    <h1>This is my component</h1>
  </div>
</template>

<style>
.border {
  /* 추가 */
  border: solid;
}
</style>
```

- 자식 관계를 표현하기 위해 기존 MyComponent에 간단한 border 를 추가

```vue
<!-- MyComponentItem.vue -->
<template>
  <div>
    <h3>This is componentItem</h3>
  </div>
</template>

<script>
export default {
  name: "MyComponentItem", // 생성
}
</script>
```

- src/components/ 안에 MyComponentItem.vue 생성

```vue
s
```

- MyComponent 에 MyComponentItem 등록

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <MyComponent />
    <!-- 재사용성 -->
    <MyComponent />
    <!-- 재사용성 -->
    <HelloWorld msg="Welcome to Your Vue/js App" />
  </div>
</template>
```

- component의 재사용성

## 3. Pass Props & Emit Events

### Data in components

- 동적 웹페이지에서 다뤄야 할 데이터가 등장
- 한 페이지 내에서 같은 데이터를 공유 해야 함

  - 하지만 페이지들은 component 로 구분이 되어있음

- 각 Component는 독립적이므로 서로 다른 data 를 갖게 될 것이다.
- 컴포넌트는 부모-자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고받게 하자
- 데이터의 흐름을 파악하기 용이
- 유지 보수하기 쉬워짐

**pass props & emit event**

- 부모 => 자식으로의 데이터의 흐름
  - pass **props** 의 방식
- 자식 => 부모로의 데이터의 흐름
  - **emit** event 의 방식

### Pass Props

- 요소의 property 속성을 사용하여 데이터 전달
- props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props 를 명시적으로 선언해야 함

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <MyComponent />
    <HelloWorld msg="Welcome to Your Vue/js App" />
  </div>
</template>
```

- props
  - HelloWorld 컴포넌트 msg라는 property 넘김
  - msg 사용 출력
- App.vue 의 `<HelloWorld/>` 요소에 `msg="~"` 라는 property 를 설정하였고, 하위 컴포넌트인 HelloWorld는 자신에게 부여된 msg property 를 template 에서 `{{ msg }}` 의 형태로 사용한 것

```vue
<!-- HelloWorld.vue -->
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>
```

- 부모 => 자식으로의 data 전달 방식을 pass props 라고 함
- 정적인 데이터를 전달하는 경우 static props 라고 명시하기도 함
- 요소에 속성을 작성하듯이 사용 가능하여, `prop-data-name="value"` 의 형태로 데이터를 전달
  - 이때 속성의 키 값은 kebab-case 를 사용

```vue
<!-- HelloWorld.vue -->
<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
}
</script>
```

- Prop 명시

- 데이터를 받는 쪽, 즉 하위 컴포넌트에서도 props에 대해 명시적으로 작성 해주어야 함

- 전달 받은 props 를 type과 함께 명시

- 컴포넌트를 문서화할 뿐만 아니라, 잘못된 타입이 전달하는 경우 브라우저의 자바스크립트 콘솔에서 사용자에게 경고

  > https://v2.vuejs.org/v2/guide/components-props.html#Prop-Validation

**MyComponent to MyComponentItem**

```vue
<!-- MyComponent.vue -->
<template>
  <div class="border">
    <h1>This is my component</h1>
    <MyComponentItem static-props="component에서 componentItem으로" />
  </div>
</template>
```

```vue
<!-- MyComponentItem.vue -->
<template>
  <div>
    <h3>This is componentItem</h3>
    <p>{{ staticProps }}</p>
  </div>
</template>

<script>
export default {
  name: "MyComponentItem",
  props: {
    staticProps: String,
  },
}
</script>
```

**Pass Props convention**

- 부모에서 넘겨주는 props

  - `kebab-case`

    (HTML 속성명은 대소문자를 구분하지 않기 때문)

- 자식에서 받는 props
  - `camelCase`
- 부모 html 템플릿에서 kebab-case 로 넘긴 변수를 자식의 vue 스크립트에서 자동으로 camelCase 로 변환하여 인식함

**Dynamic props**

- 변수를 props 로 전달할 수 있음
- v-bind directive 를 사용해 데이터를 동적으로 바인딩
- 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨

**Dynamic props 실습**

```vue
<!-- MyComponent.vue -->
<template>
  <div class="border">
    <h1>This is my component</h1>
    <MyComponentItem
      static-props="component에서 componentItem으로"
      v-bind:dynamic-props="dynamicProps"
      /><!-- Dynamic props -->
  </div>
</template>

<script>
export default {
  // Dynamic props
  data : function () {
    return {
      dynamicProps : "It's in data"
    }
  }
}
</script>
```

```vue
<!-- MyComponentItem.vue -->
<template>
  <div>
    <h3>This is componentItem</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
     <!-- Dynamic props -->
  </div>
</template>

<script>
export default {
  name: "MyComponentItem",
  props: {
    staticProps: String,
    // Dynamic props
    dynamicProps: String,
  },
}
</script>
```

**컴포넌트의 data 함수**

```js
data: function () {
  return {
    // component's data in here
  }
},
```

- 각 vue 인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 return 반환하여 사용해야 함

  > https://v2.vuejs.org/v2/guide/components.html#data-Must-Be-a-Function

**Pass Props**

- `v-bind:dynaimc-props="dynamicProps"` 는

  앞의 key값(`dynamic-props`) 이란 이름으로

  뒤의 `" "` 안에 오는 데이터(`dynamicProps`) 를 전달하겠다는 뜻

- 즉, `v-bind:my-props="dynamicProps"` 로 데이터를 넘긴다면,

  자식 컴포넌트에서 `myProps` 로 데이터를 받아야 함

```vue
<!-- MyComponent.vue -->
<template>
  <div class="border">
    <h1>This is my component</h1>
    <MyComponentItem
      static-props="component에서 componentItem으로"
      v-bind:my-props="dynamicProps"
    />
  </div>
</template>
```

```vue
<!-- MyComponentItem.vue -->
<template>
  <div>
    <h3>This is componentItem</h3>
    <p>{{ staticProps }}</p>
    <p>{{ myProps }}</p>
  </div>
</template>

<script>
export default {
  name: "MyComponentItem",
  props: {
    staticProps: String,
    myProps: String,
  },
}
</script>
```

- `v-bind` 로 묶여있는 `" "` 안의 구문은 javascript 의 구문으로 볼 수 있음
  - 따라서 `dynamicProps` 라고 하는 변수에 대한 `data` 를 전달할 수 있는 것

```vue
<!-- static props 로 string 으로써의 "1" 을 전달 -->
<SomeComponent num-props="1" />
<!-- dynamic props 로 숫자로써의 1 을 전달 -->
<SomeComponent v-bind:num-props="1" />
```

**`단방향 데이터 흐름`**

- 모든 props 는 부모에서 자식으로 즉 아래로 단방향 바인딩을 형성

- 부모 속성이 업데이트되면 자식으로 흐르지만 반대 방향은 아님
  - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop 들이 최신 값으로 새로고침 됨
  
- 목적

  - 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지

- 하위 컴포넌트에서 prop 를 변경하려고 시도해서는 안되며 그렇게 하면 Vue 는 콘솔에서 경고를 출력함

  > https://v2.vuejs.org/v2/guide/components-props.html#One-Way-Data-Flow

  > All props form a **one-way-down binding** between the child property and the parent one: when the parent property updates, it will flow down to the child, but not the other way around. This prevents child components from accidentally mutating the parent’s state, which can make your app’s data flow harder to understand.

### Emit Event

- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 `이벤트를 발생시킴`
- 이벤트를 발생시키는 게 어떻게 데이터를 전달하는 것이냐?
  1. 데이터를 이벤트 리스너의 **콜백함수의 인자로 전달**
  2. 상위 컴포넌트는 해당 **이벤트를 통해 데이터를 받음**

**`$emit`**

- **`$emit`** 메서드를 통해 부모 컴포넌트에 이벤트를 발생
  - **`$emit('event-name')`** 형식으로 사용하며 부모컴포넌트에 **`event-name`** 이라는 이벤트가 발생했다는 것을 알림
  - 마치 사용자가 **마우스 클릭**을 하면 `click` 이벤트가 발생하는 것처럼 `$emit('event-name')` 가 실행되면 `event-name` 이벤트가 발생하는 것
- 참고) `$`
  - javascript 는 변수에 `_`, `$` 두개의 특수문자를 사용 가능
  - 이때, 기존에 사용하던 변수, 메서드들과 겹치지 않게 하기 위해서 vue 는 `$emit` 를 이벤트 이벤트 전달을 위한 방식으로 택하였다.

**Emit Event**

```vue
<!-- MyComponentItem.vue -->
<template>
  <div>
    <button v-on:click="childToParent">클릭</button><br />
  </div>
</template>

<script>
export default {
  methods: {
    ChildToParent: function () {
      this.$emit("child-to-parent")
    },
  },
}
</script>
```

1. 자식 컴포넌트에 버튼을 만들고 클릭 이벤트를 추가
2. `$emit` 을 통해 부모 컴포넌트에게 `child-to-parent` 이벤트를 트리거

```vue
<!-- MyComponent.vue -->
<template>
  <div class="border">
    <h1>This is my component</h1>
    <MyComponentItem 
      v-on:child-to-parent="parentGetEvent" 
      />
  </div>
</template>

<script>
export default {
  methods: {
    parentGetEvent: function () {
      console.log("자식 컴포넌트에서 발생한 이벤트")
    },
  },
}
</script>
```

- emit 된 이벤트를 상위 컴포넌트에서 청취 후 핸들러 함수 실행

**Emit Event 흐름 정리**

1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수 (`ChildToParent`) 호출
2. 호출된 함수에서 **`$emit`** 을 통해 상위 컴포넌트에 이벤트(`child-to-parent`) 발생
3. 상위 컴포넌트는 자식 컴포넌트가 발생시킨 이벤트(`child-to-parent`)를 청취하여 연결된 핸들러 함수(`parentGetEvent`) 호출

**emit with data**

```vue
<!-- MyComponentItem.vue -->
<template>
  <div>
    <button v-on:click="childToParent">클릭</button><br />
  </div>
</template>

<script>
export default {
  methods: {
    ChildToParent: function () {
      this.$emit("child-to-parent", "child data")
    },
  },
}
</script>
```

- 이벤트를 emit 발생시킬 때 인자로 **`데이터를 전달`** 가능

```vue
<!-- MyComponent.vue -->
<template>
  <div class="border">
    <h1>This is my component</h1>
    <MyComponentItem 
      v-on:child-to-parent="parentGetEvent" 
      />
  </div>
</template>

<script>
export default {
  methods: {
    parentGetEvent: function (inputData) {
      console.log("자식 컴포넌트에서 발생한 이벤트")
      console.log(`child component로부터 ${inputData}를 받음`)
    },
  },
}
</script>
```

- 이렇게 전달한 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러 함수의 인자로 사용 가능

**emit with data 흐름 정리**

1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수 (`ChildToParent`) 호출

2. 호출된 함수에서 **`$emit`** 을 통해 부모 컴포넌트에 이벤트(`child-to-parent`)를 발생

   - 이벤트에 데이터(`child data`)를 함께 전달

3. 부모 컴포넌트는 자식 컴포넌트의 이벤트(`chilc-to-parent`)를 청취하여

   연결된 핸들러 함수(`parentGetEvent`) 호출,

   함수의 인자로 전달된 데이터(`child data`)가 포함되어 있음

4. 호출된 함수에서 **`console.log(child data)`** 실행

```vue
<!-- TodoListInput.vue -->
<template>
  <div>
    <input type="text" v-model="inputData" />
    <!-- TodoListInput 컴포넌트의 버튼을 누르면 add-todo 이벤트가 발생한다.  -->
    <button v-on:click="onClick">추가</button>
  </div>
</template>

<script>
export default {
  name: "TodoListInput",
  data: function () {
    return {
      inputData: "",
    }
  },
  methods: {
    onClick: function () {
      // (이벤트 발생 시 data의 text 값도 함께 전달한다.)
      this.$emit("add-todo", this.inputData)
    },
  },
}
</script>
```

```vue
<!-- TodoList.vue -->
<template>
  <div>
    <TodoListInput v-on:add-todo="onAddTodo" />
    <!-- TodoList 컴포넌트에서 add-todo 이벤트를 청취하면,  -->
    <!-- onAddTodo 메서드를 실행한다. -->
  </div>
</template>

<script>
import TodoListInput from "@/components/TodoListInput"

export default {
  name: "TodoList",
  components: {
    TodoListInput,
  },
  methods: {
    // onAddTodo 메서드에서는
    onAddTodo: function (inputData) {
      // TodoListInput 컴포넌트에서 전달받은 값을
      console.log(
        // console.log 함수를 통해 출력한다.
        `TodoListInput 컴포넌트에서 전달받은 값은 ${inputData}`
      )
    },
  },
}
</script>
```

**emit with dynamic data**

- pass props 와 마찬가지로 동적인 데이터도 전달 가능

```vue
<!-- MyComponentItem.vue -->
<template>
  <div>
    <input
      type="text"
      v-model="childInputData"
      v-on:keyup.enter="childInput"
    />
  </div>
</template>

<script>
export default {
  name: "MyComponentItem",
  data: function () {
    return {
      childInputData: null,
    }
  },
  methods: {
    childInput: function () {
      this.$emit("child-input", this.childInputData)
      this.childInputData = ""
    },
  },
}
</script>
```

```vue
<!-- MyComponent.vue -->
<template>
  <div class="border">
    <h1>This is my component</h1>
    <MyComponentItem 
      v-on:child-input="getDynamicData" 
      />
  </div>
</template>

<script>
import MyComponentItem from "@/components/MyComponentItem"

export default {
  name: "MyComponent",
  components: {
    MyComponentItem,
  },
  methods: {
    getDynamicData: function (inputData) {
      console.log(`child component로부터 ${inputData}를 입력받음`)
    },
  },
}
</script>
```

**emit with dynamic data 흐름 정리**

1. 자식 컴포넌트에 있는 `keyup.enter` 이벤트를 청취하여

   연결된 핸들러 함수(`ChildInput`) 호출

2. 호출된 함수에서 `$emit` 을 통해 부모 컴포넌트에 이벤트(`child-input`)를 발생

   - 이벤트에 `v-model` 로 바인딩 된 `입력받은 데이터`를 전달

3. 상위 컴포넌트는 자식 컴포넌트의 이벤트(`child-input`)를 청취하여

   연결된 핸들러 함수(`getDynamicData`) 호출,

   함수의 인자로 전달된 데이터가 포함되어 있음

4. 호출된 함수에서 `console.log(입력받은 데이터)` 실행

**Directives `v-on`**

- `:` 을 통해 전달된 인자에 따라 특별한 modifiers (수식어)가 있을 수 있음

  > https://v2.vuejs.org/v2/api/#v-on
  >
  > https://v2.vuejs.org/v2/guide/components-custom-events.html#Binding-Native-Events-to-Components

  - **`.native`** - listen for a **native** event on the root element of component.

  - 부모가 자식 컴포넌트의 이벤트를 v-on으로 청취할 때, 이게 일반 이벤트인지 emit 으로 발생하는 이벤트인지 구분을 못한다.

    - 컴포넌트에서 일반 이벤트를 사용할 때 작성한다. 일반 이벤트라면 뒤에 .native 를 붙인다.

    ```html
    <!-- native event on component -->
    <my-component v-on:click.native="onClick"></my-component>
    ```

**정리**

- 자식 컴포넌트에서 부모 컴포넌트로 이벤트를 발생시킴
  - 이벤트에 데이터를 담아 전달 가능
- 부모 컴포넌트에서는 자식 컴포넌트의 이벤트를 청취
  - 전달받은 데이터는 이벤트 핸들러 함수의 인자로 사용

**pass props / emit event 컨벤션**

- HTML 요소에서 사용할 때는 `kebab-case`
- JavaScript 에서 사용할 때는 `camelCase`
- props

  - 상위 => 하위 흐름에서 HTML 요소로 내려줌 : `kebab-case`
  - 하위에서 받을 때 JavaScript 에서 받음 : `camelCase`

- emit
  - emit 이벤트를 발생시키면 HTML 요소가 이벤트를 청취함 : `kebab-cases`
  - 메서드, 변수명 등은 JavaScript 에서 사용함 : `camelCase`

## finish

1. Vue CLI
2. SFC
3. Pass Props & Emit Events

```vue
<!-- AppChild.vue -->
<template>
  <div>
    <h1>App Child</h1>
    <!-- 
      1. 입력한 TEXT 를 childData 와 v-model로 양방향 바인딩하여 사용자가 입력한 값을 저장한다.
      2. 입력할 때 마다 emit으로 데이터를 전달하기위해 input 이벤트를 이용하여 sendData 메서드를 실행한다.
        - 엔터칠 때 마다 데이터를 전달하고 싶으면 @keyup.enter 이벤트를 사용하면 됨
     -->
    <input type="text" v-model="childData" v-on:input="sendData" />
    <p>App Data : {{ appData }}</p>
    <p>Parent Data : {{ parentData }}</p>
    <p>Child Data : {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: "AppChild",
  // Parent가 전달해주는 데이터를 받기위해 props에 선언한다.
  // 이름은 부모 컴포넌트가 전달해주는 케밥케이스 이름을 카멜 케이스 형태로 작성해준다. (html -> js)
  // 그리고 어떤 타입의 값인지 명시해준다.
  props: {
    appData: String,
    parentData: String,
  },
  data: function () {
    return {
      // 입력 데이터를 저장하기 위해 선언
      childData: null,
    }
  },
  methods: {
    // 입력 데이터를 부모 컴포넌트에 전달하기 위해 emit 이벤트 사용
    // 첫 번째 인자는 '발생하는 이벤트 이름', 두 번째 인자는 '전달하고 싶은 데이터'
    sendData: function () {
      this.$emit("child-data", this.childData)
      // emit 이벤트를 발생시켰다면 이제 부모 컴포넌트에서 이벤트 처리를 해줘야 함
    },
  },
}
</script>
```

```vue
<!-- AppParent.vue -->
<template>
  <div>
    <h1>App Parent</h1>
    <!-- 
      1. 입력한 TEXT 를 childData 와 v-model로 양방향 바인딩하여 사용자가 입력한 값을 저장한다.
      2. 입력할 때 마다 emit으로 데이터를 전달하기위해 input 이벤트를 이용하여 sendData 메서드를 실행한다.
        - 엔터칠 때 마다 데이터를 전달하고 싶으면 @keyup.enter 이벤트를 사용하면 됨
     -->
    <input type="text" v-model="parentData" v-on:input="sendData" />
    <p>AppData : {{ appData }}</p>
    <p>ChildData : {{ childData }}</p>
    <!-- 
      App.vue 에서 전달한 데이터와
      parent 컴포넌트에서 입력한 데이터를 자식 컴포넌트에 전달(prop)하고
      자식 컴포넌트에서 발생하는 이벤트를 처리한다.
     -->
    <AppChild
      v-bind:app-data="appData"
      v-bind:parent-data="parentData"
      v-on:child-data="getChild"
    />
  </div>
</template>

<script>
import AppChild from "@/components/AppChild"
export default {
  name: "AppParent",
  data: function () {
    return {
      parentData: null, // 부모(App.vue)에서 전달되는 데이터 저장
      childData: null, // 자식(AppChild.vue)에서 전달되는 데이터 저장
    }
  },
  components: {
    AppChild,
  },
  props: {
    // Parent가 전달해주는 데이터를 받기위해 props에 선언한다.
    // 이름은 부모 컴포넌트가 전달해주는 케밥케이스 이름을 카멜 케이스 형태로 작성해준다. (html -> js)
    // 그리고 어떤 타입의 값인지 명시해준다.
    appData: String,
  },
  methods: {
    // 현재 컴포넌트(AppParent.vue)에서 작성한 데이터를 App.vue 로 전달해주기 위한 메서드
    sendData: function () {
      this.$emit("parent-data", this.parentData)
    },
    // 자식 컴포넌트(AppChild.vue)에서 전달되는 데이터를 App.vue 로 전달해주기 위한 메서드
    // 첫 번째 인자로 자식에서 전달되는 값이니 매개변수를 선언하여 해당 값을 받는다.
    getChild(data) {
      this.childData = data
      this.$emit("send-child", data)
    },
  },
}
</script>
```

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <h1>App</h1>
    <!-- 
      입력한 TEXT 를 childData 와 v-model로 양방향 바인딩하여 사용자가 입력한 값을 저장한다.
    -->
    <input type="text" v-model="appData" />
    <p>Parent Data : {{ parentData }}</p>
    <p>Child Data : {{ childData }}</p>
    <!-- 
      App.vue 에서 입력한 데이터를 자식 컴포넌트(AppParent.vue)에 전달(prop)하고
      자식 컴포넌트에서 발생하는 이벤트를 처리한다.
      현재 AppParent.vue 에서는 2개의 이벤트가 발생한다. (Parent, Child data 전달)
     -->
    <AppParent
      v-bind:app-data="appData"
      v-on:parent-data="getParent"
      v-on:send-child="getChild"
    />
  </div>
</template>

<script>
import AppParent from "@/components/AppParent"

export default {
  name: "App",
  data: function () {
    return {
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  components: {
    AppParent,
  },
  methods: {
    // AppParent.vue 에서 전달되는 데이터 저장
    getParent: function (data) {
      this.parentData = data
    },
    // AppChild.vue 에서 전달되는 데이터 저장
    // (AppParent.vue가 다시 App.vue로 전달하는 형태)
    // (AppChild => AppParent.vue => App.vue)
    getChild(data) {
      this.childData = data
    },
  },
}
</script>

<style>
#app {
  font-family: D2Coding, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

