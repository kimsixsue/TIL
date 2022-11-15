[Vue_DRF](#vue_DRF)

1. [Vue with DRF](#1-vue-with-DRF)
   - [Server & Client](#server--client)
   - [Again DRF](#again-DRF)
   - [Back to Vue](#back-to-vue)
   - [Vue with DRF](#vue-with-DRF)
2. [CORS](#2-cors)
   - [Cross-Origin Resource Sharing](#cross-origin-resource-sharing)
   - [How to set CORS](#how-to-set-cors)
   - [Vue with DRF (feat.CORS)](#vue-with-drf-featcors)
	   - [Article Read](#article-read)
	   - [Article Create](#article-create)
	   - [Article Detail](#article-detail)
3. [DRF Auth System](#3-DRF-auth-system)
   - [Authentication & Authorization](#authentication--authorization)
   - [How to authentication determined](#how-to-authentication-determined)
   - [dj-rest-auth](#dj-rest-auth)
   - [Permission setting](#permission-setting)
4. [DRF Auth with Vue](#4-DRF-auth-with-vue)
   - [SignUp Request](#signup-request)
   - [LogIn Request](#login-request)
   - [IsAuthenticated in Vue](#isauthenticated-in-vue)
   - [Request with Token](#request-with-Token)
5. [drf-spectacular](#5-drf-spectacular)
   - [finish](#finish)

# Vue_DRF

## 1. Vue with DRF

- Server와 Client의 통신 방법 이해하기
- CORS 이슈 이해하고 해결하기
- DRF Auth System 이해하기
- Vue와 API server 통신하기

### Server & Client

- server

  - 클라이언트에게 **정보**와 **서비스**를 제공하는 컴퓨터 시스템

  - 서비스 전체를 제공 ==  Django Web Service

    - Django를 통해 전달받은 HTML에는

      하나의 웹 페이지를 구성할 수 있는 모든 데이터가 포함

    - 즉, 서버에서 모든 내용을 렌더링, 하나의 HTML 파일로 제공

    - 정보를 포함한 web 서비스를 구성하는 모든 내용을 서버 측에서 제공

  - 정보를 제공 == DRF API Service

    - Django를 통해 관리하는 정보만을 클라이언트에게 제공

    - DRF를 사용하여 JSON으로 변환

- Client

  - **Server가 제공하는 서비스에 적절한 요청** 을 통해

    - Server가 정의한 방식대로 요청 인자를 넘겨 요청
    - Server는 정상적인 요청에 적합한 응답 제공

  - **Server로부터 반환 받은 응답을 사용자에게 표현**하는 기능을 가진

    프로그램 혹은 시스템

    - 사용자의 요청에 적합한 data를 server에 요청하여 응답 받은 결과로

      **적절한 화면을 구성**

**정리**

- Server는 정보와 서비스를 제공
  - DB와 통신하며 데이터를 생성, 조회, 수정, 삭제를 담당
  - 요청을 보낸 Client에게 정상적인 요청이었다면 처리한 결과를 응답
- Client는 사용자의 정보 요청을 처리, server에게 응답 받은 정보를 표현
  - Server에게 정보(데이터)를 요청
  - 응답 받은 정보를 가공하여 화면에 표현

### Again DRF

```bash
# back-server
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata articles.json comments.json
```

### Back to Vue

```bash
# fronst-server
$ npm install # package install
$ npm run serve
```

### Vue with DRF

**AJAX 요청 준비**

```bash
$ npm install axios # axios 설정, 설치
```

```js
// store/index.js
import axios from 'axios'
// 요청 보낼 API server 도메인 변수에 담기
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  actions: { // 메소드 정의
    getArticles(context) { 
      axios({
        method: 'get', // 요청 보낼 경로 확인 필수
        url: `${API_URL}/api/v1/articles/`,
      }) // 성공 시 .then
        .then((res) =>
          console.log(res, context)
        ) // 실패 시 .catch
        .catch((err) => console.log(err))
    },
  },
})
```

```vue
<!-- views/ArticleView.vue -->
<script>
export default {
  name: 'ArticleView',
  components: {
    ArticleList
  }, // 인스턴스가 생성된 직후 요청을 보내기 위해
  created() { // created() hook 사용
    this.getArticles()
  },
  methods: { // actions 호출
    getArticles() {
      this.$store.dispatch('getArticles')
    }
  }
}
</script>
```

**요청 결과 확인**

- Vue와 Django 서버를 모두 켠 후 메인 페이지 접속
- Server에서는 200을 반환하였으나 Client Console에서는 Error를 확인
  - 데이터를 확인할 수 없는 이유?
    - **CORS policy**에 의해 **blocked** 되었기 때문

## 2. CORS

### Cross-Origin Resource Sharing

**What Happened?**

- 브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착

  - Server의 log는 **200(정상)** 반환
  - 즉 Server는 정상적으로 응답했지만 브라우저가 막은 것

- 보안상의 이유로 브라우저는 **SOP 동일 출처 정책**에 의해

  다른 출처의 리소스와 상호작용 하는 것을 제한 함

**SOP (Same - Origin Policy)**

- "동일 출처 정책"
- 불러온 문서나 스크립트가
  다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식
- 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임
- https://developer.mozilla.org/ko/docs/Web/Security/Same-origin_policy

**Origin 출처**

- **Scheme/Protocol, Host, Port를 모두 포함한 URL을** 출처라고 부름
- `http`://`localhost`:`3000`/posts/3
- 세 영역이 일치하는 경우에만 Same Origin 동일 출처로 인정

**CORS 교차 출처 리소스 공유**

- 추가 **HTTP Header**를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이

  **다른 출처의 자원에 접근할 수 있는 권한**을 부여하도록 브라우저에 알려주는 체제

  - 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 **서버에 지정**할 수 있는 방법

- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행

  - 만약 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 

    브라우저에게 **다른 출처지만 접근해도 된다는 사실을 알려야 함**

  - "교차 출처 리소스 공유 정책 CORS policy"

**CORS policy 교차 출처 리소스 공유 정책**

- 다른 출처에서 온 리소스를 공유하는 것에 대한 정책

- CORS policy에 위배되는 경우 브라우저에서 해당 응답 결과를 사용하지 않음

  - Server에서 응답을 주더라도 브라우저에서 거절

- 다른 출처의 리소스를 불러오려면 그 출처에서 **올바른 CORS header**를

  포함한 응답을 반환해야 함

- https://developer.mozilla.org/ko/docs/Web/HTTP/CORS

### How to set CORS

- CORS 표준에 의해 추가된 HTTP Response Header를 통해 이를 통제 가능

- HTTP Response Header 예시

  - **Access-Control-Allow-Origin** / Access-Control-Allow-Credentials /

    Access-Control-Allow-Headers / Access-Control-Allow-Methods

- Access-Control-Allow-Origin

  - 단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 허용

**django-cors-headers library 사용하기**

- django-cors-headers github에서 내용 확인

  - https://github.com/adamchainz/django-cors-headers

- **응답에 CORS header를 추가**해주는 라이브러리

- 다른 출처에서 Django 애플리케이션에 대한 브라우저 내 요청을 허용함

```bash
$ pip install django-cors-headers
# 라이브러리 설치 및 requirements.txt 업데이트
$ pip freeze >requirements.txt
```

  ```python
  # my_api/settings.py
  INSTALLED_APPS = [
    'corsheaders',  # CORS policy
  ]
  MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # CorsMiddleware 는 가능한 CommonMiddleware 보다 먼저 정의 되어야 함
    'django.middleware.common.CommonMiddleware',
  ]
  
  # 교차 출처 자원 공유를 허용할 Domain 등록
  CORS_ALLOWED_ORIGINS = [ # 특정 Origin만 선택적으로 허용
    'http://localhost:8080',
  ]
  # 만약 모든 Origin 허용하고자 한다면
  CORS_ALLOWED_ALL_ORIGINS = True
  ```

- console 창에 정상적으로 출력되는 데이터 확인
- 응답에 Access-Conrol-Allow-Origin 헤더가 있는 것을 확인

### Vue with DRF (feat.CORS)

#### Article Read

- 응답 받은 데이터 구조 확인
  - **data Array**에 각 게시글 객체
  - 각 게시글 객체는 다음으로 구성
    1. id
    2. title
    3. content

```js
// store/index.js
import axios from 'axios'
// 요청 보낼 API server 도메인 변수에 담기
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: { // 기존 articles 데이터 삭제
    articles: []
  },
  mutations: { // Mutations 정의
    GET_ARTICLES(state, articles) {
      state.articles = articles
    }, // 응답 받아온 데이터를 state에 저장
  },
  actions: { // 메소드 정의
    getArticles(context) { 
      axios({
        method: 'get', // 요청 보낼 경로 확인 필수
        url: `${API_URL}/api/v1/articles/`,
      }) // 성공 시 .then
        .then((res) =>
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        ) // 실패 시 .catch
        .catch((err) => console.log(err))
    },
  },
})
```

#### Article Create

```vue
<!-- views/CreateView.vue -->
<template>
  <div>
    <h1>게시글 작성</h1> <!--.prevent를 활용해 form의 기본 이벤트 동작 막기-->
    <form @submit.prevent="createArticle"><!--게시글 생성을 위한 form을 제공-->
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea
        id="content" cols="30" rows="10"
        v-model.trim="content" 
      > <!--v-model.trim을 활용해 사용자 입력 데이터에서 공백 제거-->
      </textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return // title, content가 비었다면 alert를 통해 경고창을 띄우고
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      } // AJAX 요청을 보내지 않도록 return 시켜 함수를 종료
      axios({ // axios를 사용해 server에 게시글 생성 요청
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: { title, content },
      })
        .then((res) => {
          console.log(res)
      })
      .catch((err) => console.log(err))
    } // actions를 사용하지 않나요?
  } // state를 변화 시키는 것이 아닌 DB에 게시글 생성 후,
} // ArticleView로 이동할 것이므로 methods에서 직접 처리
</script>
```

```js
// router/index.js
import CreateView from '@/views/CreateView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },
]
```

```vue
<!-- views/ArticleView.vue -->
<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">
      [CREATE] <!--router-link를 통해 CreateView로 이동-->
    </router-link>
    <hr>
    <ArticleList/>
  </div>
</template>

<script>
export default {
  name: 'ArticleView',
  components: {
    ArticleList
  }, // 인스턴스가 생성된 직후 요청을 보내기 위해
  created() { // created() hook 사용
    this.getArticles()
  },
  methods: { // actions 호출
    getArticles() {
      this.$store.dispatch('getArticles')
    }
  }
}
</script>
```

- 게시글 작성 요청 결과 확인
  - 정상 작동 확인

```vue
<!-- views/CreateView.vue -->
<template>
  <div>
    <h1>게시글 작성</h1> <!--.prevent를 활용해 form의 기본 이벤트 동작 막기-->
    <form @submit.prevent="createArticle"><!--게시글 생성을 위한 form을 제공-->
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea
        id="content" cols="30" rows="10"
        v-model.trim="content" 
      > <!--v-model.trim을 활용해 사용자 입력 데이터에서 공백 제거-->
      </textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return // title, content가 비었다면 alert를 통해 경고창을 띄우고
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      } // AJAX 요청을 보내지 않도록 return 시켜 함수를 종료
      axios({ // axios를 사용해 server에 게시글 생성 요청
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: { title, content },
      }) // 응답 확인을 위해 정의한 인자 res 제거
        .then(() => {
          this.$router.push({name: 'ArticleView'})
      }) // 게시글 생성 완료 후, ArticleView로 이동
      .catch((err) => console.log(err))
    } // actions를 사용하지 않나요?
  } // state를 변화 시키는 것이 아닌 DB에 게시글 생성 후,
} // ArticleView로 이동할 것이므로 methods에서 직접 처리
</script>
```

- 게시글 작성 요청 결과 재확인
  - 게시글 생성 후,  ArticleView로 이동
  - 새로 생성된 게시글 확인 가능
- 어떻게 router로 이동만 했는데 보일까?
  - ArticleView가 create될 때 마다 server에 게시글 전체 데이터를 요청하고 있기 때문

**[참고] 지금의 요청 방식은 효율적인가?**

- 비효율적인 부분이 존재

  - 전체 게시글 정보를 요청해야 새로 생성된 게시글을 확인할 수 있음

  - 만약 vuex state를 통해 전체 게시글을 정보를 관리하도록 구성한다면

    내가 새롭게 생성한 게시글은 확인할 수 있겠지만

  - 나 이외의 유저들이 새롭게 생성한 게시글은 언제 불러 와야 할까

  - 무엇을 기준으로 새로운 데이터가 생겼다는 것을 확인할 수 있을까

- 내가 구성하는 서비스에 따라 데이터 관리 방식을 고려해 보아야 함

#### Article Detail

```vue
<!--views/DetailView.vue-->
<template>
  <div> <!--게시글 상세 정보를 표현할 컴포넌트-->
    <h1>Detail</h1>
  </div>
</template>
<!--AJAX 요청으로 응답 받아올 article의 상세 정보들을 표현-->
<script>
export default {
  name: 'DetailView',
}
</script>
```

```js
// router/index.js
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },
  {// id를 동적 인자로 입력 받아 특정 게시글에 대한 요청
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },
]
```

```vue
<!-- components/ArticleListItem.vue -->
<template>
  <div><!--router-link를 통해 특정 게시글의 id 값을 동적 인자로 전달-->
    <router-link
      :to="{
        name: 'DetailView',
        params: { id: article.id }
      }"
    ><!-- 게시글 상세 정보를 Server에 요청 -->
      [DETAIL]
    </router-link>
  </div>
</template>
```

```vue
<!--views/DetailView.vue-->
<template>
  <div> <!--게시글 상세 정보를 표현할 컴포넌트-->
    <h1>Detail</h1>
  </div>
</template>
<!--AJAX 요청으로 응답 받아올 article의 상세 정보들을 표현-->

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',//this.$route.params를 활용해 컴포넌트가 create될 때
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
      }) // 넘겨받은 id로 상세 정보 AJAX 요청
      .then((res) => {
        console.log(res)
      })
      .catch((err) => console.log(err))
    }
  }
}
</script>
```

- 게시글 상세 정보 요청 결과 확인
  - 정상 작동 확인
  - 넘겨 받은 데이터 구조 확인 후, 적절하게 화면 구성

```vue
<!--views/DetailView.vue-->
<template>
  <div> <!--게시글 상세 정보를 표현할 컴포넌트-->
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
  </div><!--data에 담기까지 시간이 걸리므로 optional chaining을 활용-->
</template>
<!--AJAX 요청으로 응답 받아올 article의 상세 정보들을 표현-->

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  data() {
    return {
      article:null
    }
  },
  name: 'DetailView',
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',//this.$route.params를 활용해 컴포넌트가 create될 때
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
      }) // 넘겨받은 id로 상세 정보 AJAX 요청
      .then((res) => { this.article = res.data }}
      }) // 응답 받은 정보를 data에 저장
      .catch((err) => console.log(err))
    }
  }
}
</script>
```

- 최종 결과 확인

## 3. DRF Auth System

### Authentication & Authorization

**Authentication 인증, 입증**

- 자신이라고 주장하는 사용자가 누구인지 확인하는 행위

- 모든 보안 프로세스의 첫 번째 단계 (가장 기본 요소)

- 즉, 내가 누구인지를 확인하는 과정

- 401 Unauthorized

  - 비록 HTTP 표준에서는 "unauthorized 미승인"을 명확히 하고 있지만,

    의미상 이 응답은 "unauthenticated 비인증"을 의미

- 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정 (절차)

- 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함

  - 사용자는 조직에 대한 액세스 권한을 부여 받기 전에 먼저

    자신의 ID가 진짜인지 먼저 확인해야 함

- 서류의 등급, 웹 페이지에서 글을 조회 & 삭제 & 수정할 수 있는 방법, 제한 구역

  - 인증이 되었어도 모든 권한을 부여 받는 것은 아님

- 403 Forbidden

  - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음

**Authentication and Authorization work together**

- 회원가입 후, 로그인 시 서비스를 이용할 수 있는 권한 생성

  - 인증 이후에 권한이 따라오는 경우가 많음

- 단, 모든 인증을 거쳐도 권한이 동일하게 부여되는 것은 아님

  - Django에서 로그인을 했더라도

    다른 사람의 글까지 수정 / 삭제가 가능하진 않음

- 세션, 토큰, 제 3자를 활용하는 등의 다양한 인증 방식이 존재

### How to authentication determined

**인증 여부 확인 방법**

- [DRF 공식문서에서 제안하는 인증 절차 방법](https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme)
- **Setting the authentication scheme**
- The default authentication schemes may be set globally, using the `DEFAULT_AUTHENTICATION_CLASSES` setting. For example.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ] # BasicAuthentication
}   # SessionAuthentication 는 뭘까?
```

- settings.py에 작성해야 할 설정

  - "기본적인 인증 절차를 어떠한 방식으로 둘 것이냐"를 설정하는 것
  - 예시의 2가지 방법 외에도 각 framework마다 다양한 인증 방식이 있음

- 사용할 방법은 DRF가 기본으로 제공해주는 인증 방식 중 하나인 **`TokenAuthentication`**

- 모든 상황에 대한 인증 방식을 정의하는 것이므로,

  각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식이 필요

- view 함수마다 (각 요청마다) 다른 인증 방식을 설정하고자 한다면 decorator 활용

```python
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        "user": str(request.user),  # `django.contrib.auth.User` instance.
        "auth": str(request.auth),  # None
    }
    return Response(content)
```

- [참고] permission_classes
  - 권한 관련 설정
  - 권한 역시 특정 view 함수마다 다른 접근 권한을 요구 할 수 있음

**다양한 인증 방식**

- BasicAuthentication
  - 가장 기본적인 수준의 인증 방식
  - 테스트에 적합
- SessionAuthentication
  - Django에서 사용하였던 session 기반의 인증 시스템
  - DRF와 Django의 session 인증 방식은 보안적 측면을 구성하는 방법에 차이가 있음
- RemoteUserAuthentication
  - Django의 Remote user 방식을 사용할 때 활용하는 인증 방식
- TokenAuthentication
  - 매우 간단하게 구현할 수 있음
  - 기본적인 보안 기능 제공
  - 다양한 외부 패키지가 있음
- (중요) settings.py 에서 `DEFAULT_AUTHENTICATION_CLASSES`를 정의
  - **TokenAuthentication** 인증 방식을 사용할 것임을 명시

**TokenAuthentication 사용 방법**

```python
INSTALLED_APPS = [
    ...# INSTALLED_APPS에 `rest_framework.authtoken` 등록
    'rest_framework.authtoken'
]
```

```python
from rest_framework.authtoken.models import Token
# 각 User 마다 고유 Token 생성
token = Token.objects.create(user=...)
print(token.key)
```

- 생성한 Token을 각 User에게 발급
  - User는 발급 받은 Token을 요청과 함께 전송
  - Token을 통해 User  인증 및 권한 확인

```python
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


def some_view_func(request):  # Token 발급 방법
    token = Token.objects.create(user=...)
    return Response({"token": token.key})
```

- User는 발급 받은 Token을 headers에 담아 요청과 함께 전송
  - 단, 반드시 `Token` 문자열 함께 삽입
    - 삽입해야 할 문자열은 각  인증 방식마다 다름 (ex. Bearer, Auth, JWT 등)
  - **주의)** Token 문자열과 발급받은 실제 token 사이를 `' '(공백)`으로 구분
- Authorization HTTP headers 작성 방법

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**토큰 생성 및 관리 문제점** 

- 기본 제공 방식에서 고려하여야 할 사항들
  1. Token 생성 시점
  2. 생성한 Token 관리 방법
  3. User와 관련된 각종 기능 관리 방법
     - 회원가입
     - 로그인
     - 회원 정보 수정
     - 비밀 번호 변경 등...

### dj-rest-auth

- 회원가입, 인증(소셜미디어 인증 포함), 비밀번호 재설정, 사용자 세부 정보 검색,

  회원 정보 수정 등을 위한 REST API end point 제공

- **주의) django-rest-auth / dj-rest-auth**
  This library provides a set of REST API endpoints for registration, authentication (including social media authentication), password reset, retrieve and update user details, etc. By having these API endpoints, your client apps such as AngularJS, iOS, Android, and others can communicate to your Django backend site independently via REST APIs for user management.

  There are currently two forks of this project.

  - Django-rest-auth is the original project, but is not currently receiving updates.

  - **Dj-rest-auth** is a newer fork of the project.

- https://github.com/iMerica/dj-rest-auth

**dj-rest-auth 사용 방법**

```bash
$ pip install dj-rest-auth # 패키지 설치
```

```python
INSTALLED_APPS = (
    ..., # App 등록
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'dj_rest_auth'
)
```

```python
urlpatterns = [  # url 등록
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
```

**시작하기 전에**

```python
# my_api/settings.py
INSTALLED_APPS = [
    # Django Apps
    'accounts',
    'articles'',
    ...
]  # auth.User로 설정된 DB(db.sqlite3) 제거
# auth.User를 accounts.User로 변경 필요
AUTH_USER_MODEL = 'accounts.User'
```

**dj-rest-auth 사용하기**

```bash
$ pip install dj-rest-auth # dj-rest-auth 설치
```

```python
# my_api/settings.py
INSTALLED_APPS = [
    ...
    # Auth
    'rest_framework.authtoken',
    'dj_rest_auth',
]
```

```bash
$ pip manage.py migrate
```

```python
# my_api/urls.py
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("dj_rest_auth.urls")),
]
```

- 결과 확인

  - `/accounts/`로 이동
  - 회원 가입 기능 없음

- Github 재확인

  - 상세 옵션은 공식 문서를 참고하도록 안내

    **Documentation**
    
    View the full documentation here: https://dj-rest-auth.readthedocs.io/en/latest/index.html

- 공식 문서로 이동

  - [Registration (optional)](https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional) 확인

**Registration**

- Registration 기능을 사용하기 위해 추가 기능 등록 및 설치 필요

  - dj-rest-auth는 소셜 회원가입을 지원한다.
  - dj-rest-auth의 회원가입 기능을 사용하기 위해서는 `django-allauth` 필요

  1. If you want to enable standard registration process you will need to install `django-allauth` by using `pip install 'dj-rest-auth[with_social]'`.
  2. Add `django.contrib.sites`, `allauth`, `allauth.account`, `allauth.socialaccount` and `dj_rest_auth.registration` apps to INSTALLED_APPS in your django settings.py:
  3. Add `SITE_ID = 1` to your django settings.py

```bash
# django-allauth 설치
$ pip install 'dj-rest-auth[with_social]' # 반드시 ''도 함께 입력
```

```python
# my_api/settings.py
INSTALLED_APPS = [
    ...
    # registration
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]
# App 등록 및 SITE_ID 설정
SITE_ID = 1
```

- [참고] SITE_ID

  - Django는 하나의 컨텐츠를 기반으로 여러

    도메인에 컨텐츠를 게시 가능하도록 설계됨

  - 다수의 도메인이 하나의 데이터베이스에 등록

  - 현재 프로젝트가 첫번째 사이트임을 나타냄

```python
# my_api/urls.py
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("dj_rest_auth.urls")),
    path("accounts/signup/", include("dj_rest_auth.registration.urls")),
]
```

```bash
# allauth 추가에 대한 migrate
$ python manage.py migrate
```

- `/accounts/signup` 페이지 확인
- Get method는 접근 불가
- 회원가입 POST 요청 양식 제공
  - email은 생략 가능

**Sign up & Login**

- 회원 가입 후 결과 확인
  - 요청에 대한 응답으로 **Token 발급**
- 로그인 시에도 동일한 토큰 발급
  - 정상적인 로그인 가능
- 발급 받은 토큰은 **테스트를 위해 기록**

**Password change**

- `/accounts/password/change/` 기능 확인
  - 로그인 되어 있거나, 인증이 필요한 기능
  - DRF 자체 제공 HTML form에서는 토큰을 입력할 수 있는 공간이 없음
  - Postman 에서 진행

```python
{  # [참고] Raw data에서 직접 headers 추가 가능
    "headers": {"Authorization" : "Token token"},
    "new_password1": "new password",
    "new_password2": "newpassword"
}
```

- Postman으로 양식에 맞춰 POST 요청
  - body/form-data에 값 입력
- headers에 Token 입력
  - `Authorization: Token { your token }` 형식에 맞춰 입력
- 실패 이유는?
  - **인증 방법이 입증되지 않음**

```python
# my_api/settings.py
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

- 최종 결과 확인
  - 정상적으로 비밀번호 변경 완료

### Permission setting

- 권한 설정 방법 확인
  - DRF 공식 문서 > API Guide > Permissions 확인
- https://www.django-rest-framework.org/api-guide/permissions/

- 권한 세부 설정
  1. 모든 요청에 대해 인증을 요구하는 설정
  2. 모든 요청에 대해 인증이 없어도 허용하는 설정
- 설정 위치 == 인증 방법을 설정한 곳과 동일
  - 우선 모든 요청에 대해 허용 설정

```python
'DEFAULT_PERMISSION_CLASSES': [
   'rest_framework.permissions.AllowAny',
]
```

```python
# my_api/settings.py
REST_FRAMEWORK = {
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

**Article List Read**

```python
# articles/views.py
from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Article

# 게시글 조회 및 생성 요청 시 인증된 경우만 허용하도록 권한 부여
@api_view(["GET", "POST"])  # decorator를 활용
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == "GET":
        articles = get_list_or_404(Article)
        ...
        return Response(serializer.data)
    elif request.method == "POST":
        ...
```

- `/articles/` 조회 요청 확인
- 게시글 조회 시 로그인 필요

**Article Create**

- `/articles` 생성 요청 확인
  - Postman으로 진행

- 결과 확인
  - 게시글 생성 성공

**Article Detail Read**

- `/articles/1/` 상세 조회 요청 확인
  - headers에 token을 담지 않아도 조회 가능
  - 인증 필요 권한 설정을 따로 하지 않았기 때문

**정리**

1. 인증 방법 설정
   - DEFAULT_AUTHENTICATION_CLASSES
2. 권한 설정하기
   - DEFAULT_PERMISSION_CLASSES
3. 인증 방법, 권한 세부 설정도 가능
   - @authentication_classes
   - @permission_classes
4. 인증 방법은 다양한 방법이 있으므로 내 서비스에 적합한 방식을 선택

## 4. DRF Auth with Vue

**Vue Server 요청 정상 작동 여부 확인**

- 정상 작동하던 게시글 전체 조회 요청이 작동하지 않음
  - 401 status code 확인
  - 인증되지 않은 사용자이므로 조회 요청이 불가능해진 것

### SignUp Request

```vue
<!-- views/SignUpView.vue -->
<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">
			<!-- Server에서 정의한 field명 확인 -->
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1">
			<!-- Server에서 정의한 field명 확인 -->
      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
			<!-- Server에서 정의한 field명 확인 -->
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>
```

```js
// router/index.js
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },
  {// id를 동적 인자로 입력 받아 특정 게시글에 대한 요청
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
]
```

```vue
<!-- src/App.vue -->
<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'ArticleView' }">Articles</router-link> |
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link>
    </nav>
    <router-view/>
  </div>
</template>
```

- `views/SignupView.vue` 결과 확인

**SignUp Request**

- 회원가입을 완료 시 응답 받을 정보 Token을 store에서 관리할 수 있도록

  actions를 활용하여 요청 후, state에 저장할 로직 작성

  - 회원가입이나 로그인 후 얻을 수 있는 Token은 server를 구성 방식에 따라

    매 요청마다 요구 할 수 있으므로, 다양한 컴포넌트에서 쉽게 접근 할 수 있도록

    중앙 상태 저장소인 vuex에서 관리

```vue
<!-- views/SignUpView.vue -->
<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username" />
      <!-- Server에서 정의한 field명 확인 -->
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1" />
      <!-- Server에서 정의한 field명 확인 -->
      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2" />
      <!-- Server에서 정의한 field명 확인 -->
      <input type="submit" value="SignUp" />
    </form>
  </div>
</template>

<script>
export default {
  ...
  methods: {
    signUp() { 
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      // 사용자 입력 값을 하나의 객체 payload에 담아 전달
      const payload = {
        username,
        password1,
        password2,
      }
      this.$store.dispatch('signUp', payload)
    },
  },
}
</script>
```

```js
// store/index.js
import axios from 'axios'
import Vuex from 'vuex'
// 요청 보낼 API server 도메인 변수에 담기
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: { // 기존 articles 데이터 삭제
    articles: [],
    token: null, // token을 저장할 위치 확인
  },
  mutations: { // Mutations 정의
    GET_ARTICLES (state, articles) {
      state.articles = articles
    }, // 응답 받아온 데이터를 state에 저장
    // auth
    SIGN_UP (state, token) {
      state.token = token
    }, // mutations를 통해 state 변화
  },
  actions: { // 메소드 정의
    getArticles (context) {
      axios({
        method: 'get', // 요청 보낼 경로 확인 필수
        url: `${API_URL}/api/v1/articles/`,
      }) // 성공 시 .then
        .then((res) =>
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        ) // 실패 시 .catch
        .catch((err) => console.log(err))
    },
    signUp (context, payload) {
      const username = payload.username,
      const password1 = payload.password1,
      const password2 = payload.password2
      // payload가 가진 값을 각각 할당
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          context.commit('SIGN_UP', res.data.key)
        })
        .catch((err) => console.log(err))
    },
  },
})
```

- 요청 결과 확인
  - 정상 응답 확인

**토큰 관리**

- 게시물 전체 조회와 달리, 인증 요청의 응답으로 받은 Token은 매번 요청하기 힘듦
  - 비밀번호를 항상 보관하고 있을 수는 없음
  - localStorage에 token 저장을 위해 [vuex-persistedstate](https://github.com/robinvdvleuten/vuex-persistedstate) 활용

```bash
$ npm install vuex-persistedstate # 설치
```

```js
// store/index.js
import axios from 'axios'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
// 요청 보낼 API server 도메인 변수에 담기
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: { // 기존 articles 데이터 삭제
    articles: [],
    token: null, // token을 저장할 위치 확인
  },
  mutations: { // Mutations 정의
    GET_ARTICLES (state, articles) {
      state.articles = articles
    }, // 응답 받아온 데이터를 state에 저장
    // auth
    SIGN_UP (state, token) {
      state.token = token
    }, // mutations를 통해 state 변화
  },
  actions: { // 메소드 정의
    getArticles (context) {
      axios({
        method: 'get', // 요청 보낼 경로 확인 필수
        url: `${API_URL}/api/v1/articles/`,
      }) // 성공 시 .then
        .then((res) =>
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        ) // 실패 시 .catch
        .catch((err) => console.log(err))
    },
    signUp (context, payload) {
      const username = payload.username,
      const password1 = payload.password1,
      const password2 = payload.password2
      // payload가 가진 값을 각각 할당
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          context.commit('SIGN_UP', res.data.key)
        })
        .catch((err) => console.log(err))
    },
  },
})
```

- 결과 확인
  - localStorage에 저장

**[참고] User 인증 정보를 localStorage에 저장해도 되는가?** 

- 안전한 방법으로 볼 수는 없음
- 따라서, vuex-persistedstate는 아래의 2가지 방법을 제공
  1. 쿠키를 사용하여 관리
  2. 로컬 저장소를 난독화하여 관리
- 편의를 위해 localStorage를 사용할 예정

### LogIn Request

```vue
<!-- views/LoginView.vue -->
<template>
  <di>
    <h1>LogIn Page</h1> <!-- 회원가입 로직과 동일 -->
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">
      <!-- Server에서 정의한 field명 확인 -->
      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password">
      <!-- Server에서 정의한 field명 확인 -->
      <input type="submit" value="logIn">
    </form>
  </div>
</template>
```

```js
// router/index.js
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },
  {// id를 동적 인자로 입력 받아 특정 게시글에 대한 요청
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
]
```

```vue
<!-- src/App.vue -->
<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'ArticleView' }">Articles</router-link> |
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> |
      <router-link :to="{ name: 'LogInView' }">LogInPage</router-link>
    </nav> <!-- 파이프 라인 등을 활용하여 링크 간 공간 확보 -->
    <router-view/>
  </div>
</template>
```

- `views/LoginView.vue` 결과 확인

**Login Request**

- signUp과 다른 점은 password1 password2가 password로 바뀐 것 뿐
- 요청을 보내고 응답을 받은 Token을 state에 저장하는 것까지도 동일
  - mutations가 처리 해야 하는 업무가 동일
  - SIGN_UP mutations를 `SAVE_TOKEN mutations`로 대체 가능

```vue
<!-- views/LoginView.vue -->
<template>
  <di>
    <h1>LogIn Page</h1> <!-- 회원가입 로직과 동일 -->
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">
      <!-- Server에서 정의한 field명 확인 -->
      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password">
      <!-- Server에서 정의한 field명 확인 -->
      <input type="submit" value="logIn">
    </form>
  </div>
</template>
<script>
export default {
  ...
  methods: {
    logIn () {
      const username = this.username
      const password = this.password
      // 사용자 입력 값을 하나의 객체 payload에 담아 전달
      const payload = {
        username, password
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>
```

```js
// store/index.js
import axios from 'axios'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
// 요청 보낼 API server 도메인 변수에 담기
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: { // 기존 articles 데이터 삭제
    articles: [],
    token: null, // token을 저장할 위치 확인
  },
  mutations: { // Mutations 정의
    GET_ARTICLES (state, articles) {
      state.articles = articles
    }, // 응답 받아온 데이터를 state에 저장
    // auth
    SIGN_UP (state, token) {
      state.token = token
    }, // mutations를 통해 state 변화
    // sign up && login
    SAVE_TOKEN (state, token) {
      state.token = token
    }
  },
  actions: { // 메소드 정의
    getArticles (context) {
      axios({
        method: 'get', // 요청 보낼 경로 확인 필수
        url: `${API_URL}/api/v1/articles/`,
      }) // 성공 시 .then
        .then((res) =>
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        ) // 실패 시 .catch
        .catch((err) => console.log(err))
    },
    // auth
    signUp (context, payload) {
      const username = payload.username,
      const password1 = payload.password1,
      const password2 = payload.password2
      // payload가 가진 값을 각각 할당
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          // context.commit('SIGN_UP', res.data.key)
          // 확인) signUp이 호출할 mutations도 함께 변경
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => console.log(err))
    },
    logIn (context, payload) { // payload가 가진 값을 각각 할당
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          context.commit('SAVE_TOKEN', res.data.key)
        }) // 이 때, mutations는 SAVE_TOKEN 호출 확인
        .catch((err) => console.log(err))
    },
  },
})
```

- 최종 결과 확인
  - 정확한 결과 확인을 위해 기존 토큰 삭제 추천
  - 정상 작동 확인

### IsAuthenticated in Vue

- 회원가입, 로그인 요청에 대한 처리 후

  state에 저장된 Token을 직접 확인하기 전까지 인증 여부 확인 불가

- 인증 되지 않았을 시 게시글 정보를 확인할 수 없으나 이유를 알 수 없음

  - 로그인 여부를 확인 할 수 있는 수단이 없음

```js
// store/index.js
import axios from 'axios'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
// 요청 보낼 API server 도메인 변수에 담기
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: { // 기존 articles 데이터 삭제
    articles: [],
    token: null, // token을 저장할 위치 확인
  },
  getters: { // 로그인 여부 판별 코드 확인
    isLogin (state) {
      return state.token ? true : false
    } // Toke이 있으면 true 없으면 false 반환
  },
  mutations: { // Mutations 정의
    GET_ARTICLES (state, articles) {
      state.articles = articles
    }, // 응답 받아온 데이터를 state에 저장
    // auth
    SIGN_UP (state, token) {
      state.token = token
    }, // mutations를 통해 state 변화
    // sign up && login
    SAVE_TOKEN (state, token) {
      state.token = token
    }
  },
  actions: { // 메소드 정의
    getArticles (context) {
      axios({
        method: 'get', // 요청 보낼 경로 확인 필수
        url: `${API_URL}/api/v1/articles/`,
      }) // 성공 시 .then
        .then((res) =>
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        ) // 실패 시 .catch
        .catch((err) => console.log(err))
    },
    // auth
    signUp (context, payload) {
      const username = payload.username,
      const password1 = payload.password1,
      const password2 = payload.password2
      // payload가 가진 값을 각각 할당
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          // context.commit('SIGN_UP', res.data.key)
          // 확인) signUp이 호출할 mutations도 함께 변경
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => console.log(err))
    },
    logIn (context, payload) { // payload가 가진 값을 각각 할당
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          context.commit('SAVE_TOKEN', res.data.key)
        }) // 이 때, mutations는 SAVE_TOKEN 호출 확인
        .catch((err) => console.log(err))
    },
  },
})
```

```vue
<!-- views/ArticleView.vue -->
<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">
      [CREATE] <!--router-link를 통해 CreateView로 이동-->
    </router-link>
    <hr>
    <ArticleList/>
  </div>
</template>

<script>
export default {
  name: 'ArticleView',
  components: {
    ArticleList
  }, // 인스턴스가 생성된 직후 요청을 보내기 위해
  created() { // created() hook 사용
    this.getArticles()
  },
  computed: {
    isLogin () {
      return this.$store.getters.isLogin
    }
  },
  methods: { // actions 호출
    getArticles () { // isLogin 정보를 토대로
      if (this.isLogin) { // 게시글 정보를 요청할 것인지,
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView' })
      } // LoginView로 이동시킬 것인지 결정
    }
  }
}
</script>
```

```js
// store/index.js 에서는 $router에 접근할 수 없음
import router from '@/router' // router를 import 해야 함
import axios from 'axios'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
// 요청 보낼 API server 도메인 변수에 담기
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: { // 기존 articles 데이터 삭제
    articles: [],
    token: null, // token을 저장할 위치 확인
  },
  getters: { // 로그인 여부 판별 코드 확인
    isLogin (state) {
      return state.token ? true : false
    } // Toke이 있으면 true 없으면 false 반환
  },
  mutations: { // Mutations 정의
    GET_ARTICLES (state, articles) {
      state.articles = articles
    }, // 응답 받아온 데이터를 state에 저장
    // auth
    SIGN_UP (state, token) {
      state.token = token
    }, // mutations를 통해 state 변화
    // sign up && login
    SAVE_TOKEN (state, token) {
      state.token = token
      router.push({ name: 'ArticleView' })
    } // 단, store/index.js에서는 $router에 접근할 수 없음
  },    // router를 import 해야 함
  actions: { // 메소드 정의
    getArticles (context) {
      axios({
        method: 'get', // 요청 보낼 경로 확인 필수
        url: `${API_URL}/api/v1/articles/`,
      }) // 성공 시 .then
        .then((res) =>
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        ) // 실패 시 .catch
        .catch((err) => console.log(err))
    },
    // auth
    signUp (context, payload) {
      const username = payload.username,
      const password1 = payload.password1,
      const password2 = payload.password2
      // payload가 가진 값을 각각 할당
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          // context.commit('SIGN_UP', res.data.key)
          // 확인) signUp이 호출할 mutations도 함께 변경
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => console.log(err))
    },
    logIn (context, payload) { // payload가 가진 값을 각각 할당
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          context.commit('SAVE_TOKEN', res.data.key)
        }) // 이 때, mutations는 SAVE_TOKEN 호출 확인
        .catch((err) => console.log(err))
    },
  },
})
```

- 결과 확인

1. localStorage에서 token 삭제 후, 새로 고침
2. Articles 링크 클릭 시 LoginPage로 이동
   - 인증 되지 않은 사용자를 LogInPage로 이동 시키는데 성공

**로그인 후, Articles에서는**

- 인증은 받았지만 게시글 조회 시 인증 정보를 담아 보내고 있지 않음
- 원인
  - 로그인은 했으나 Django에서는 로그인 한 것으로 인식하지 못함
  - 발급 받은 token을 요청으로 보내지 않았기 때문

### Request with Token

- 인증 여부를 확인하기 위한 Token 이 준비되었으니,
- headers HTTP에 Token을 담아 요청을 보내면 된다.

**Article List Read with Token**

```js
// store/index.js 에서는 $router에 접근할 수 없음
import router from '@/router' // router를 import 해야 함
import axios from 'axios'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
// 요청 보낼 API server 도메인 변수에 담기
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: { // 기존 articles 데이터 삭제
    articles: [],
    token: null, // token을 저장할 위치 확인
  },
  getters: { // 로그인 여부 판별 코드 확인
    isLogin (state) {
      return state.token ? true : false
    } // Toke이 있으면 true 없으면 false 반환
  },
  mutations: { // Mutations 정의
    GET_ARTICLES (state, articles) {
      state.articles = articles
    }, // 응답 받아온 데이터를 state에 저장
    // auth
    SIGN_UP (state, token) {
      state.token = token
    }, // mutations를 통해 state 변화
    // sign up && login
    SAVE_TOKEN (state, token) {
      state.token = token
      router.push({ name: 'ArticleView' })
    } // 단, store/index.js에서는 $router에 접근할 수 없음
  },    // router를 import 해야 함
  actions: { // 메소드 정의
    getArticles (context) {
      axios({
        method: 'get', // 요청 보낼 경로 확인 필수
        url: `${API_URL}/api/v1/articles/`,
        headers: { // headers에 Authorizations 와 token 추가
          Authorization: `Token ${context.state.token}`
        }
      }) // 성공 시 .then
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        }) // 실패 시 .catch
        .catch((err) => { console.log(err) })
    },
    // auth
    signUp (context, payload) {
      const username = payload.username,
      const password1 = payload.password1,
      const password2 = payload.password2
      // payload가 가진 값을 각각 할당
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          // context.commit('SIGN_UP', res.data.key)
          // 확인) signUp이 호출할 mutations도 함께 변경
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => console.log(err))
    },
    logIn (context, payload) { // payload가 가진 값을 각각 할당
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      }) // AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
        .then((res) => { // state에 저장할 것
          context.commit('SAVE_TOKEN', res.data.key)
        }) // 이 때, mutations는 SAVE_TOKEN 호출 확인
        .catch((err) => console.log(err))
    },
  },
})
```

- 결과 확인

```python
# articles/views.py
from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleListSerializer


