# Django_Auth

## 1. The Django authentication system

Django authentication system(인증 시스템)은 **Authentication 인증**과 **Authorization 권한** 부여를 함께 제공(처리)하며, 이러한 기능이 어느 정도 결합되어 일반적으로 인증 시스템이라고 함

필수 구성은 settings.py 에 이미 포함되어 있으며 INSTALLED_APPS 에서 확인 가능

- **django.contrib.auth**

**Authentication 인증**

- 신원 확인
- 사용자가 자신이 누구인지 확인하는 것

**Authorization (권한, 허가)**

- 권한 부여
- 인증된 사용자가 수행할 수 있는 작업을 결정

**사전 설정**

- 두번째 app accounts 생성 및 등록
  - **auth와 관련한 경로나 키워드들을 Django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것을 권장**


```bash
$ python manage.py startapp accounts
```

```python
# settings.py
INSTALLED_APPS = [
    'articles',
    'accounts',
]
```

- **url 분리 및 매핑**

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    
]
```

```python
# crud/urls.py

urlpatterns = [
    path('accounts/', include('accounts.urls')),
]
```

### Substituting a custom User model

”커스텀 User 모델로 **대체하기**”

Django는 기본적인 인증 시스템과 여러 가지 필드가 포함된 User Model을 제공, 대부분의 개발 환경에서 기본 User Model을 Custom User Model로 대체함

개발자들이 작성하는 일부 프로젝트에서는 django에서 제공하는 built-in User model의 기본 인증 요구사항이 적절하지 않을 수 있음

- email을 식별 값으로 사용하는 것이 더 적합한 사이트인 경우, Django의 User Model은 기본적으로 username을 식별 값으로 사용하기 떄문에 적합하지 않음

그래서 Django는 현재 프로젝트에서 나타낼 User를 참조하는 **AUTH_USER_MODEL** 설정 값을 제공하여 default user model을 override 재정의 할 수 있도록 함

**AUTH_USER_MODEL**

프로젝트에서 User를 나타낼 때 사용하는 모델

프로젝트가 진행되는 동안 (모델을 만들고 마이그레이션 한 후) 변경할 수 없음

**프로젝트 시작 시 설정**하기 위한 것이며, 참조하는 모델은 첫 번째 마이그레이션에서 사용할 수 있어야 함

- 즉, 첫번째 마이그레이션 전에 확정 지어야 하는 값

  ```python
  # settings.py
  # 기본 값
  AUTH_USER_MODEL = 'auth.User'
  ```

**[참고] settings의 로드 구조**

settings.py는 사실 **global_settings.py**를 상속받아 재정의하는 파일임

> https://github.com/django/django/blob/main/django/conf/global_settings.py

### How to substituting a custom User model

“custom User model로 대체하기”

> https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model

**대체하기**

- AbstractUser 를 상속받는 커스텀 User 클래스 작성

- 기존 User 클래스도 AbstractUser 를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 됨

  >  https://github.com/django/django/blob/main/django/contrib/auth/models.py#405

  ```python
  # accounts/models.py
  # User 모델을 정의한다
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      pass  # 비워두게 되면 에러가 발생하므로 pass 를 작성해둠
  ```

- Django 프로젝트에서 User를 나타내는데 사용하는 모델을 방금 생성한 커스텀 User 모델로 지정

  ```python
  # settings.py
  # 이 때 accounts 는 User 클래스를 정의한 application 이름
  AUTH_USER_MODEL = 'accounts.User'
  ```

- admin.py 에 커스텀 User 모델을 등록

  - 기본 User  모델이 아니기 때문에 등록하지 않으면 admin site 에 출력되지 않음

    ```python
    # accounts/admin.py
    from django.contrib import admin
    # admin 페이지에 등록
    from django.contrib.auth.admin import UserAdmin  # 기존에 사용하는 User 관리 인터페이스
    # Admin page 에서 user 관리 page의 인터페이스를 설정. 
    from .models import User  # 새롭게 정의한 User 모델
    
    admin.site.register(User, UserAdmin)
    ```

**[참고] User 모델 상속 관계**

models.Model -> class AbstractBaseUser -> class AbstractUser -> class User

**[참고] AbstractUser**

- “관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스”

- **Abstract base classes 추상 기본 클래스**

  - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스

  - 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨

    > https://docs.python.org/3/library/abc.html

**데이터베이스 초기화**

- 프로젝트 중간일 경우, 데이터베이스 초기화 후 마이그레이션

1. migrations 파일 삭제
   - migrations 폴더 및 `__init__.py`는 삭제하지 않음
   - 번호가 붙은 파일만 삭제
2. db.sqlite3 삭제
3. migrations 진행
   - makemigrations
   - migrate

**custom User로 변경된 테이블 확인**

- 이제 auth_user 테이블이 아니라 accounts_user 테이블을 사용하게 됨

**반드시 User 모델을 대체해야 할까?**

Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분 하더라도 커스텀 User 모델을 설정하는 것을 **highly recommended 강력하게 권장**

커스텀 User 모델은 **기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문**

- 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함

## 2. HTTP Cookies

로그인과 로그아웃을 이해하기 전 반드시 알아야하는 HTTP Cookies에 대해  먼저 알아보기

### HTTP

- Hyper Text Transfer Protocol

- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)

- WWW 웹에서 이루어지는 모든 데이터 교환의 기초

- 클라이언트 - 서버 프로토콜이라고도 부름

**요청과 응답**

- **requests 요청**
  - 클라이언트(브라우저)에 의해 전송되는 메시지
- **response 응답**
  - 서버에서 응답으로 전송되는 메시지

**HTTP 특징**

1. **connectionless 비 연결 지향**
   - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음

2. **stateless 무상태**

   - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음


   - 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

**어떻게 로그인 상태를 유지할까?**

- 로그인을 하고 웹 사이트를 사용할 때 페이지를 이동해도 로그인 “상태”가 유지됨
- 서버와 클라이언트 간 지속적인 상태 유지를 위해 “**쿠키와 세션**”이 존재

### Cookie 쿠키

- HTTP 쿠키는 **상태가 있는 세션**을 만들도록 해 줌

**개념**

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각이다.

- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일

  1. 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE 의 데이터 형식으로 저장

  2. 이렇게 쿠키를 저장해 놓았다가, **동일한 서버에 재요청 시 저장된 쿠키를 함께 전송**

- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨

  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음

  - stateless 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억 시켜 주기 때문


- 즉, 웹 페이지에 접속하면 웹 페이지를 응답한 서버로부터 쿠키를 받아 브라우저에 저장하고, 클라이언트가 같은 서버에 재요청 시마다 요청과 함께 저장해 두었던 쿠키도 함께 전송
  1. The browser requests a web page
  2. The server sends the page and the cookie
  3. The browse requests another page from the same server

**쿠키 사용 목적**

1. **Session management 세션 관리**
   - **로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리**

2. Personalization 개인화
   - 사용자 선호, 테마 등의 설정

3. Tracking 트래킹
   - 사용자 행동을 기록 및 분석

**Session 세션**

- 사이트와 특정 브라우저 사이의 “state(상태)”를 유지시키는 것

- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장

  - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달

  - 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 알맞은 로직을 처리


- session id 는 세션을 구별하기 위해 필요하며, 쿠키에는 session id 만 저장

**쿠키 Lifetime 수명**

1. **Session cookie**

   - current session 현재 세션이 종료되면 삭제됨

   - 브라우저 종료와 함께 세션이 삭제됨

2. **Persistent cookies**
   - Expires 속성에 지정된 날짜 혹은 max-Age 속성에 지정된 기간이 지나면 삭제됨

**Session in Django**

- Django는 **database-backed sessions 저장 방식**를 기본 값으로 사용

  - session 정보는 Django DB의 **django_session 테이블**에 저장


  - 설정을 통해 다른 저장방식으로 변경 가능

    > https://docs.djangoproject.com/en/3.2/topics/http/sessions/


- Django는 특정 **session id**를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄

- Django는 우리가 session 메커니즘(복잡한 동작원리)에 대부분을 생각하지 않게끔 많은 도움을 줌

## 3. Authentication in Web requests

- Django가 제공하는 인증 관련 built-in forms 익히기

> https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.forms

### Login

- 로그인은 **Session을 Create**하는 과정

**AuthenticationForm**

- 로그인을 위한 built-in form

  - 로그인 하고자 하는 사용자 정보를 입력 받음

  - 기본적으로 username과 password를 받아 데이터가 유효한지 검증


- request를 첫번째 인자로 취함

> https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L174

**로그인 페이지 작성**

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]
```

