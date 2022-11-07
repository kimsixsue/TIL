- [Django_REST_API](#django-rest-api)
  - [REST API](#rest-api)
    - [HTTP](#http)
    - [Identifying resources on the Web](#identifying-resources-on-the-web)
    - [URI](#uri)
    - [REST API](#rest-api-1)
  - [Response JSON](#response-json)
    - [Intro](#intro)
    - [Response](#response)
  - [Django REST framework Single Model](#django-rest-framework-single-model)
    - [ModelSerializer](#modelserializer)
    - [Build RESTful API Article](#build-restful-api-article)
  - [Django REST framework N-1 Relation](#django-rest-framework-n-1-relation)
    - [N-1 역참조 데이터 조회](#n-1-역참조-데이터-조회)
    - [Django shortcuts functions](#django-shortcuts-functions)
  - [finish](#finish)

# Django REST API

## REST API

### HTTP

- HTML 문서와 같은 resource 자원들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
- 클라이언트와 서버는 다음과 같은 개별적인 메시지 교환에 의해 통신
  - request 요청
    - 클라이언트에 의해 전송되는 메시지
  - response 응답
    - 서버에서 응답으로 전송되는 메시지

**HTTP 특징**

- Stateless 무상태
  - 동일한 connection 연결에서 연속적으로 수행되는 두 요청 사이에 링크가 없음
  - 즉, 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음

**HTTP Request Methods**

- 리소스에 대한 행위(수행하고자 하는 동작)를 정의
- 즉, 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의
- HTTP verbs 라고도 함
- HTTP Method 예시
  - GET, POST, PUT, DELETE

1. GET
   - 서버에 리소스의 표현을 요청
   - GET을 사용하는 요청은 데이터만 검색해야 함
2. POST
   - 데이터를 지정된 리소스에 제출
   - 서버의 상태를 변경
3. PUT
   - 요청한 주소의 리소스를 수정
4. DELETE
   - 지정된 리소스를 삭제

**HTTP response status codes**

- 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
- 응답을 5개의 그룹으로 나뉨
  1. Informational responses (100-199)
  2. Successful responses (200-299)
  3. Redirection messages (300-399)
  4. Client error responses (400-499)
  5. Server error responses (500-599)

### Identifying resources on the Web

**웹에서의 리소스 식별**

- HTTP 요청의 대상을 resource 자원이라고 함
- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
- 각 리소스는 식별을 위해 **URI**로 식별됨

### URI

- Uniform Resource Identifier 통합 자원 식별자
- 인터넷에서 하나의 리소스를 가리키는 문자열
- 가장 일반적인 URI는 웹 주소로 알려진 **URL**

- 특정 이름공간에서 **이름**으로 리소스를 식별하는 URI는 **URN**

**URL**

- Uniform Resource Locator (통합 자원 **위치**)
- 웹에서 주어진 리소스의 주소
- 네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속
  - 이러한 리소스는 HTML, CSS, 이미지 등이 될 수 있음
- URL은 여러 부분으로 구성되며 일부는 필수이고 나머지는 선택사항

**URL 구조**

- Scheme (or protocol)

  - 브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜
  - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄
  - 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기위한 mailto:, 파일을 전송하기 위한 ftp: 등 다른 프로토콜도 존재

- Authority

  - Scheme 다음은 문자 패턴 :// 으로 구분된 Authority 권한이 작성됨
  - Authority는 domain과 port를 모두 포함하며 둘은 : 콜론 으로 구분됨

  1. Domain Name
     - 요청 중인 웹 서버를 나타냄
     - 어떤 웹 서버가 요구되는지를 가리키며 직접 IP 주소를 사용하는 것도 가능. 하지만, 사람이 외우기 어렵기 때문에 주로 Domain Name으로 사용
     - 예를 들어 도메인 google.com의 IP 주소는 142.251.42.142
  2. Port
     - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 Gate 문
     - HTTP 프로토콜의 표준 포트는 다음과 같고 생략이 가능 (나머지는 생략 불가능)
       - HTTP - 80
       - HTTPS - 443
     - Django의 경우 8000(80+00)이 기본 포트로 설정되어 있음

- Path

  - 웹 서버의 리소스 경로
  - 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현

- Parameters

  - 웹 서버에 제공하는 추가적인 데이터
  - 파라미터는 ‘&’ 기호로 구분되는 key-value 쌍 목록
  - 서버는 리소르를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음

- Anchor

  - 리소스의 다른 부분에 대한 앵커
  - 리소스 내부 일종의 “북마크”를 나타내며 브라우저에 해당 북마크 지점에 있는 콘텐츠를 표시
    - 예를 들어 HTML 문서에서 브라우저는 앵커가 정의한 지점으로 스크롤 함
  - fragment identifier 부분 식별자라고 부르는 ‘#’ 이후 부분은 서버에 전송되지 않음

### REST API

**API**

- Application Programming Interface
- 애플리케이션과 프로그래밍으로 소통하는 방법
  - 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성
- API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약 (인터페이스)이라고 볼 수 있음
- API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공

**Web API**

- 웹 서버 또는 웹 브라우저를 위한 API
- 현재 웹 개발은 모든 것을 하나부터 열까지 직접 개발하기보다 여러 Open API를 활용하는 추세
- API는 다양한 타입의 데이터를 응답
  - HTML, XML, **JSON** 등

**REST**

- Representational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - 2000년 로이 필딩의 박사학위 논문에서 처음으로 소개 된 후 네트워킹 문화에 널리 퍼짐
- a group of software architecture design constraints 소프트웨어 아키텍쳐 디자인 제약 모음
- REST 원리를 따르는 시스템을 **RESTful** 하다고 부름
- REST의 기본 아이디어는 리소스 즉 자원
  - **자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술**

**REST에서 자원을 정의하고 주소를 지정하는 방법**

1. 자원의 식별
   - **URI**
2. 자원의 행위
   - **HTTP Method**
3. 자원의 표현
   - 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) 결과물
   - **JSON**으로 표현된 데이터를 제공

**JSON**

- JSON is a lightweight data-interchange format
- JavaScript의 표기법을 따른 단순 문자열
- 파이썬의 dictionary, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 **key-value 형태의 구조**를 갖고 있음
- 사람이 읽고 쓰기 쉽고 기계가 파싱(해석 & 분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터 타입

## Response JSON

- JSON 형태로의 서버 응답 변화
- 다양한 방법의 JSON 응답

### Intro

**서버가 응답하는 것**

- 서버가 응답할 수 있는 것은 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음
- JSON 데이터를 응답하는 서버로의 변환
- JSON 데이터를 받아 화면을 구성하여 사용자에게 보여주는 것은 Front-end Framework가 담당할 예정
- Front-end Framework는 Vue.js를 사용
- Front-end와 Back-end가 분리되어 구성되게 됨

### Response

다양한 방법으로 JSON 데이터 응답해보기

1. HTML 응답
2. JsonResponse()를 사용한 JSON 응답
   - Django가 기본적으로 제공하는 JsonResponse 객체를 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능
   - **JsonResponse()**
     - JSON-encoded response를 만드는 클래스
     - **safe** parameter
       - 기본 값 True
       - False로 설정 시 모든 타입의 객체를 serialization 할 수 있음 (그렇지 않으면 dict 인스턴스만 허용됨)
3. Django Serializer를 사용한 JSON 응답

   - Django의 내장 HttpResponse()를 활용한 JSON 응답
   - **Serialization**
     - “직렬화”
     - 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
       - 즉, 어떠한 언어나 환경에서도 “**나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정**”
     - 변환 포맷은 **json**, xml, yaml이 있음
   - Django의 `serialize()`는 Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환 할 수 있는 Python 데이터 타입으로 만들어 줌

4. Django REST framework를 사용한 JSON 응답

   - **Django Rest Framework**

     - Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

     - Web API 구축을 위한 강력한 toolkit을 제공

     - REST framework를 작성하기 위한 여러 기능을 제공

     - DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동

       > <https://www.django-rest-framework.org/>

## Django REST framework Single Model

단일 모델의 data를 Serialization하여 JSON으로 변환하는 방법에 대한 학습

```bash
python -m venv venv
source venv/Scripts/activate
django-admin startproject 프로젝트 .
python manage.py startapp 앱
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata D/M.json D/M.json D/M.json
python manage.py createsuperuser
python manage.py runserver
```

```python
# /settings.py
INSTALLED_APPS = [
    '앱',
    'rest_framework',
    'django_seed',
    'django_extensions',
]
```

```python
# /urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('앱.urls')),
]
```

```python
# 앱/admin.py
from django.contrib import admin

from .models import 모델클래스

admin.site.register(모델클래스)
```

### ModelSerializer

**ModelSerializer 작성**

- articles/serializers.py 생성

  - serializers.py의 위치나 파일명은 자유롭게 작성 가능

  ```python
  # articles/serializers.py
  
  from rest_framework import serializers
  
  from .models import Article
  
  # 여러 데이터의 정보를 보여줄 때 사용하는 serializer
  class ArticleListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = ('id', 'title', 'content',)
  ```

**ModelSerializer**

- ModelSerializer 클래스는 모델 필드가 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
  1. Model 정보에 맞춰 자동으로 필드를 생성
  2. serializer에 대한 유효성 검사기를 자동으로 생성
  3. `.create()` 및 `.update()`의 간단한 기본 구현이 포함됨

**ModelSerializer의 `many` option**

- 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize 하려면 many=True를 작성해야 함

### Build RESTful API Article

**GET - List**

- 게시글 데이터 목록 조회하기

- DRF에서 **api_view** 데코레이터 작성은 필수

  ```python
  # articles/urls.py
  
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
      path('articles/', views.articles_list),
  ]
  ```

  ```python
  # articles/views.py
  
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Article
  from .serializers import ArticleListSerializer

  @api_view(['GET'])
  def article_list(request):
      articles = Article.objects.all()
      serializer = ArticleListSerializer(articles, many=True)
      return Response(serializer.data)
  ```

- **api_view** decorator

  - DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음
  - 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답

**GET - Detail**

- 단일 게시글 데이터 조회하기

- 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의

  ```python
  # articles/serializers.py
  
  from rest_framework import serializers
  
  from .models import Article
  
  class ArticleSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = '__all__'  # 생성, 수정을 할 때 모든 필드의 유효성 검사
  ```

  ```python
  # articles/urls.py
  
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
  
      path('articles/<int:article_pk>/', views.articles_detail),
  ]
  ```

  ```python
  # articles/views.py
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Article
  from .serializers import ArticleSerializer
  
  @api_view(['GET'])
  def article_detail(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      serializer = ArticleSerializer(article)
      return Response(serializer.data)
  ```

**POST**

- 게시글 데이터 생성하기

- 요청에 대한 데이터 생성이 성공했을 경우는 201 Created 상태 코드를 응답하고 실패 했을 경우는 400 Bad request를 응답

  ```python
  # articles/views.py
  
  from rest_framework import status
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Article
  from .serializers import ArticleListSerializer, ArticleSerializer
  
  @api_view(['GET', 'POST'])
  def article_list(request):
      if request.method == 'GET':
          articles = Article.objects.all()
          serializer = ArticleListSerializer(articles, many=True)
          return Response(serializer.data)
  
      elif request.method == 'POST':
          serializer = ArticleSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  ```

**Raising an exception on invalid data**

- 유효하지 않은 데이터에 대해 예외 발생시키기

- is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음

- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환

- view 함수 코드 변경

  ```python
  # articles/views.py
  
  from rest_framework import status
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .serializers import ArticleSerializer
  
  @api_view(['GET', 'POST'])
  def article_list(request):
  
      elif request.method == 'POST':
          serializer = ArticleSerializer(data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```

**DELETE**

- 게시글 데이터 삭제하기

- 요청에 대한 데이터 삭제가 성공했을 경우는 204 No Content 상태 코드 응답 (명령을 수행했고 더 이상 제공할 정보가 없는 경우)

  ```python
  # articles/views.py
  
  from rest_framework import status
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Article
  from .serializers import ArticleSerializer
  
  @api_view(['GET', 'DELETE'])
  def article_detail(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      if request.method == 'GET':
       serializer = ArticleSerializer(article)
       return Response(serializer.data)
  
      elif request.method == 'DELETE':
          article.delete()
          return Response({'id': article_pk}, status=status.HTTP_204_NO_CONTENT)
  
      elif request.method == 'DELETE':
          review.delete()
          msg = f"review {review_pk} is deleted"
          return Response({"delete": msg}, status=status.HTTP_204_NO_CONTENT)
  ```

**PUT**

- 게시글 데이터 수정하기

- 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 상태 코드 응답

  ```python
  # articles/views.py
  
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .serializers import ArticleSerializer
  
  @api_view(['GET', 'DELETE', 'PUT'])
  def article_detail(request, article_pk):
  
      elif request.method == 'PUT':
          serializer = ArticleSerializer(article, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  ```

## Django REST framework N-1 Relation

- N:1 관계에서의 모델 data를 Serialization하여 JSON으로 변환하는 방법 학습

**GET - List**

- 댓글 데이터 목록 조회하기

  ```python
  # articles/serializers.py
  
  from rest_framework import serializers
  
  from .models import Comment
  
  class CommentSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Comment
          fields = '__all__'
  ```

  ```python
  # articles/urls.py
  
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
  
      path('comments/', views.comment_list),
  ]
  ```

  ```python
  # articles/views.py
  
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Comment
  from .serializers import CommentSerializer
  
  @api_view(['GET'])
  def comment_list(request):
      comments = Comment.objects.all()
      serializer = CommentSerializer(comments, many=True)
      return Response(serializer.data)
  ```

**GET - Detail**

- 단일 댓글 데이터 조회하기

  ```python
  # articles/urls.py
  
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
  
      path('comments/<int:comment_pk>/', views.comment_detail),
  ]
  ```

  ```python
  # articles/views.py
  
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Comment
  from .serializers import CommentSerializer
  
  @api_view(['GET'])
  def comment_detail(request, comment_pk):
      comment = Comment.objects.get(pk=comment_pk)
      serializer = CommentSerializer(comment)
      return Response(serializer.data)
  ```

**POST**

- 단일 댓글 데이터 생성하기

  ```python
  # articles/urls.py
  
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
  
      path('articles/<int:article_pk>/comments/', views.comment_create),
  ]
  ```

  ```python
  # articles/views.py
  
  from rest_framework import status
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Article
  from .serializers import CommentSerializer
  
  @api_view(['POST'])
  def comment_create(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```

**Passing Additional attributes to `.save()`**

- **save() 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음**

- **CommentSerializer를 통해 Serialize되는 과정에서 Parameter로 넘어온 article_pk에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장**

  ```python
  # articles/views.py
  
  from rest_framework import status
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Article
  from .serializers import CommentSerializer
  
  @api_view(['POST'])
  def comment_create(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(article=article)  # 저장
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```

**읽기 전용 필드 설정**

- **read_only_fields** 를 사용해 외래 키 필드를 **읽기 전용 필드**로 설정

- **읽기 전용 필드**는 데이터를 전송하는 시점에 **해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력**하도록 함

  ```python
  # articles/serializers.py
  
  from rest_framework import serializers
  
  from .models import Comment
  
  class CommentSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Comment
          fields = '__all__'
          read_only_fields = ('article',)
  ```

**DELETE & PUT**

- 댓글 데이터 삭제 및 수정 구현하기

  ```python
  # articles/views.py
  
  from rest_framework import status
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Comment
  from .serializers import CommentSerializer
  
  @api_view(['GET', 'DELETE', 'PUT'])
  def comment_detail(request, comment_pk):
      comment = Comment.objects.get(pk=comment_pk)
      if request.method == 'GET':
       serializer = CommentSerializer(comment)
       return Response(serializer.data)
  
      elif request.method == 'DELETE':
          comment.delete()
          return Response({'id': comment_pk}, status=status.HTTP_204_NO_CONTENT)
  
      elif request.method == 'PUT':
          serializer = CommentSerializer(comment, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  
      elif request.method == 'DELETE':
          review.delete()
          msg = f"review {review_pk} is deleted"
          return Response({"delete": msg}, status=status.HTTP_204_NO_CONTENT)
  ```

### N-1 역참조 데이터 조회

**개요**

1. 특정 게시글에 작성된 댓글 목록 출력하기
   - 기존 필드 override
2. 특정 게시글에 작성된 댓글의 개수 출력하기

   - 새로운 필드 추가

3. **특정 게시글에 작성된 댓글 목록 출력하기**

- 기존 필드 override - Article Detail

  - “게시글 조회 시 해당 게시글의 댓글 목록까지 함께 출력하기”
  - Serializer는 기존 필드를 override 하거나 추가적인 필드를 구성할 수 있음

  1. PrimaryKeyRelatedField()

     ```python
     # articles/serializers.py
     
     from rest_framework import serializers
     
     from .models import Article
     
     class ArticleSerializer(serializers.ModelSerializer):
         comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
     
         class Meta:
             model = Article
             fields = '__all__'
     ```

  - **models.py**에서 ForeignKey 클래스의 선택 옵션 **related_name**을 통해 이름 변경 가능

  - 역참조 시 사용하는 model_set manager 매니저 이름을 변경할 수 있음

    - **역참조** 시 생성되는 **comment_set**을 **override** 할 수 있음

  - 작성 후, migration 과정이 필요

  - 선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 생기기도 함

    ```python
    # articles/models.py

    from django.db import models

    class Comment(models.Model):
        article = models.ForeignKey(
            Article, on_delete=models.CASCADE, related_name='comments')
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

    class Movie(models.Model):
        actors = models.ManyToManyField(Actor, related_name='movies')

    class Review(models.Model):
        movie = models.ForeignKey(
            Movie, on_delete=models.CASCADE, related_name='review_set')
    ```

  - 작성 후 삭제(다시 원래 코드로 복구)

    - **위와 같이 변경 하면 기존 article.comment_set은 더 이상 사용할 수 없고, article.comments로 대체됨**

  2. Nested relationships

     ```python
     # articles/serializers.py
     
     from rest_framework import serializers
     
     from .models import Article, Comment
     
     # 역참조 할 때 댓글 정보를 보여주기 위해 Commentserializer 위치 이동
     class CommentSerializer(serializers.ModelSerializer):
     
         class Meta:
             model = Comment
             fields = '__all__'
             read_only_fields = ('article',)
     
     class ArticleSerializer(serializers.ModelSerializer):
         comment_set = CommentSerializer(many=True, read_only=True)
      
         class Meta:
             model = Article
             fields = '__all__'
     ```
    
     - 모델 관계 상으로 참조 된 대상은 참조하는 대상의 표현에 포함되거나 nested 중첩 될 수 있음
     - 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현 할 수 있음
     - 두 클래스의 상/하 위치를 변경해야 함

2. **특정 게시글에 작성된 댓글의 개수 출력하기**

- 새로운 필드 추가 - Article Detail

  - “게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력하기”

    ```python
    # articles/serializers.py
    
    from rest_framework import serializers
    
    from .models import Article

    # detail 한 내용을 보여주는 serializer 사용
    # 생성, 수정을 할 때 모든 필드의 유효성 검사를 위해 사용
    class ArticleSerializer(serializers.ModelSerializer):
        # related manager 이름을 필드명으로 작성
        comment_set = CommentSerializer(many=True, read_only=True)
        # 추가 필드명은 사용자 정의
        comment_count = serializers.IntegerField(
            source='comment_set.count', read_only=True)
    
        class Meta:
            model = Article
            fields = '__all__'
    ```

  - **source**

    - serializers field’s argument
    - 필드를 채우는 데 사용할 속성의 이름
    - dotted notation 점 표기법을 사용하여 속성을 탐색 할 수 있음

**[주의] 읽기 전용 필드 지정 이슈**

- 특정 필드를 override 혹은 추가한 경우 **read_only_fields**가 동작하지 않으니 주의

### Django shortcuts functions

**개요**

- **django.shortcuts** 패키지는 개발에 도움 될 수 있는 여러 함수와 클래스를 제공

- 제공되는 shortcuts 목록

  - render(), redirect(), **get_object_or_404()**, **get_list_or_404()**

    > <https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/>

**get_object_or_404()**

- 모델 manager objects에서 `get()`을 호출하지만, 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise 함

  ```python
  # articles/views.py
  
  from django.shortcuts import get_object_or_404
  
  article = get_object_or_404(Article, pk=article_pk)
  comment = get_object_or_404(Comment, pk=comment_pk)
  ```

**get_list_or_404()**

- 모델 manager objects에서 `all()`, `filter()`의 결과를 반환하고 해당 객체 목록이 없을 땐 Http404를 raise 함

  ```python
  # articles/views.py
  
  from django.shortcuts import get_list_or_404
  
  article = get_list_or_404(Article)
  comment = get_list_or_404(Comment)
  ```

**왜 사용해야 할까?**

- 클라이언트 입장에서 “서버에 오류가 발생하여 요청을 수행할 수 없다(500)”라는 원인이 정확하지 않은 에러를 마주하기 보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소

## finish

- REST API
- Response JSON
- Django REST framework - Single Model
- Django REST framework - N:1 Relation0