# 게시글 조회 및 생성 요청 시 인증된 경우만 허용하도록 권한 부여
@api_view(["GET", "POST"])  # decorator를 활용
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == "GET":
        # 404 발생 원인은 view 함수가 그렇게 처리하기로 하였기 때문
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
    ...
```

- 게시글 생성 기능 완성 후, 다시 결과 확인

**Article Create with Token**

```vue
<!-- views/CreateView.vue -->
<template>
  <div>
    <h1>게시글 작성</h1>
    <!--.prevent를 활용해 form의 기본 이벤트 동작 막기-->
    <form @submit.prevent="createArticle">
      <!--게시글 생성을 위한 form을 제공-->
      <label for="title">제목 : </label>
      <input
        type="text"
        id="title"
        v-model.trim="title"
      ><br>
      <label for="content">내용 : </label>
      <textarea
        id="content"
        cols="30"
        rows="10"
        v-model.trim="content"
      > <!--v-model.trim을 활용해 사용자 입력 데이터에서 공백 제거-->
      </textarea><br>
      <input
        type="submit"
        id="submit"
      >
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  methods: {
    createArticle () {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return // title, content가 비었다면 alert를 통해 경고창을 띄우고
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      } // AJAX 요청을 보내지 않도록 return 시켜 함수를 종료
      axios({ // axios를 사용해 server에 게시글 생성 요청
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: { title, content },
        headers: { // headers에 Authorization 과 token 추가
          Authorization: `Token ${this.$store.state.token}`
        }
      }) // 응답 확인을 위해 정의한 인자 res 제거
        .then(() => {
          this.$router.push({ name: 'ArticleView' })
        }) // 게시글 생성 완료 후, ArticleView로 이동
        .catch((err) => console.log(err))
    } // actions를 사용하지 않나요?
  } // state를 변화 시키는 것이 아닌 DB에 게시글 생성 후,
} // ArticleView로 이동할 것이므로 methods에서 직접 처리
</script>
```

- 결과 확인
  - 정상 작동 확인

**Create Article with User**

```python
# articles/models.py
from django.conf import settings
from django.db import models