```python
# accounts/views.py
from django.contrib.auth import login as auth_login  # 재귀, 충돌 방지
from django.contrib.auth.forms import AuthenticationForm  # 일반 폼
from django.shortcuts import render, redirect

def login(request):
    # 실제 로그인이 일어날 때
    # session 이 create 되어 DB에 저장
    # POST 요청일 때 로그인 동작을 처리해야 함
    if request.method == 'POST':
        # 사용자의 입력 데이터가 채워진 form 을 생성
        form = AuthenticationForm(request, data=request.POST)
        # 입력이 잘 되었는지 그리고 회원인지 확인
        if form.is_vaild():  # 유효성 검사 이후
            # 우리 회원이라면 로그인 처리(session 생성해서 DB에 저장)
            # 유저 인스턴스가 필요한데 AithenticationForm의 메소드를 이용
            # form.get_user() 의 반환값은 form에 담긴 user 인스턴스
            auth_login(request, form.get_user())  # 유저 정보
            return redirect('articles:index')
    # 로그인 입력 페이지를 띄울 때는 GET 요청
    else:  
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

```django
<!-- accounts/login.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>LOGIN</h1>  <!-- LOGIN을 Base.html에 만들기 권장 -->
  {% comment %}action 의 값이 비어있으면 현재 페이지로 요청을 보냄{% endcomment %}
  <form action="{% url 'accounts:login' %}" method="POST">
	{% csrf_token %}
    {{ form.as_p }}1
    <input type="submit">
  </form>
{% endblock content %}
```

```django
<!-- base.html -->
<body>
  <div class="container">
    <a href="{% url 'accounts:login' %}">Login</a>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
