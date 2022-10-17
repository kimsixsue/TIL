[Django Static Media](#django-static-media)

1. [Managing static files](#1-managing-static-files)

   + [Static files](#static-files)

   + [Static files organization](#static-files-organization)

   + [Static files Use](#static-files-use)

2. [Image Upload](#2-image-upload)

   + [ImageField](#imagefield)

   + [CREATE](#create)

   + [READ](#read)

   + [UPDATE](#update)

   + [upload_to argument](#upload_to-argument)

3. [Image Resizing](#3-image-resizing)

4. [QuerySet API Advanced](#4-queryset-api-advanced)

   + [CRUD basics](#crud-basics)

   + [Sorting data](#sorting-data)

   + [Filtering data](#filtering-data)

   + [Aggregation(Grouping data)](#aggregationgrouping-data)

* [finish](#finish)

# Django Static Media

## 1. Managing static files

개발자가 서버에 미리 준비한 혹은 사용자가 업로드한 정적파일을 클라이언트에게 제공하는 방법

### Static files

**정적 파일**

- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  - 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일
- **파일 자체가 고정**되어 있고, 서비스 중에도 추가되거나 **변경되지 않고 고정** 되어 있음
  - 이미지, 자바 스크립트 또는 CSS와 같은 미리 준비된 추가 파일
- Django에서는 이러한 파일들을 “static file”이라 함
  - Django는 staticfiles 앱을 통해 정적 파일과 관련 된 기능을 제공

**Media File**

- 미디어 파일
- user-uploaded 사용자가 웹에서 업로드하는 정적 파일
- 유저가 업로드 한 모든 정적 파일

**웹 서버와 정적 파일**

- 웹 서버의 기본동작은
  - URL 특정 위치에 있는 자원을 HTTP request 요청 받아서
  - HTTP response 응답을 처리하고 serving 제공하는 것

- 이는 “자원과 자원에 접근 가능한 주소가 있다.”라는 의미
  - 파일은 자원이고 해당 **파일을 얻기 위한 경로인 URL 웹 주소가 존재**함
- 웹 서버는 요청받은 URL로 서버에 존재하는 static resource 정적 자원

### Static files organization

**Django에서 정적파일을 구성하고 사용하기 위한 몇가지 단계**

1. INSTALLED_APPS에 django.contrib.staticfiles가 포함되어 있는지 확인하기

2. settings.py에서 **STATIC_URL**을 정의하기

3. 앱의 static 폴더에 정적 파일을 위치하기

   - app_dir/**static**/sample_img.jpg

4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

   ```django
   {% load static %}
   
   <img src="{% static 'sample_img.jpg' %}" alt="sample image">
   ```

**Django template tag**

```django
{% load %}
```

- load tag
- 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드

```django
{% static '경로' %}
```

- static tag
- STATIC_ROOT 에 저장된 정적 파일에 연결

**Static files 관련 Core Settings**

1. STATIC_ROOT

   - Default: None
   - Django 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아 넣는 경로
   - **collectstatic** 이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
   - **개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음**
   - 실 서비스 환경(배포 환경)에서 Django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위해 사용
   - 배포 환경에서는 Django를 직접 실행하는 것이 아니라, 다른 서버에 의해 실행되기 때문에 실행하는 다른 서버는 Django에 내장되어 있는 정적 파일들을 인식하지 못 함 (내장되어 있는 정적 파일들을 밖으로 꺼내는 이유)

2. STATICFILES_DIRS

   - Dafault: [] (Empty list)

   - **app/static/** 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트

   - 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

     ```python
     STATICFILES_DIRS = [
         BASE_DIR / 'static',
     ]
     ```

3. STATIC_URL

   - Default: None

   - STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL

   - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로 (기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색

   - **실제 파일이나 디렉토리가 아니며, URL로만 존재** 

   - 비어 있지 않은 값으로 설정 한다면 반드시 slash(/) 로 끝나야 함

     ```python
     STATIC_URL = '/static/'
     ```

### Static files Use

**static file 가져오기**

- Static file을 가져오는 2가지 방법

  1. 기본 경로에 있는 static file 가져오기

     1. articles/static/articles 경로에 이미지 파일 배치하기

     2. static tag를 사용해 이미지 파일 출력하기

        ```django
        {% extends 'base.html' %}
        {% load static %}
        
        {% block content %}
          <img src="{% static 'articles/sample_img_1.png' %}" alt="sample-img">
        ```

  2. 추가 경로에 있는 static file 가져오기

     1. 추가 경로 작성

        ```python
        STATICFILES_DIRS = [
            BASE_DIR / 'static',
        ]
        ```

     2. static/ 경로에 이미지 파일 배치하기

     3. static tag를 사용해 이미지 파일 출력하기

        ```django
        {% extends 'base.html' %}
        {% load static %}
        
        {% block content %}
          <img src="{% static 'sample_img_2.png' %}" alt="sample-img">
        ```

**STATIC_URL 확인하기**

- Django가 해당 이미지를 클라이언트에게 응답하기 위해 만든 image url 확인하기
  - 개발자도구 - Inspect 버튼을 통해 확인
- “**STATIC_URL + static file 경로**”로 설정됨
  - http://127.0.0.1:8000/`static`/articles/sample_img_1.png

## 2. Image Upload

Django ImageField를 사용해 사용자가 업로드한 정적 파일(미디어 파일) 관리하기

### ImageField

**ImageField()**

- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능
- 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
- ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하며 최대 길이를 변경할 수 있음

**FileField()**

- FiledField(max_length=100, upload_to=‘’, storage=None, **options)

- 파일 업로드에 사용하는 모델 필드

- 2개의 선택 인자를 가지고 있음
  
  1. upload_to
  
     >https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.FileField.upload_to
  
  2. storage

**FileField / ImageField를 사용하기 위한 단계**

1. settings.py에 **MEDIA_ROOT**, **MEDIA_URL** 설정
2. **upload_to** 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정 (선택사항)

**MEDIA_ROOT**

- Default: ‘’ (Empty string)

- 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로

- Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음

  - 데이터베이스에 저장되는 것은 “**파일 경로**”

- MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함

  ```python
  # settings.py
  
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

**MEDIA_URL**

- Default: ‘’ (Empty string)

- MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL

- 업로드 된 파일의 URL 주소를 만들어 주는 역할

  - 웹 서버 사용자가 사용하는 public URL

- 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

- MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야 함

  ```python
  # settings.py
  
  MDIA_URL = '/media/'
  ```

**개발 단계에서 사용자가 업로드한 미디어 파일 제공하기**

```python
# crud/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # the rest of your URLconf goes here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- 사용자로부터 업로드 된 파일이 프로젝트에 업로드 되고 나서, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함
  - 업로드 된 파일의 URL == settings.MEDIA_URL
  - 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT

### CREATE

**ImageField 작성**

- 기존 컬럼 사이에 작성해도 실제 테이블에 추가 될 때는 가장 우측(뒤)에 추가됨

```python
# articles/models.py

class Article(models.Model):
    image = models.imageField(blank=True)
```

**Model field option**

- Model field option 중 아래 2가지 사항 알아보기
  1. blank
  2. null

**blank**

- Default : False
- True인 경우 필드를 비워 둘 수 있음
  - 이럴 경우 DB에는 ‘’(빈 문자열)이 저장됨
- is_valid 유효성 검사에서 사용 됨
  - “Validation-related”
  - 필드에 blank=True가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있음

**null**

- Default: False
- True인 경우 Django는 빈 값을 DB에 NULL로 저장함
  - “Database-related”

**null 관련 주의사항**

- “**CharField, TextField와 같은 문자열 기반 필드에는 null 옵션 사용을 피해야 함**”
  - 문자열 기반 필드에 null=True 로 설정 시 데이터 없음에 대한 표현에 “빈 문자열”과 “NULL” 2가지 모두 가능하게 됨
  - “데이터 없음”에 대한 표현에 두 개의 가능한 값을 갖는 것은 좋지 않음
  - Django는 문자열 기반 필드에서 NULL이 아닌 빈 문자열을 사용하는 것이 규칙

**Migrations**

- ImageField를 사용하려면 반드시 Pillow 라이브러리가 필요
  - Pillow 설치 없이는 makemigrations 실행 불가

**ArticleForm에서 image 필드 출력 확인**

- 파일 또는 이미지 업로드 시에는 form 태그에 enctype 속성

  ```django
  <!-- articles/create.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
    </form>
  ```

**request.FILES**

- 파일 및 이미지는 request의 POST 속성 값으로 넘어가지 않고 FILES 속성 값에 담겨 넘어감

  ```python
  # articles/views.py
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES)
  ```


**이미지 첨부하기**

- 이미지를 첨부해서 한번, 첨부하지 않고 한번 게시글 작성해보기
- 이미지를 첨부하지 않으면 blank=True 속성으로 인해 빈 문자열이 저장되고, 이미지를 첨부한 경우는 MEDIA_ROOT 경로에 이미지가 업로드 됨
  - **파일 자체가 아닌 “경로”가 저장 된다는 것을 잊지 말 것**
- 만약 같은 이름의 파일을 업로드 한다면 Django는 파일 이름 끝에 임의의 난수 값을 붙여 저장함

### READ

**업로드 이미지 출력하기**

- 업로드 된 파일의 상대 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}">
  ```

- article.image.url - 업로드 파일의 경로

- article.image - 업로드 파일의 파일 이름

- 이미지를 업로드하지 않은 게시물은 detail 템플릿을 출력할 수 없는 문제 해결하기

  - 이미지 데이터가 있는 경우만 이미지 출력할 수 있도록 처리

    ```django
    <!-- articles/detail.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
      {% if article.image %}
        <img src="{{ article.image.url }}" alt="{{ article.image }}">
      {% endif %}
    ```

### UPDATE

- 이미지는 바이너리 데이터이기 때문에 텍스트처럼 일부만 수정 하는 것은 불가능

- 때문에 새로운 사진으로 대체하는 방식을 사용

**업로드 이미지 수정하기**

- enctype 속성값 추가

  ```django
  <!-- articles/update.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
    </form>
  ```

- 이미지 파일이 담겨있는 request.FILES 추가 작성

  ```python
  # articles/views.py
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      if request.user == article.user:
          if request.method == 'POST':
              form = ArticleForm(request.POST, request.FILES, instance=article)
  ```

### upload_to argument

**사용자 지정 업로드 경로와 파일 이름 설정하기**

- ImageField는 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법을 제공

  1. 문자열 값이나 경로 지정 방법

     - upload_to 인자에 새로운 이미지 저장 경로를 추가 후 migration 과정 진행

       ```python
       # articles/models.py
       
       class Article(models.Model):
           image = models.ImageField(blank=True, upload_to='images/ ' )
       ```

       ```bash
       $ python manage.py makemigrations
       $ python manage.py migrate
       ```

     - MEDIA_ROOT 이후 경로가 추가 되는 것

     - 단순 문자열 뿐만 아니라 파이썬 time 모듈의 strftime() 형식도 포함될 수 있으며, 이는 파일 업로드 날짜/시간으로 대체 됨

       ```python
       # articles/models.py
       
       class Article(models.Model):
           image = models.ImageField(blank=True, upload_to='%Y/%m/%d/ ' )
       ```

       ```bash
       $ python manage.py makemigrations
       $ python manage.py migrate
       ```

  2. 함수 호출 방법

     - upload_to는 독특하게 함수처럼 호출이 가능하며 해당 함수가 호출되면서 반드시 2개의 인자를 받음

       ```python
       # articles/models.py
       
       def articles_image_path(instance, filename):
           return f'images/{instance.user.username}/{filename}'
       
       class Article(models.Model):
           image = models.ImageField(blank=True, upload_to=articles_image_path)
       ```

     1. instance

        - FileField가 정의된 모델의 인스턴스
        - 대부분 이 객체는 아직 데이터베이스에 저장되기 전이므로 아직 PK 값이 없을 수 있으니 주의

     2. filename

        - 기존 파일 이름

        ```bash
        $ python manage.py makemigrations
        $ python manage.py migrate
        ```

## 3. Image Resizing

- 실제 원본 이미지를 서버에 그대로 로드 하는 것은 여러 이유로 부담이 큼
- HTML `<img>` 태그에서 직접 사이즈를 조정할 수도 있지만, 업로드 될 때 이미지 자체를 resizing 하는 것을 사용해 볼 것

**사전 준비**

- django-imagekit 모듈 설치 및 등록

  ```bash
  $ pip install django-imagekit
  $ pip freeze > requirements.txt
  ```

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      'imagekit',
  ]
  ```

**썸네일 만들기**

- 2가지 방식으로 썸네일 만들기를 진행

  1. 원본 이미지 저장 X

     - **ProcessedImageField()의 parameter로 작성된 값들은 makemigrations 후에 변경이 되더라도 다시 makemigrations 를 해줄 필요없이 즉시 반영 됨**

     ```python
     # articles/models.py
     
     from imagekit.processors import Thumbnail
     from imagekit.models import ProcessedImageField
     
     class Article(models.Model):
         image = ProcessedImageField(
             blank=True,
             uploadt_to='thumbnails/',
             processors=[Thumbnail(200,300)],
             format='JPEG',
             options={'quality': 80},
         )
     ```

     ```bash
     $ python manage.py makemigrations
     $ python manage.py migrate
     ```

  2. 원본 이미지 저장 O

     ```python
     # articles/models.py
     
     from imagekit.processors import Thumbnail
     from imagekit.models import ProcessedImageField, ImageSpecField
     from django.db import models
     from django.confg import settings
     
     class Article(models.Model):
         image = models.ImageField(blank=True)
         image_thumbnail = ImageSpecField(
             source='image',
             processors=[Thumbnail(200,300)],
             format='JPEG',
             options={'quality': 80},
         )
     ```

     ```bash
     $ python manage.py makemigrations
     $ python manage.py migrate
     ```

     - 기본적으로 원본 이미지가 업로드 되고 출력됨

     ```django
     <!-- articles/detail.html -->
     
     {% extends 'base.html' %}
     
     {% block content %}
       {% if article. image %}
         <img src="{{ article.image.url }}" alt=="{{ article.image }}">
         <img src="{{ article.image_thumbnail.url }}" alt=="{{ article.image_thumbnail }}">
       {% endif %}
     ```

     - 썸네일이 사용되었을 때만 resizing한 이미지를 생성

## 4. QuerySet API Advanced

**사전 준비**

1. 가상 환경 생성 및 활성화

2. 패키지 목록 설치

3. migrate 진행

   ```bash
   $ python manage.py migrate
   ```

4. sqlite3에서 csv 데이터 import 하기

   ```bash
   $ sqlite3 db.sqlite3
   ```

   ```sql
   sqlite > .mode csv
   sqlite > .import users.csv users_user
   sqlite > .exit
   ```

- shell_plus 실행

  ```bash
  $ python manage.py shell_plus
  ```

### CRUD basics

모든 user 레코드 조회

```sql
User.objects.all()
```

user 레코드 생성

```sql
User.objects.create(
    first_name='길동',
    last_name='홍',
    age=100,
    country='제주도',
    phone='010-1234-4567',
    balance=10000,
)
```

101번 user 레코드 조회

```sql
user = User.objects.get(pk=101)
```

101번 user 레코드의 last_name 을 김 으로 수정

```sql
user.last_name = '김'
user.save()
```

101번 user 레코드 삭제

```sql
user.delete()
```

전체 인원 수 조회

```sql
User.objects.count()
```

**.count()**

- QuerySet과 일치하는 데이터베이스의 개체 수를 나타내는 정수를 반환
- .all() 을 사용하지 않아도 됨

### Sorting data

나이가 어린 순으로 이름과 나이 조회하기

```sql
User.objects.order_by('age').values('first_name', 'age')
```

**order_by()**

- .order_by(`*fields`)
- QuerySet의 정렬을 재정의
- 기본적으로 오름차순으로 정렬하며 필드명에 ‘-’ (하이픈) 을 작성하면 내림차순으로 정렬
- 인자로 ‘?’ 를 입력하면 랜덤으로 정렬

**values()**

- .values(`*fields`, `**expressions`)
- 모델 인스턴스가 아닌 딕셔너리 요소들을 가진 QuerySet을 반환
- `*fields`는 선택인자이며 조회하고자 하는 필드명을 가변인자로 입력 받음
  - 필드를 지정하면 각 딕셔너리에는 지정한 필드에 대한 key와 value만을 출력
  - 입력하지 않을 경우 각 딕셔너리에는 레코드의 모든 필드에 대한 key와 value를 출력

이름과 나이를 나이가 많은 순서대로 조회하기

```sql
User.objects.order_by('-age').values('first_name', 'age')
```

이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기

```sql
User.objects.order_by('age', '-balance').values('first_name', 'age', 'balance')
```

### Filtering data

중복없이 모든 지역 조회하기

```sql
User.objects.distinct().values('country')
```

지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기

```sql
User.objects.distinct().values('country').order_by('country')
```

이름과 지역이 중복 없이 모든 이름과 지역 조회하기

```sql
User.objects.distinct().values('first_name', 'country')
```

이름과 지역이 중복 없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회하기

```sql
User.objects.distinct().values('first_name', 'country').order_by('country')
```

나이가 30인 사람들의 이름 조회

```sql
User.ojbects.filter(age=30).values('first_name')
```

나이가 30살 이상인 사람들의 이름과 나이 조회하기

```sql
User.ojbects.filter(age__gte=30).values('first_name')
```

**Field lookups**

- SQL WHERE 절의 상세한 조건을 지정하는 방법

- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 사용됨

- 문법 규칙

  - 필드명 뒤에 “double_underscore” 이후 작성함

    ```sql
    field__lookuptype=value
    ```

  
  > https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups

나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기

```sql
User.objects.filter(age__gte=30, balance__gt=500000).values('first_name', 'age', 'balance')
```

이름에 ‘호’가 포함되는 사람들의 이름과 성 조회하기

```sql
User.objects.filter(first_name__contains='호').values('first_name', 'last_name')
```

핸드폰 번호가 011로 시작하는 사람들의 이름과 핸드폰 번호 조회

```sql
User.objects.filter(phone__startswith='011-').values('first_name', 'phone')
```

- SQL에서의 ‘%’ 와일드 카드와 같음
- under score `_` 는 별도로 정규 표현식을 사용해야 함

이름이 ‘준’으로 끝나는 사람들의 이름 조회하기

```sql
User.objects.filter(first_name__endswith='준').values('first_name')
```

경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기

```sql
User.objects.filter(country__in=['경기도', '강원도']).values('first_name', 'country')
```

경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기

```sql
User.objects.exclude(country__in=['경기도', '강원도']).values('first_name', 'country')
```

**exclude()**

- exclude(`**kwargs`)
- 주어진 매개변수와 일치하지 않는 객체를 포함하는 QuerySet 반환

나이가 가장 어린 10명의 이름과 나이 조회하기

```sql
User.objects.order_by('age').values('first_name', 'age')[:10]
```

나이가 30이거나 성이 김씨인 사람들 조회

```python
from django.db.models import Q

User.objects.filter(Q(age=30) | Q(last_name='김')
```

**‘Q’ object**

- 기본적으로 filter()와 같은 메서드의 키워드 인자는 AND statement를 따름

- 만약 더 복잡한 쿼리를 실행해야 하는 경우가 있다면 Q 객체가 필요함

  ```python
  from django.db.models import Q
  
  Q(question__startswith='What')
  ```

- ‘&’ 및 ‘|’를 사용하여 Q 객체를 결합할 수 있음

  ```sql
  Q(question__startswith='Who') | Q(question__startswith='What')
  ```

- 조회를 하면서 여러 Q 객체를 제공할 수도 있음

  ```sql
  Article.objects.get(
      Q(title__startswith='Who'),
      Q(created_at=date(2005, 5, 2)) | Q(created_at=date(2005, 5, 6))
  )
  ```

### Aggregation(Grouping data)

**aggregate()**

- “Aggregate calculates values for the **entire** queryset.”
- 전체 queryset에 대한 값을 계산
- 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용
- 딕셔너리를 반환
- Aggregation functions
  - Avg, Count, Max, Min, Sum 등

나이가 30살 이상인 사람들의 평균 나이 조회하기

```python
from django.db.models import Avg

User.objects.filter(age__gte=30).aggregate(Avg('age'))
# 딕셔너리 key 이름을 수정할 수도 있다.
User.objects.filter(age__gte=30).aggregate(avg_value=Avg('age'))
```

가장 높은 계좌 잔액 조회하기

```python
from django.db.models import Max

User.objects.aggregate(Max('balance'))
```

모든 계좌 잔액 총액 조회하기

```python
from django.db.models import Sum

User.objects.aggregate(Sum('balance'))
```

**annotate()**

- 쿼리의 각 항목에 대한 요약 값을 계산
- SQL의 **GROUP BY**에 해당
- ‘주석을 달다’ 라는 사전적 의미를 가지고 있음

각 성씨가 몇 명씩 있는지 조회하기

```python
from django.db.models import Count

User.objects.values('last_name').annotate(Count('last_name'))
```

각 지역별로 몇 명씩 살고 있는지 조회하기

```python
from django.db.models import Count

User.objects.values('country').annotate(Count('country'))
# 딕셔너리의 key 값을 변경할 수 있다.
User.objects.values('country').annotate(num_of_country=Count('country'))
```

각 지역별로 몇 명씩 살고 있는지  + 지역별 계좌 잔액 평균 조회하기

- 한번에 여러 값을 계산해 조회할 수 있음

  ```sql
  User.objects.values('country').annotate(
      Count('country'), 
      avg_balance=Avg('balance')
  )
  ```

**N : 1 예시**

- 만약 Comment - Article 관계가 N : 1 인 경우 다음과 같은 참조도 가능

  ```sql
  Article.objects.annotate(
      number_of_comment=Count('comment'),
      pub_date=Count('comment', filter=Q(comment__created_at__lte='2000-01-01'))
  )
  ```

- Article.objects.all() 전체 게시글을 조회하면서, annotate로 number_of_comment 각 게시글의 댓글 개수와 2000-01-01보다 나중에 pub_date 작성된 댓글의 개수를 함께 조회하는 것

## finish

- Managing static files
- Image Upload
- Image Resizing
- QuerySet API Advanced