# Create your models here.
class Article(models.Model): # 게시글을 작성시 User 정보를 포함하여 작성하도록 수정
    user = models.ForeignKey(  # User정보를 Vue에서도 확인 가능하도록 정보 제공
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
```

```bash
$ python manage.py makemigrations
# Please select a fix:
 ...
Select an option: 1
# 기존 게시글에 대한 User 정보 default 값 설정
Please enter the default value now, as valid Python
...
Type 'exit' to exit this prompt
>>> 1

$ python manage.py migrate # 
```

```python
# articles/serializers.py
from rest_framework import serializers

from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    # username을 확인 할 수 있도록 username field 정의 필요
    # comment_count field 정의 방법 참고

    class Meta:
        model = Article
        fields = ("id", "title", "content", "user", "username")

    # ArticleListSerializer에서 user는 사용자가 작성 하지 않음 -> fields에 추가


class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    # username을 확인 할 수 있도록 username field 정의 필요
    # comment_count field 정의 방법 참고

    class Meta:
        model = Article
        fields = "__all__"  # ArticleSerializer에서 user는 읽기 전용으로 제공
        read_only_fields = ("user",)

```

```python
# articles/views.py
from django.shortcuts import get_list_or_404
from rest_framework import status
# permission Decorators
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


# 게시글 조회 및 생성 요청 시 인증된 경우만 허용하도록 권한 부여
@api_view(["GET", "POST"])  # decorator를 활용
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == "GET":
        # 404 발생 원인은 view 함수가 그렇게 처리하기로 하였기 때문
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        ...
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)  # 게시글 생성시 user 정보 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