</body>
```

**login()**

- login(request, user, backend=None)

- 인증된 사용자를 로그인 시키는 로직으로 view 함수에서 사용됨

- 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 사용

- HttpRequest 객체와 User 객체가 필요

**get_user()**

- AuthenticationForm의 인스턴스 메서드

- 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

>  https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L244

### Authentication with User

**현재 로그인 되어있는 유저 정보 출력하기**

- 템플릿에서 인증 관련 데이터를 출력하는 방법

```django
<!-- base.html -->
{{ user }}
{{ user.username }}  <!-- 로그인 시만 출력 -->
```

- 어떻게 base 템플릿에서 context 데이터 없이 user 변수를 사용할 수 있는 걸까?
  - settings.py의 **context processors** 설정 값 때문


**context processors**

- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록

- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨

- 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것

- 현재 user 변수를 담당하는 프로세서는 django.contrib.auth.context_processors.auth

- 이외에 더 많은 Built-in template context processors들은 공식문서를 참고

> https://docs.djangoproject.com/en/3.2/ref/templates/api/#built-in-template-context-processors

```python
# settings.py
TEMPLATE = [
    {
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.auth.context_processors.auth',
            ],
        },
    },
]
```

**django.contrib.auth.context_processors.auth**

- 현재 로그인한 사용자를 나타내는 User 클래스의 인스턴스가 템플릿 변수 **{{ user }}** 에 저장됨
  - 클라이언트가 로그인하지 않은 경우 AnonymousUser 클래스 의 인스턴스로 생성


### Logout

- 로그아웃은 **Session을 Delete**하는 과정

**logout()**

- **logout(request)**

- HttpRequest 객체를 인자로 받고 반환 값이 없음

- 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음

- 다음 2가지 일을 처리한다.

  1. 현재 요청에 대한 session data를 DB에서 삭제

  2. 클라이언트의 쿠키에서도 sessionid를 삭제

  - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함

**로그아웃 로직 작성하기**

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

def logout(request):
    # 로그아웃은 사용자로부터 입력 받는 것이 없기에
    # GET 요청에 대한 처리는 필요없음
    if request.method == 'POST':
        # 로그아웃을 처리하는 내용
        # session 을 DB에서 삭제
        auth_logout(request)
    return redirect('articles:index')
```

```django
<!-- base.html -->
<div class="container">
  <h3>Hello, {{ user }}</h3>
  <a href="{% url 'accounts:login' %}">Login</a>
  <form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Logout">
  </form>
  <hr>
  {% block content %}
  {% endblock content %}
</div>
```

## 4. Authentication with User

