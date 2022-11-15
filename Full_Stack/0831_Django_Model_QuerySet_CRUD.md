[Django_Model_QuerySet_CRUD](#Django_Model_QuerySet_CRUD)

1. [Namespace](#1-namespace)
   - [URL namespace](#url-namespace)
   - [Template namespace](#template-namespace)
2. [Django Model](#2-django-model)
   - [Database](#database)
   - [Model](#model)
   - [Migrations](#migrations)
   - [추가 필드 정의](#추가-필드-정의)
   - [ORM](#orm)
3. [QuerySet API](#3-queryset-api)
   - [QuerySet API](#queryset-api)
   - [QuerySet API 익히기](#QuerySet-API-익히기)
4. [CRUD with view functions](#4-crud-with-view-functions)

- [Admin site](#admin-site)
- [마무리](#마무리)

# Django_Model_QuerySet_CRUD

## 1. Namespace

개체를 구분할 수 있는 범위를 나타내는 namespace 이름 공간에 대한 이해

### URL namespace

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음

- **app_name** attribute를 작성해 URL namespace를 설정

  ```python
  # 앱/urls.py
  app_name = "앱"
  urlpatterns = [
      ...,
  ]
  ```

  ```django
  <!--url 태그에서 반드시-->
  {% url 'app_name:url_name' %}
  <!--형태 안 맞으면 NoReverseMatch 에러 발생-->
  ```

**URL 참조**

- “`:`” 연산자를 사용하여 지정

### Template namespace

- Django는 기본적으로 **app_name/templates/** 경로에 있는 templates 파일들만 찾을 수 있으며, settings.py의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링 함

- 바로 이 속성 값이 해당 경로를 활성화하고 있음

  ```python
  # 프로젝트/settings.py
  TEMPLATES = [
      {
          ...,
          'APP_DIRS': True,
          ...
      },
  ]
  ```

**디렉토리 생성을 통해 물리적인 이름공간 구분**

- Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 `app_name/templates/app_name/` 형태로 변경

- Django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것

**반드시 Template namespace를 고려해야 할까?**

- 만약 단일 앱으로만 이루어진 프로젝트라면 상관없음
- 여러 앱이 되었을 떄에도 템플릿 파일 이름이 겹치지 않게 하면 되지만, 앱이 많아지면 대부분은 같은 이름의 템플릿 파일이 존재하기 마련

## 2. Django Model

Model 모델의 핵심 개념과 ORM을 통한 데이터베이스 조작 이해

Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공

### Database

체계화된 데이터의 모임

검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템

**Database 기본 구조**

1. Schema 스키마

2. Table 테이블

**Schema 스키마**

- Structure 뼈대

- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

  | column | datatype |
  | ------ | -------- |
  | id     | INT      |
  | name   | TEXT     |
  | age    | INT      |
  | email  | TEXT     |

**Table 테이블**

- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- Relation 관계라고도 부름

1. field(필드)

   - 속성, Column 컬럼

2. record(레코드)
   - 튜플, Row 행

**field 필드**

- 속성 혹은 column 컬럼
- 각 필드에는 고유한 데이터 형식이 지정됨
  - INT, TEXT 등

**record 레코드**

- 튜플 혹은 row 행
- 테이블의 데이터는 레코드에 저장됨

**Primary Key**

- 기본 키
- 각 레코드의 고유한 값 (식별자로 사용)
- 기술적으로 **다른 항목과 절대로 중복되어 나타날 수 없는 unique 단일 값**을 가짐
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용 됨

**Query 쿼리**

- 데이터를 조회하기 위한 명령어를 일컬음
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어 (주로 테이블형 자료구조에서)
- “Query를 날린다.”
  - “데이터베이스를 조작한다.”

### Model

Django는 Model을 통해 데이터에 접속하고 관리

단일한 데이터에 대한 정보를 가짐

사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함

저장된 데이터베이스의 layout 구조

일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 mapping 매핑

- 모델 클래스 1개 == 데이터베이스 테이블 1개

**Model 작성하기**

새 프로젝트(crud), 앱(articles) 작성 및 앱 등록

```bash
django-admin startproject crud .

python manage.py startapp articles
```

```python
# 프로젝트/settings.py
INSTALLED_APPS = [
    'articles',
    ...
]
```

models.py 작성

- 모델 클래스를 작성하는 것은 데이터베이스 **테이블의 스키마를 정의**하는 것

- “모델 클래스 == 테이블 스키마”

  ```python
  # 앱/models.py
  from django.db import models
  
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      # id 컬럼은 테이블 생성시 Django가 자동으로 생성
  ```

**Model 이해하기**

- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨

  - 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨

  - **클래스 상속 기반 형태의 Django 프레임워크 개발**
    - 프레임워크에서는 잘 만들어진 도구를 가져다가 잘 쓰는 것

- models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의
  - 클래스 변수 title과 content는 DB 필드를 나타냄

1. 클래스 변수(속성)명

   - DB 필드의 이름

2. 클래스 변수 값 (models 모듈의 Field 클래스)
   - DB 필드의 데이터 타입

**Django Model Field**

- Django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할

  데이터 유형 (INT, TEXT 등)을 정의

- 데이터 유형에 따라 다양한 모델 필드를 제공

  - DataField(), CharFIeld(), IntegerField() 등

  > <https://docs.djangoproject.com/en/3.2/ref/models/fields/>

**사용할 모델 필드 알아보기**

- **CharField(max_length=None, `options`)**
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  
  - **max_length**
    - 필드의 최대 길이(문자)
    - CharField의 필수 인자
    - 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용됨
  
- **TextField(`options`)**
  - 글자의 수가 많을 때 사용
  
  - max_length 옵션 작성 시 사용자 입력 단계에서는 반영 되지만, 모델과 데이터베이스 단계에는 적용되지 않음 (CharField를 사용해야 함)
    - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음

**데이터베이스 스키마**

- 지금까지 작성한 models.py는 데이터베이스 스키마를 설계한 것

- 이제 데이터베이스에 테이블을 생성하기 위한 **설계도** 작성이 필요함

  | Column  | Data Type   |
  | ------- | ----------- |
  | title   | VARCHAR(10) |
  | content | TEXT        |

### Migrations

모델에 대한 blueprint 청사진을 만들고 이를 통해 테이블을 생성하는 일련의 과정

Django가 모델에 생긴 변화(필드 추가, 모델 삭제 등)를 DB에 반영하는 방법

**Migrations 관련 주요 명령어**

1. makemigrations

2. migrate

**makemigrations**

- 모델을 작성 혹은 변경한 것에 기반한 새로운 migration(설계도, 청사진 이하 마이그레이션)을 만들 때 사용

- “테이블을 만들기 위한 설계도를 생성하는 것”

```bash
python manage.py makemigrations
```

- 명령어 실행 후 migrations/0001_initial.py 가 생성된 것을 확인

- “파이썬으로 작성된 설계도”

**migrate**

- makemigrations로 만든 migration 설계도를 실제 db.sqlite3 DB 파일에 반영하는 과정

- 결과적으로 **모델에서의 변경사항들**과 DB의 스키마가 동기화를 이룸

  - **“모델과 DB의 동기화”**

    ```bash
    python manage.py migrate
    ```

**[참고] Migrations 기타 명령어**

```bash
$ python manage.py showmigrations
# migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
# [X] 표시가 있으면 migrate가 완료되었음을 의미
```

```bash
$ python manage.py sqlmigrate [application_name] [migration_number]
# 해당 migrations 파일이 SQL 문으로 어떻게 해석 될 지 미리 확인 할 수 있음
```

### 추가 필드 정의

**Model 변경사항 반영하기**

- models.py에 변경사항이 생겼을 때 어떤 과정의 migration이 필요할까?

- 추가 모델 필드 작성 후 다시 한번 makemigrations 진행

```python
# 앱/model.py
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # id 컬럼은 테이블 생성시 Django가 자동으로 생성
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```bash
python manage.py makemigrations
```

- 기존에 id, title, content 컬럼을 가진 테이블에 2개의 컬럼이 추가되는 상황

- Django 입장에서는 이미 존재하는 테이블에 새로운 컬럼이 추가되는 요구 사항을 받았는데, 이 컬럼들은 기본적으로 빈 값으로 추가될 수 없음
  - 그래서 Django는 우리에게 추가되는 컬럼에 대한 기본 값을 설정해야 하니 어떻게 어떤 값을 설정할 것인지를 물어보는 과정을 진행

```bash
You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option:
```

- 각 보기 번호의 의미

  1. 다음 화면으로 넘어가서 새 컬럼의 기본 값을 직접 입력하는 방법

  2. 현재 과정에서 나가고 모델 필드에 default 속성을 직접 작성하는 방법

- “1”을 입력 후 Enter (created_at 필드에 대한 default 값 설정)

- 다음 화면에서 아무것도 입력하지 않고 Enter를 입력하면

  Django에서 기본적으로 파이썬의 timezone 모듈의 now 메서드 반환 값을

  기본 값으로 사용하도록 해줌

```bash
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>>
```

- 새로운 설계도(마이그레이션 파일)가 만들어 진 것을 확인

- 새로운 설계도를 생성하기 때문에 DB와 동기화를 진행해야 함

  (아직 DB에는 변경사항이 반영하지 않았기 때문)

```bash
python manage.py migrate
```

**`반드시` 기억해야 할 migration 3단계**

1. models.py에서 변경사항이 발생하면
2. migrations 파일 생성 (설계도 생성)
   - makemigrations
3. DB 반영 (모델과 DB의 동기화)
   - migrate

**DateTimeField()**

- Python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드

- DateField를 상속받는 클래스

- 선택 인자

  1. **auto_now_add**

     - 최초 생성 일자 (Useful for creation of timestamps)

     - Django ORM이 최초 insert(테이블에 데이터 입력)시에만

       현재 날짜와 시간으로 갱신(테이블에 어떤 값을 최초로 넣을 때)

  2. **auto_now**

     - 최종 수정 일자 (Useful for “last-modified” timestamps)

     - Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

**그런데 설계도는 어떻게, 누가 해석할까**

- makemigrations로 인해 만들어진 설계도는 파이썬으로 작성되어있음

- 그런데 SQL만 알아 들을 수 있다는 DB가 어떻게 이 설계도를 이해하고 동기화를 이룰 수 있을까?

- 바로 이 과정에서 중간에 해석을 담당하는 것이 **ORM**

### ORM

- Object-Relational-Mapping

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에

  (Django <-> SQL) 데이터를 변환하는 프로그래밍 기술

- 객체 지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와

  객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- Django는 내장 Django ORM을 사용

- https://django-orm-cookbook-ko.readthedocs.io/en/latest/

**ORM 장단점**

- 장점

  - SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능

  - 객체 지향적 접근으로 인한 높은 생산성

- 단점
  - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음

**ORM을 사용하는 이유**

- **“생산성”**

- 현시대 개발에서 가장 중요한 키워드는 바로 생산성

- 우리는 DB를 object 객체로 조작하기 위해 ORM을 사용할 것

**Model 정리**

- “웹 애플리케이션의 데이터를 **구조화**하고 **조작**하기 위한 도구”

## 3. QuerySet API

### 사전 준비

**외부 라이브러리 설치 및 설정**

- 편의를 위한 추가 라이브러리 설치 밀 설정

```bash
pip install ipython
pip install django-extensions
```

```python
# 프로젝트/settings.py
INSTALLED_APPS = [
    'articles',
    'django_extensions',

]
```

- 패키지 목록 업데이트

```bash
pip freeze > requirements.txt
```

**[참고] IPython & django-extensions**

- IPython

  - 파이썬 기본 쉘보다 더 강력한 파이썬 쉘

- django_extensions

  - Django 확장 프로그램 모음

  - shell_plus, graph model 등 다양한 확장 기능 제공

**[참고] Shell**

- 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램

- 셸(껍데기)은 사용자와 운영 체제의 내부사이의 인터페이스를 감싸는 층이기 때문에

  그러한 이름이 붙음

- “사용자 <-> 셸 <-> 운영체제”

**[참고] Python Shell**

- 파이썬 코드를 실행해주는 인터프리터

  - 인터프리터 : 코드를 한 줄 씩 읽어 내려가며 실행하는 프로그램

- 인터렉티브 혹은 대화형 shell 이라고 부름

- Python 명령어를 실행하여 그 결과를 바로 제공

```bash
python -i
```

**Django shell**

- ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용

- 다만 일반 파이썬 쉘을 통해서는 장고 프로젝트 환경에 영향을 줄 수 없기 때문에

  Django 환경 안에서 진행할 수 있는 Django 쉘을 사용

```bash
# 원래는 다음과 같은 명령어를 통해 Django shell을 사용하지만
$ python manage.py shell
# django-extension이 제공하는 더 강력한 shell_plus로 진행
$ python manage.py shell_plus

In [1]: Article.objects.all()
Out[1]: <QuerySet []>
```

### QuerySet API

**Database API**

- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움

- Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는

  DB API를 자동으로 만듦

**Database API 구문**

| Article     | objects | all()            |
| ----------- | ------- | ---------------- |
| Model class | Manager | **Queryset API** |

**“objects” manager**

- Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스

- Django는 기본적으로 모든 Django 모델 클래스에 대해 objects 라는

  Manager 객체를 자동-으로 추가함

- 이 Manager(objects)를 통해 특정 데이터를 조작(메서드)할 수 있음

- **“DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager”**

**Query**

- 데이터베이스에 특정한 데이터를 보여 달라는 요처

  - “쿼리문을 작성한다.”

    -> 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.

- 이 때, 파이썬으로 작성한 코드가 ORM의 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 **QuerySet**이라는 자료 형태로 변환하여 우리에게 전달

**QuerySet**

- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)

  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음

- Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음

- “objects” manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 때 반환되는 객체

- 단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 Class 모델의 인스턴스로 반환됨

**QuerySet API**

- “QuerySet과 상호작용하기 위해 사용하는 도구 (메서드, 연산자 등)”

### QuerySet API 익히기

Queryset API를 활용해 데이터를 생성하고, 읽고, 수정하고 삭제해보기

**CRUD**

- Create / Read / Update / Delete

  - 생성 / 조회 / 수정 / 삭제

- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말

### CREATE

**데이터 객체를 만드는(생성하는) 3가지 방법**

- 첫번째 방법

  1. article = Article()

     - 클래스를 통한 인스턴스 생성

  2. article.title

     - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당

  3. article.save()

     - 인스턴스로 save 메서드 호출

     - save 메서드를 호출해야 비로소 DB에 데이터가 저장된다. (레코드 생성)

```bash
article = Article()
article.title = '제목'
article.content = '내용'
article.save()
```

**두번째 방법**

- 인스턴스 생성 시 초기 값을 함께 작성하여 생성

```bash
article = Article(title='second', content='django!')
article.save()
```

**세번째 방법**

- QuerySet API 중 **create()** 메서드 활용

```bash
# 위 2가지 방식과는 다르게 바로 생성된 데이터가 반환된다.
Article.objects.create(title='third',content='django!')
```

**.save()**

- “Saving object”

- 객체를 데이터베이스에 저장함

- 데이터 생성 시 save를 호출하기 전에는 객체의 id 값은 None

  - id 값은 Django가 아니라 데이터베이스에서 계산되기 때문

- 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨

**vscode SQLite 확장프로그램을 통해 직접 테이블 데이터 확인하기**

- SQLite 설치

- 실행 (DB 우클릭 - Open Database)

- 좌측 하단 SQLITE EXPLORER 확인

- 테이블 선택 후 show table 버튼 클릭

- 테이블 데이터 확인

### READ

- QuerySet API method를 사용해 데이터를 다양하게 조회하기

- QuerySet API method는 크게 2가지로 분류됨

  1. Methods that “**return new querysets**”

  2. Methods that “**do not return querysets**”

**all()**

- QuerySet return

- 전체 데이터 조회

```bash
Article.objects.all()
```

**get()**

- 단일 데이터 조회

- 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고,

  둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

- 위와 같은 특징을 가지고 있기 때문에 primary key와 같이

  **uniqueness 고유성을 보장하는 조회에서 사용해야 함**

```bash
Article.objects.get(pk=1)
```

**filter()**

- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

```bash
>>> Article.objects.filter(content='django!')
<QuerySet []>
>>> Article.objects.filter(title='first')
<QuerySet [<Article: Article object 1)>]>
# 조회된 객체가 없거나 1개여도 QuerySet을 반환
```

**Field lookups**

- 특정 레코드에 대한 조건을 설정하는 방법

- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨

> <https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups>

```bash
Article.objects.filter(content__contains='ja')
```

### UPDATE

**Update 과정**

1. 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장

2. article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당

3. save() 인스턴스 메서드 호출

```bash
article = Article.objects.get(pk=1)
article.title = 'bye bye'
article.save()
```

### DELETE

**Delete 과정**

1. 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장

2. delete() 인스턴스 메서드 호출

```bash
article = Article.objects.get(pk=1)
article.delete()
```

**[참고] `__str__()`**

- 표준 파이썬 클래스의 메서드인 **str()** 을 정의하여 각각의 object가

  사람이 읽을 수 있는 문자열을 return 반환하도록 할 수 있음

```python
def __str__(self):
    return self.title
```

- Django shell에서 변화된 출력 확인

```bash
>>> article = Article.objects.get(pk=1)
>>> article
<QuerySet [<Article: 'first']>
# __str__() 작성 후 반드시 shell을 재시작해야 반영됨
```

## 4. CRUD with view functions

QuerySet API를 통해 view 함수에서 직접 CRUD 구현하기

### 사전준비

**base 템플릿 작성**

- bootstrap CDN 및 템플릿 추가 경로 작성

  ```django
  <!-- templates/base.html -->
  <!DOCTYPE html>
  <html lang="en">
  
    <head>
      <meta charset="UTF-8"/>
      <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <!-- bootstrap CSS CDN -->
      <title>Document</title>
    </head>
  
    <body>
      <div class="container">
        {% block content %}{% endblock content %}
      </div>
      <!-- bootstrap JS CDN -->
    </body>
  
  </html>
  ```
  
  ```python
  # 프로젝트/settings.py
  TEMPLATES = [
      {
          ...,
          'DIRS': [BASE_DIR / 'templates'],
          ...,
      },
  ]
  ```

**url 분리 및 연결**

```python
# 앱/urls.py
from django.urls import path

app_name = 'articles'
urlpatterns = [

]
```

```python
# 프로젝트/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

**index 페이지 작성**

```python
# 앱/urls.py
from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]
```

```python
# 앱/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'articles/index.html')
```

```django
<!-- 앱/templates/앱/index.html -->
{% extends 'base.html' %}
{% block content %}
  <h1>Articles</h1>
{% endblock content %}
```

### READ

**전체 게시글 조회**

- index 페이지에서는 전체 게시글을 조회해서 출력한다.

```python
# 앱/views.py
from django.shortcuts import render

from .models import Article


def index(request):
    # 1. 모든 데이터를 확보
    articles = Article.objects.all()
    # 2. 확보한 데이터를 template 에 보여줘야 한다.
    # 확보한 데이터를 템플릿으로 전달할 필요가 있다.
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

```django
<!-- 앱/templates/앱/index.html -->
{% extends 'base.html' %}
{% block content %}
  <h1>Articles</h1>
  <hr/>
  {% for article in articles %}
    <p>글 번호:
      {{ article.pk }}</p>
    <p>글 제목:
      {{ article.title }}</p>
    <p>글 내용:
      {{ article.content }}</p>
    <hr/>
  {% endfor %}
{% endblock content %}
```

**개별 게시글 상세 페이지 제작**

- 글의 pk 번호를 활용해서 하나의 뷰 함수와 템플릿 함수로 대응
  - Variable Routing

**urls**

- URL로 특정 게시글을 조회할 수 있는 번호를 받음

  ```python
  # 앱/urls.py
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
      path('<int:pk>/', views.detail, name='detail'),
  ]
  ```

**views**

- Article.objects.get(pk=pk)에서 오른쪽 pk는 variable routing을 통해 받은 pk, 왼쪽 pk는 DB에 저장된 레코드의 id 컬럼

  ```python
  # 앱/views.py
  from django.shortcuts import render
  
  from .models import Article
  
  
  # 글 내용 조회 (하나의 글 데이터 필요)
  def detail(request, pk):
      # query api 에서 get 메소드는 유일한 값을 이용해서 데이터를 찾음
      article = Article.objects.get(pk=pk)
      # 전달 받은 아이디로 데이터를 가져온다. (데이터 확보)
      context = {
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```

**templates**

```django
<!-- 앱/templates/앱/detail.html -->
{% extends 'base.html' %}
{% block content %}
  <h2>DETAIL</h2>
  <h3>{{ article.pk }}
    번째 글</h3>
  <hr/>
  <p>제목:
    {{ article.title }}</p>
  <p>내용:
    {{ article.content }}</p>
  <p>작성 시각:
    {{ article.created_at }}</p>
  <p>수정 시각:
    {{ article.updated_at }}</p>
  <hr/>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

```django
<!-- 앱/templates/앱/index.html -->
{% extends 'base.html' %}
{% block content %}
  <h1>Articles</h1>
  <a href="{% url 'articles:new' %}">NEW</a>
  <hr/>
  {% for article in articles %}
    <a href="{% url 'articles:detail' article.pk %}">[detail]</a>
    <hr/>
  {% endfor %}
{% endblock content %}

```

**redirect 인자 변경**

```python
# 앱/views.py
from django.shortcuts import redirect

from .models import Article


def create(request, pk):
    article = Article.objects.get(pk=pk)
    # 글 작성을 완료하고 나면 다음 뜨는 페이지
    return redirect('articles:detail', article.pk)
```

### CREATE

CREATE 로직을 구현하기 위해서는 몇 개의 view 함수가 필요할까?

- 사용자의 입력을 받을 페이지를 렌더링 하는 함수 1개

  - **“new” view function**

  ```python
  # 앱/urls.py
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('new/', views.new, name='new'),
  ]
  ```

  ```python
  # 앱/views.py
  from django.shortcuts import render
  
  
  # 글 쓰기 버튼을 눌렀을 때
  # 사용자 입력 페이지 (글쓰기 페이지) 응답으로 전달
  def new(request):
      return render(request, 'articles/new.html')
  ```
  
  ```django
  <!-- 앱/templates/앱/new.html -->
  {% extends 'base.html' %}
  {% block content %}
    <h1>NEW</h1>
    <form action="#" method="GET">
      <label for="title">Title:
      </label>
      <input type="text" name="title"/>
      <br/>
      <label for="content">Content:
      </label>
      <textarea name="content"></textarea>
      <br/>
      <input type="submit"/>
    </form>
    <hr/>
    <a href="{% url 'articles:index' %}">[back]</a>
  {% endblock content %}
  ```
  
  - new 페이지로 이동할 수 있는 하이퍼 링크 작성
  
  ```django
  <!-- 앱/templates/앱/index.html -->
  {% extends 'base.html' %}
  {% block content %}
    <h1>Articles</h1>
    <a href="{% url 'articles:new' %}">NEW</a>
    <hr/>
  {% endblock content %}
  ```
  
- 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수 1개

  - **“create” view function**

  ```python
  # 앱/urls.py
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
      path('create/', views.create, name='create'),
  ]
  ```

  ```python
  # 앱/views.py
  from django.shortcuts import render
  
  from .models import Article
  
  
  # 사용자가 작성한 데이터를 받아서 DB에 저장하는 역할
  def create(request):
      # 데이터 저장하기 위해서는 사용자의 데이터를 확보
      title = request.POST.get('title')
      content = request.POST.get('content')
      # Post 클래스의 인스턴스를 생성 (클래스 변수를 같이 줘야 함)
      article = Article(title=title, content=content)
      article.save()  # 확보한 데이터를 DB에 저장
      return render(request, 'articles/create.html')
  ```
  
  - create 메서드가 더 간단해 보이지만 추후 데이터가 저장되기 전에 유효성 검사 과정을 거치게 될 예정
  - 유효성 검사가 진행된 후에 save 메서드가 호출되는 구조를 택하기 위함
  - 게시글 작성 후 확인
  
  ```django
  <!-- 앱/templates/앱/create.html -->
  {% extends 'base.html' %}
  {% block content %}
    <h1>성공적으로 글이 작성되었습니다.</h1>
  {% endblock content %}
  ```
  
  ```django
  <!-- 앱/templates/앱/new.html -->
  {% extends 'base.html' %}
  {% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="GET">
      <label for="title">Title:
      </label>
      <input type="text" name="title"/>
      <br/>
      <label for="content">Content:
      </label>
      <textarea name="content"></textarea>
      <br/>
      <input type="submit"/>
    </form>
    <hr/>
    <a href="{% url 'articles:index' %}">[back]</a>
  {% endblock content %}
  ```
  
  - 게시글 작성 후 index 페이지로 돌아고도록 함
  
  ```python
  # 앱/view.py
  from django.shortcuts import render
  
  
  def create(request):
      return render(request, 'articles/index.html')
  ```

**Django shortcut function - "redirect()"**

- 인자에 작성된 곳으로 요청을 보냄
  - view name (URL pattern name)

```python
# 앱/views.py
from django.shortcuts import redirect


def create(request):
    # 글 작성을 완료하고 나면 다음 뜨는 페이지
    # index 페이지로 이동해서 전체 데이터 목록
    return redirect('articles:index')
```

**redirect 동작 이해하기**

- 동작원리

  1. 클라이언트가 create url로 요청을 보냄

  2. create view 함수의 redirect 함수가 302 status code를 응답

  3. 응답 받은 브라우저는 redirect 인자에 담긴 index 주소로

     사용자를 이동시키기 위해 index url로 Django에 재요청

  4. index page를 정상적으로 응답 받음 (200 status code)

**[참고] 302 Found**

- HTTP response status code 중 하나

- 해당 상태 코드를 응답 받으면 브라우저는 사용자를 해당 URL의 페이지로 이동 시킴

**HTTP response status code**

- 클라이언트에게 특정 HTTP **요청이 성공적으로 완료되었는지 여부**를 알려줌

- 응답은 5개 그룹으로 나뉘어짐
  1. 1xx Informational responses
  2. 2xx Successful responses
  3. 3xx Redirection messages
  4. 4xx Client error responses
  5. 5xx Server error responses

**HTTP method GET 재검토**

- 현재는 게시글이 작성될 때 **/articles/create/?title=1&content2** 와 같은 URL로 요청이 보-내짐

- GET은 쿼리 스트링 파라미터로 데이터를 보내기 때문에 url을 통해 데이터를 보냄

- 하지만 현재 요청은 데이터를 조회하는 것이 아닌 작성을 원하는 요청

- GET이 아닌 다른 HTTP method를 알아보기

**HTTP request method**

- HTTP는 request method를 정의하여, 주어진 리소스에 수행하길 원하는 행동을 나타냄

- GET

  - 특정 리소스를 가져오도록 요청할 때 사용

  - 반드시 데이터를 가져올 때만 사용해야 함

  - DB에 변화를 주지 않음

  - CRUD에서 R 역할을 담당

- POST

  - 서버로 데이터를 전송할 때 사용

  - 서버에 변경사항을 만듦

  - 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송

  - GET의 쿼리 스트링 파라미터와 다르게 URL로 보내지지 않음

  - CRUD에서 C/U/D 역할을 담당

**HTML method 적용하기**

- 로그인에 GET이 아닌 POST를 사용
- 검색에서는 GET을 사용

  - 검색은 서버에 영향을 미치는 것이 아닌 특정 데이터를 조회만 하는 요청이기 때문
  - 특정 페이지를 조회하는 요청을 보내는 HTML의 a tag 또한 GET을 사용

- GET은 단순히 조회하려는 경우 & **POST는 서버나 DB에 변경을 요청하는 경우**

**[참고] 403 Forbidden**

- 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미

- 서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환됨

- 즉, 게시글을 작성할 권한이 없다 -> Django 입장에서는 "작성자가 누구인지 모르기 때문에 함부로 작성할 수 없다"라는 의미

- DB 모델을 조작하는 것은 단순 조회와 달리 최소한의 신원 확인이 필요하기 때문

**CSRF**

- **Cross-Site-Request-Forgery**

- "사이트 간 요청 위조"

- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

**CSRF 공격 방어**

- "Security Token 사용 방식 (CSRF Token)"

  - 사용자의 데이터에 임의의 난수 token 값을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송 시키도록 함

  - 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증

  - 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용

  - Django는 DTL에서 csrf_token 템플릿 태그를 제공

**csrf_token 템플릿 태그**

```django
{% csrf_token %}
```

- 해당 태그가 없다면 Django 서버는 요청에 대해 403 forbidden으로 응답

- 템플릿에서 내부 URL로 향하는 Post form을 사용하는 경우에 사용

  - 외부 URL로 향하는 POST form에 대해서는 CSRF 토큰이 유출되어 취약성을 유발할 수 있기 때문에 사용해서는 안됨

- input type이 hidden으로 작성되며 value는 Django에서 생성한 hash 값으로 설정

- "csrf_token 은 해당 POST 요청이 내가 보낸 것 인지를 검증하는 것"

### DELETE

**urls**

- 모든 글을 삭제 하는 것이 아니라 삭제하고자 하는 특정 글을 조회 후 삭제해야 함

  ```python
  # 앱/urls.py
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
      path('<int:pk>/delete/', views.delete, name='delete'),
  ]
  ```

**views**

```python
# 앱/views.py
from django.shortcuts import redirect

from .models import Article


def delete(request, pk):
    # 1. 삭제할 데이터를 가져온다
    article = Article.objects.get(pk=pk)
    # 2. 삭제한다.
    article.delete()
    return redirect('articles:index')
```

**templates**

- Detail 페이지에 작성하며 DB에 영향을 미치기 때문에 POST method를 사용

  ```django
  <!-- 앱/templates/앱/detail.html -->
  {% extends 'base.html' %}
  {% block content %}
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE"/>
    </form>
    <a href="{% url 'articles:index' %}">[back]</a>
  {% endblock content %}
  ```

### UPDATE

- 수정은 CREATE 로직과 마찬가지로 2개의 view 함수가 필요

- 사용자의 입력을 받을 페이지를 렌더링 하는 함수 1개

  - "edit" view function

    ```python
    # 앱/urls.py
    from django.urls import path
    
    from . import views
    
    urlpatterns = [
        path('<int:pk>/edit/', views.edit, name='edit'),
    ]
    ```

    ```python
    # 앱/views.py
    from django.shortcuts import render
    
    from .models import Article
    
    
    def edit(request, pk):
        article = Article.objects.get(pk=pk)
        context = {
            'article': article,
        }
        return render(request, 'articles/edit.html', context)
    ```

  - html 태그의 value 속성을 사용해 기존에 입력 되어 있던 데이터를 출력

    - **textarea 태그는 value 속성이 없으므로 태그 내부 값으로 작성해야 한다.**

    ```django
    <!-- 앱/templates/앱/edit.html -->
    {% extends 'base.html' %}
    {% block content %}
      <h1>EDIT</h1>
      <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
        <label for="title">Title:
        </label>
        <input type="text" name="title" value="{{ article.title }}"/>
        <br/>
        <label for="content">Content:
        </label>
        <textarea name="content" cols="30" rows="5">{{ article.content }}</textarea>
        <br/>
        <input type="submit"/>
      </form>
      <a href="{% url 'articles:index' %}">[back]</a>
    {% endblock content %}
    ```
    
  - Edit 페이지로 이동하기 위한 하이퍼 링크 작성

    ```django
    <!-- 앱/templates/앱/detail.html -->
    {% extends 'base.html' %}
    {% block content %}
      <h2>DETAIL</h2>
      <h3>{{ article.pk }}
        번째 글</h3>
      <hr/>
      <p>제목:
        {{ article.title }}</p>
      <p>내용:
        {{ article.content }}</p>
      <p>작성 시각:
        {{ article.created_at }}</p>
      <p>수정 시각:
        {{ article.updated_at }}</p>
      <hr/>
      <a href="{% url 'articles:edit' article.pk %}">EDIT</a>
      <br/>
      <form action="{% url 'articles:edit' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE"/>
      </form>
      <a href="{% url 'articles:index' %}">[back]</a>
    {% endblock content %}
    ```

- 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수 1개

  - "update" view function

    ```python
    # 앱/urls.py
    from django.urls import path
    
    from . import views
    
    urlpatterns = [
        path('<int:pk/update/', views.update, name='update'),
    ]
    ```

    ```python
    # 앱/view.py
    from django.shortcuts import redirect
    
    from .models import Article
    
    
    def update(request, pk):
        # 1. 수정할 글 데이터를 찾아온다.
        article = Article.objects.get(pk=pk)
        # 2. 수정한다.
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        # 3. 저장한다.
        article.save()
        # 글 수정 완료, 글 디테일 페이지로 가서 글을 확인
        return redirect('articles:detail', article.pk)
    ```
    
    ```django
    <!-- 앱/edit.html -->
    {% extends 'base.html' %}
    {% block content %}
      <h1>EDIT</h1>
      <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
      </form>
      <a href="{% url 'articles:index' %}">[back]</a>
    {% endblock content %}
    ```

### Admin site

- **Django의 가장 강력한 기능 중 하나**인 automatic admin interface 알아보기

- "관리자 페이지"

  - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지

  - 모델 class를 admin.py에 등록하고 관리

  - 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있음

**admin 계정 생성**

```bash
python manage.py createsuperuser
```

- username과 password를 입력해 관리자 계정을 생성

- **email은 선택사항이기 때문에 입력하지 않고 enter를 입력하는 것이 가능**

- **비밀번호 생성 시 보안상 터미널에 입력되지 않으니 무시하고 입력을 이어가도록 함**

**admin site 로그인**

- <http://127.0.0.1:8000/admin/> 로 접속 후 로그인

- 계정만 만든 경우 Django 관리자 화면에서 모델 클래스는 보이지 않음

**admin에 모델 클래스 등록**

- 모델의 record를 보기 위해서는 admin.py에 등록 필요

```python
# 앱/admin.py
from django.contrib import admin

from .models import Article

admin.site.register(Article)
```

## 마무리

Model

- Django는 Model을 통해 데이터에 접속하고 관리

ORM

- 객체지향 프로그래밍을 이용한 DB 조작

Migrations

- 모델에 생긴 변화(필드 추가, 모델 삭제 등)를 DB에 반영하는 방법(과정)

HTTP request & response

- 요청에 행동을 표현하는 HTTP request method
- 요청에 대한 성공 여부 응답을 숫자로 표현하는 HTTP response status codes