```vue
<!-- components/ArticleListItem.vue -->
<template>
  <div> <!--article이 가지고 있을 user 정보 표현-->
    <h5>{{ article.id }}</h5>
    <p>작성자 : {{ article.username }}</p>
    <p>{{ article.title }}</p>
    <!--router-link를 통해 특정 게시글의 id 값을 동적 인자로 전달-->
    <router-link
      :to="{
        name: 'DetailView',
        params: { id: article.id }
      }"
    > <!-- 게시글 상세 정보를 Server에 요청 -->
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>
```

- 결과 확인
  - 작성자 정보 확인 가능

## 5. drf-spectacular

**swagger**

- Swagger 스웨거는 개발자가 REST 웹 서비스를 설계, 빌드, 문서화, 소비하는

  일을 도와주는 오픈 소스 소프트웨어 프레임워크

  - 즉, API를 설계하고 문서화 하는데 도움을 주는 라이브러리

 **다양한 DRF API**

- Swagger 스웨거를 생성할 수 있도록 도움을 주는 라이브러리

  - **drf-spectacular**
  - https://github.com/tfranzel/drf-spectacular

- 과거에는 다양한 라이브러리가 있었으나 OpenAPI Specification이 3.0으로

  업데이트 되며 새 버전을 지원하지 않는 라이브러리들이 있으니 사용시 유의

**drf-spectacular**

- Open API 3.0을 지원하는 DRF API OpenAPI 생성기
- 지속적인 업데이트와 관리로 최신 Django, DRF 버전 지원
- **Requirements**
  - Python >= 3.6
  - Django (2.2, 3.2, 4.0, 4.1)
  - Django REST Framework (3.10.3, 3.11, 3.12, 3.13, 3.14)

```bash
$ pip install drf-spectacular
# 설치
$ pip freeze > requirements.txt
```

```python
# my_api/settings.py
INSTALLED_APPS = [ # 등록
  'drf_seectacular',
]

REST_FRAMEWORK = {  
    ...
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
# 기본 설정
SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
```

```python
# articles/urls.py
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [  # URL 설정
    # 필수 작성
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
```

- **/api/v1/swagger/** 결과 확인
  - 정상 작동 확인

## finish

1. [Vue with DRF](#1-vue-with-DRF)
2. [CORS](#2-cors)
3. [DRF Auth System](#3-DRF-auth-system)
4. [DRF Auth with Vue](#4-DRF-auth-with-vue)
5. [drf-spectacular](#5-drf-spectacular)