User Object와 User CRUD에 대한 이해

- 회원 가입, 회원 탈퇴, 회원정보 수정, 비밀번호 변경

### 회원 가입

- 회원가입은 User를 **Create**하는 것이며 **UserCreationForm** built-in form을 사용

**UserCreationForm**

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

- 3개의 필드를 가짐
  1. username (from the user model)
  1. paassword1
  1. Password2


> https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L75

**회원 가입 페이지 작성**

```python
# accouts/urls.py
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

```python
# accounts/views.py
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm,
)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

```django
<!-- accounts/signup.html -->
{% extends 'base.html' %}

{% block content %}
<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock content %}
```

**회원가입 링크 작성**

```django
<!-- base.html -->
<div class="container">
  <h3>Hello, {{ user }}</h3>
  <a href="{% url 'accounts:login' %}">Login</a>
  <form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Logout">
  </form>
  <a href="{% url 'accounts:signup' %}">Signup</a>
  <hr>
  {% block content %}
  {% endblock content %}
</div>
```

**회원가입 진행 후 에러 페이지를 확인**

- 회원가입에 사용하는 UserCreationForm이 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문

> https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L106

```python
class UserCreationForm(forms.ModelForm):
# 실제 UserCreationForm 코드    
    class Meta:
        model = User  # 상속 받아서 오버라이딩하기
        fields = ("username",)
        field_classes ={"username": UsernameField}
```

### Custom user & Built-in auth forms

- Custom user와 기존 Built-in auth forms 간의 관계

- Custom user로 인한 Built-in auth forms 변경

**AbstractBaseUser의 모든 subclass와 호환되는 forms**

- 아래 Form 클래스는 User 모델을 대체하더라도 커스텀 하지 않아도 사용가능
  1. AuthenticationForm
  2. SetPasswordForm
  3. PasswordChangeForm
  4. AdminPasswordChangeForm

- 기존 User 모델을 참조하는 Form이 아니기 때문

**커스텀 유저 모델을 사용하려면 확장해야 하는 forms**

1. UserCreationForm
2. UserChangeForm

- 두 form 모두 **class Meta: model = User**가 등록된 form이기 때문에 반드시 커스텀(확장)해야 함

**UserCreationForm() 커스텀 하기**

```python
# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        # get_user_model => 현재 활성화된 User class를 반환
        model = get_user_model()
        # fields = ('email', 'first_name', 'last_name',)

        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
```

**get_user_model()**

- “**현재 프로젝트에서 active user model 활성화된 사용자 모델**”을 반환
- 직접 참조하지 않는 이유
  - 기존 User 모델이 아닌 User 모델을 커스텀 한 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문
- Django는 User 클래스를 직접 참조하는 대신 `get_user_model()`을 사용해 참조해야 한다고 강조하고 있음

**CustomUserCreationForm() 으로 대체하기**

```python
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

**회원가입 후 곧바로 로그인 진행**

```python
# accounts/views.py

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원 가입 후 로그인 처리
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

**[참고] UserCreationForm의 save 메서드**

- user를 반환하는 것을 확인

> https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L139

```python
def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
        user.save()
    return user
```

### 회원 탈퇴

- 회원 탈퇴하는 것은 DB에서 유저를 Delete하는 것과 같음

**회원 탈퇴 로직 작성**

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('delete/', views.delete, name='delete'),
]
```

```python
# accounts/views.py

def delete(request):
    # 회원 탈퇴는 DB를 수정하는 것이기에 POST일 때만 동작
    if request.method == 'POST':
        # user 정보는 request 내부에 가지고 있어서
        # 따로 DB에서 불러올 필요없음
        request.user.delete()
    return redirect('articles:index')
```

```django
<!-- base.html -->

<h3>Hello, {{ user }}</h3>
...
<form action="{% url 'accounts:delete' %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="회원탈퇴">
</form>
```

**[참고] 탈퇴 하면서 해당 유저의 세션 정보도 함께 지우고 싶을 경우**

- “탈퇴(1) 후 로그아웃(2)”의 순서가 바뀌면 안됨
  - 먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 정보 또한 없어지기 때문


```python
# accounts/views.py

def delete(request):
    # 회원 탈퇴는 DB를 수정하는 것이기에 POST일 때만 동작
    if request.method == 'POST':
        # user 정보는 request 내부에 가지고 있어서
        # 따로 DB에서 불러올 필요없음
        request.user.delete()
        # 회원 탈퇴하면 로그인되어있을 필요가 없기 때문에 로그아웃
        # 탈퇴 전에 로그아웃을 하게되면 request 에 유저정보가 사라지므로
        # 탈퇴 후에 로그아웃을 해야한다
        auth_logout(request)
    return redirect('articles:index')
```

### 회원정보 수정

- 회원정보 수정 은 User를 Update 하는 것이며 **UserChangeForm** built-in form을 사용

**UserChangeForm**

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

- UserChangeForm 또한 ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일함

- 이미 이전에 CustomUserChangeForm으로 확장했기 때문에 CustomUserChangeForm을 사용하기


**회원정보 수정 페이지 작성**

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('update/', views.update, name='update'),
]
```

```python
# accounts/views.py
from .forms import CustomUserCreationForm, CustomUserChangeForm

def update(request):
    if request.method == 'POST':
        # instance 값이 없으면 새로 생성하는 로직이 되어버림
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

```django
<!-- accounts/update.html -->
{% extends 'base.html' %}

{% block content %}
<h1>회원정보수정</h1>
<form action="{% url 'accounts:update' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock content %}
```

**회원정보 수정 페이지 링크 작성**

```django
<!-- base.html -->
<div class="container">
  <h3>Hello, {{ user }}</h3>
  <a href="{% url 'accounts:login' %}">Login</a>
  <form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Logout">
  </form>
  <a href="{% url 'accounts:signup' %}">Signup</a>
  <a href="{% url 'accounts:update' %}">회원정보 수정</a>
  <hr>
  {% block content %}
  {% endblock content %}
</div>
```

**UserChangeForm 사용 시 문제점**

- 일반 사용자가 접근해서는 안 될 fields 정보들까지 모두 수정이 가능해짐
  - admin 인터페이스에서 사용되는 ModelForm이기 때문


- 따라서 UserChangeForm을 상속받아 작성해 두었던 서브 클래스 CustomUserChangeForm 에서 접근 가능한 필드를 조정해야 함

**CustomUserChangeForm fields 재정의**

- 수정하고자 하는 필드 작성

```python
# accounts/forms.py

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        # get_user_model => 현재 활성화된 User class를 반환
        model = get_user_model()
        # fields 정보를 UserChangeForm 것을 그대로 사용하면
        # 유저 관련 모든 데이터를 수정할 수 있기 때문에 보안에 위험
        # 그래서 유저들이 접근 가능한 필드들을 제한해야 한다.
        fields = ('email', 'first_name', 'last_name',)
```

- User 모델의 fields명은 어떻게 알 수 있을까?

**User model 상속 구조 살펴보기**

1. UserChangeForm 클래스 구조 확인

   - Meta 클래스를 보면 User라는 model을 참조하는 ModelForm이라는 것을 확인할 수 있음

     > https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L147

2. User 클래스 구조 확인

   - 실제로 User 클래스는 Meta 클래스를 제외한 코드가 없고 AbstractUser 클래스를 상속 받고있음

     >  https://github.com/django/django/blob/main/django/contrib/auth/models.py#L405

3. AbstractUser 클래스 구조 확인

   - 클래스 변수명들을 확인해보면 회원수정 페이지에서 봤던 필드들과 일치한다는 것을 확인할 수 있음

     > https://github.com/django/django/blob/main/django/contrib/auth/models.py#L334

4. 마지막으로 공식문서의 User 모델 Fields 확인

     > https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#user-model

### 비밀번호 변경

**PasswordChangeForm**

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form

- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함

- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

**비밀번호 변경 페이지 작성**

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [  # 경로가 아닌 부분을 password 로 하면 문제 생길 수 있음
    path('password/', views.change_password, name='change_password'),
]
```

```python
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # 일반 form 을 상속받았지만
            # save 메서드가 정의되어 있다.
            form.save()
            return redirect('articles:index')
    else:
        # 로그인한 유저의 비밀번호를 저장해야 하기에
        # 첫 번째 인자로 User 정보를 넣어야 한다.
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

```django
<!-- accounts/change_password.html -->
{% extends 'base.html' %}

{% block content %}
<h1>비밀번호 변경</h1>
<form action="{% url 'accounts:change_password' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock content %}
```

**[참고] SetPasswordForm 살펴보기**

- PasswordChangeForm은 SetPasswordForm의 하위 클래스이기 때문에 SetPasswordForm을 확인

**비밀번호 변경 로직 작성**

- 작성 후 비밀번호 변경 확인
  - 변경 후 로그인 상태가 지속되지 못하는 문제 발생


**암호 변경 시 세션 무효화 방지하기**

- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못함

- 비밀번호는 잘 변경되었으나 비밀번호가 변경 되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

**update_session_auth_hash()**

- update_session_auth_hash(request, user)

- current request 현재 요청과 새 session data가 파생 될 업데이트 된 사용자 객체를 가져오고, session data를 적절하게 업데이트해줌

- 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트

```python
# accounts/views.py
from django.contrib.auth import update_session_auth_hash

def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # 일반 form 을 상속받았지만
            # save 메서드가 정의되어 있다.
            form.save()  # 공식 문서 방식  
            # 비밀번호가 변경되면 session의 유저데이터와 일치하지 않게 되는 상황이 발생
            # 그렇기 때문에 session의 유저정보를 업데이트 시켜줘야 한다.
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        # 로그인한 유저의 비밀번호를 저장해야 하기에
        # 첫 번째 인자로 User 정보를 넣어야 한다.
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

## 5. Limiting access to logged-in users

- 로그인 사용자에 대한 접근 제한하기

- 로그인 사용자에 대한 접근을 제한하는 2가지 방법

1. The raw way
   - **is_authenticated** attribute
2. The **login_required** decorator

**is_authenticated**

- User model의 attributes 속성 중 하나

- 사용자가 인증 되었는지 여부를 알 수 있는 방법

- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
  - AnonymousUser에 대해서는 항상 False

- 일반적으로 **request.user**에서 이 속성을 사용 (request.user.is_authenticated)
- **permission 권한과는 관련이 없으며, 사용자가 active 활성화 상태이거나 valid session 유효한 세션을 가지고 있는지도 확인하지 않음**

**[참고] is_authenticated 코드 살펴보기**

> https://github.com/django/django/blob/main/django/contrib/auth/base_user.py#L56

```python
class AbstractBaseUser(models.Model):
    ...
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
```

**is_authenicated 적용하기**

- 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정하기

```django
<!-- base.html -->

{% if request.user.is_authenticated %}
  <h3>Hello, {{ user }}</h3>
  <form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Logout">
  </form>
  <a href="{% url 'accounts:update' %}">회원정보수정</a>
  <form action="{% url 'accounts:delete' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="회원탈퇴">
  </form>
{% else %}
  <a href="{% url 'accounts:login' %}">Login</a>
  <a href="{% url 'accounts:signup' %}">Signup</a>
{% endif %}
```

- 인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리하기

- 하지만 아직 비 로그인 상태로도 URL을 직접 입력하면 게시글 작성 페이지로 갈 수 있음

```django
<!-- articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">새 글을 작성하려면 로그인하세요</a>
  {% endif %}
{% endblock content %}
```

- 인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리

```python
# accounts/views.py

def login(request):
    # 로그인 한 사용자가 로그인 페이지를 볼 필요는 없음
    if request.user.is_authenticated:
        return redirect('articles:index')
```

**login_required**

- **login_required** decorator
- 사용자가 로그인 되어 있으면 정상적으로 view 함수를 실행
- 로그인 하지 않은 사용자의 경우 settings.py의 LOGIN_URL 문자열 주소로 redirect
  - [참고] LOGIN_URL의 기본 값은 /accounts/login/
  - 두번째 app 이름을 accounts 로 했던 이유 중 하나

- 로그인 상태에서만 글을 작성/수정/삭제 할 수 있도록 변경

  ```python
  from django.contrib.auth.decorators import login_required
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def create(request):
      pass
  
  @login_required
  @require_POST
  def delete(request, pk):
      pass
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      pass
  ```

- 인증 성공 시 사용자가 redirect 되어야하는 경로는 “next”라는 쿼리 문자열 매개 변수에 저장됨

  - 예시) /accounts/login/**?next=/articles/create/**

**“next” query string parameter**

- 로그인이 정상적으로 진행되면 이전에 요청했던 주소로 redirect 하기 위해 Django가 제공해주는 쿼리 스트링 파라미터

- 해당 값을 처리하지 말지는 자유이며 별도로 처리 해주지 않으면 view에 설정한 redirect 경로로 이동하게 됨

**“next” query string parameter 대응**

```python
# accounts/views.py

def login(request):
    # 로그인 한 사용자가 로그인 페이지를 볼 필요는 없음
    if request.user.is_authenticated:
        return redirect('articles:index')

    # 실제 로그인 동작이 일어날때 
    # session 이 create 되어 DB에 저장
    # POST 요청일 때 로그인 동작을 처리해야 함    
    if request.method == 'POST':
        # 사용자의 입력 데이터가 채워진 form 을 생성
        form = AuthenticationForm(request, request.POST)
        # 입력이 잘 되었는지 그리고 회원인지 확인
        if form.is_valid():
            # 우리 회원이라면 로그인 처리(session 생성해서 DB에 저장)
            # 유저 인스턴스가 필요한데 AuthenticationForm의 메소드를 이용
            # form.get_user() 의 반환값은 form에 담긴 user 인스턴스
            auth_login(request, form.get_user())
            # QueryStringParameter 로 전달되는 데이터를 가져오는 방법
            # 데이터가 있으면 next에 값이 들어감
            # 데이터가 없으면 next는 빈 값이 들어있음
            next = request.GET.get('next')
            # 단축 평가를 통해서 최종적으로 선택되는 값이 정해짐
            return redirect(next or 'articles:index')
```

**“next” query string parameter 주의사항**

- 만약 login 템플릿에서 form action이 작성되어 있다면 동작하지 않음

- 해당 action 주소 next 파라미터가 작성 되어있는 현재 url이 아닌 /accounts/login/으로 요청을 보내기 때문


```django
<!-- accounts/login.html -->

{% block content %}
  <h1>로그인</h1>  <!-- LOGIN을 Base.html에 만들기 권장 -->
  <!-- action 의 값이 비어있으면 현재 페이지로 요청을 보냄 -->
  <form action="" method="POST">
	{% csrf_token %}
    {{ form.as_p }}1
    <input type="submit">
  </form>
{% endblock content %}
```

**두 데코레이터로 인해 발생하는 구조적 문제**

1. 먼저 비로그인 상태로 detail 페이지에서 게시글 삭제 시도
2. delete view 함수의 **@login_required**로 인해 로그인 페이지로 리다이렉트
   - http://127.0.0.1:8000/accounts/login/?next=/articles/1/delete/
3. redirect로 이동한 로그인 페이지에서 로그인 진행
4. delete view 함수의 **@require_POST**로 인해 405 상태 코드를 받게 됨
   - 405(Method Not Allowed) status code 확인

- 로그인 성공 이후 GET method로 next 파라미터 주소에 리다이렉트 되기 때문

  ```bash
  Method Not Allowed (GET): /articles/1/delete/
  [07/Sep/2022 16:17:18] "GET /articles/1/delete/ HTTP/1.1" 405 0
  ```

- 두 가지 문제가 발생한 것

1. redirect 과정에서 POST 요청 데이터의 손실
2. redirect로 인한 요청은 GET 요청 메서드로만 요청됨

- 해결방안

  - **@login_required**는 GET request method를 처리할 수 있는 View 함수 에서만 사용해야함
  - 둘 중 하나만 남기기

- POST method만 허용하는 delete 같은 함수는 내부에서는 is_authenticated 속성 값을 사용 해서 처리

  ```python
  # articles/views.py
  
  @require_POST
  def delete(request, pk):
      if request.user.is_authenticated:
          article = Article.objects.get(pk=pk)
          article.delete()
      return redirect('articles:index')
  ```

**accounts view 함수에 모든 데코레이터 및 속성 값 적용해보기**

```python
# accounts/views.py

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods(['GET', 'POST'])
def login(request):
    pass

@require_POST
def logout(request):
    if request.user.is_authenticated:
        pass
    
@require_http_methods(['GET', 'POST'])
def signup(request):
    pass

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    pass

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    pass
```

## 마무리

- The Django authentication system
  - User 모델 대체하기


- HTTP Cookies
  - 상태가 있는 세션 구성


- Authentication in Web requests
  - Auth built-in form 사용하기


- Authentication with User
  - User Object와 User CRUD
