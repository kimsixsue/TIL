[DB relationship N-1](#db-relationship-n-1)

1. [A many-to-one relationship](#1-a-many-to-one-relationship)

   + [Intro](#intro)

   + [Foreign Key](#foreign-key)

2. [N-1 (Comment - Article)](#2-n-1--comment---article-)

   + [Django Relationship fields](#django-relationship-fields)

   + [Comment Model](#comment-model)

   + [Related manager](#related-manager)

   + [Comment 1](#comment-1)

   + [Comment 2](#comment-2)

3. [N-1 (Article - User)](#3-n-1--article---user-)

   + [Referencing the User model](#referencing-the-user-model)

   + [model relationship](#model-relationship)

   + [CREATE](#create)

   + [DELETE](#delete)

   + [UPDATE](#update)

   + [READ](#read)

4. [N-1 (Comment - User)](#4-n-1--comment---user-)

   + [model relationship](#model-relationship-1)

   + [CREATE](#create-1)

   + [READ](#read-1)

   + [DELETE](#delete-1)

   + [is_authenticated](#is-authenticated)

# DB relationship N-1

## 1. A many-to-one relationship

- 관계형 데이터베이스에서의 외래 키 속성을 사용해 모델간 N:1 관계 설정하기

### Intro

**RDB(관계형 데이터베이스)**

- 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
- RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, **외래 키**를 사용하여 각 행에서 서로 다른 테이블 간의 **관계**를 만드는 데 사용할 수 있음

**RDB에서의 관계**

1. 1:1
   - One-to-one relationships
   - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
2. **N:1**
   - Many-to-one relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
   - 기준 테이블에 따라(1:N, One-to-many relationships)이라고도 함
3. M:N
   - Many-to-many relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
   - 양쪽 모두에서 N:1 관계를 가짐

### Foreign Key

**개념**

- 외래 키(외부 키)
- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 1개의 키에 해당하고, 이는 참조되는 측 테이블의 Primary Key 기본 키를 가리킴
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨
  - 이 때문에 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음

**특징**

- 키를 사용하여 부모 테이블의 유일한 값을 참조 (by 참조 무결성)
- 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함

## 2. N-1 (Comment - Article)

- Comment(N) - Article(1)
  - Comment 모델과 Article 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 게시글에 작성 될 수 있음”

### Django Relationship fields

**Django Relationship fields 종류**

1. OneToOneField()
   - A one-to-one relationship
2. **ForeignKey()**
   - A many-to-one relationship
3. ManyToManyField()
   - A many-to-many relationship

**`ForeignKey`(`to`, `on_delete`, `**options`)**

- A many-to-one relationship을 담당하는 Django의 모델 필드 클래스

- Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당

- 2개의 필수 위치 인자가 필요

  1. 참조하는 **model class**
     - 어떤 모델 클래스와 관계를 가질건지 (부모 클래스)
  2. **on_delete** 옵션

  > https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey

### Comment Model

**Comment 모델 정의**

```python
# articles/models.py

from django.db import models

class Comment(models.Model):  # 댓글 N:1 글
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content    
```

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스의 단수형(소문자)으로 작성하는 것을 권장

**ForeignKey arguments - `on_delete`**

- 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의
- 데이터 무결성을 위해서 매우 중요한 설정
- on_delete 옵션 값
  - **CASCADE** : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
  - PROTECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들이 존재

**Migration 과정 진행**

- models.py에서 모델에 대한 수정사항이 발생했기 때문에 migration 과정을 진행

  ```bash
  $ python manage.py makemigrations
  ```

- 마이그레이션 파일 **0002_comment.py** 생성 확인

- migrate 진행

  ```bash
  $ python manage.py migrate
  ```

- migrate 후 Comment 모델 클래스로 인해 생성된 테이블 확인
- ForeignKey 모델 필드로 인해 작성된 컬럼의 이름이 **article_id**인 것을 확인
- 만약 ForeignKey 인스턴스를 article이 아닌 abcd로 생성 했다면 abcd_id로 만들어짐
  - 이처럼 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장 되었던 이유

**댓글 생성 연습하기**

- shell_plus 실행

  ```bash
  $ python manage.py shell_plus
  ```

1. 댓글 생성

   ```bash
   # Comment 클래스의 인스턴스 comment 생성
   comment = Comment()
   
   # 인스턴스 변수 저장
   comment.content = 'first comment'
   
   # DB에 댓글 저장
   comment.save()
   
   # 에러 발생
   django.db.utils.IntegrityError: NOT NULL constraint failed: articles_comment.article_id
   # articles_comment 테이블의 ForeignKeyField, article_id 값이 저장시 누락되었기 때문
   
   # 게시글 생성 및 확인
   article = Article.objects.create(title='title', content='content')
   article
   => <article: title>
   
   # 외래 키 데이터 입력
   # 다음과 같이 article 객체 자체를 넣을 수 있음
   comment.article = article
   
   # DB에 댓글 저장 및 확인
   comment.save()
   comemnt
   => <Comment: first comment>
   ```

2.  댓글 속성 값 확인

   ```bash
   comment.pk
   => 1
   
   comment.content
   => 'first comment'
   
   # 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음
   comment.article
   => <Article: title>
   
   # article_pk는 존재하지 않는 필드이기 때문에 사용 불가
   comment.article_id
   => 1	
   ```

3. comment 인스턴스를 통한 article 값 접근하기

   ```bash
   # 1번 댓글이 작성된 게시물의 pk 조회
   comment.article.pk
   => 1
   
   # 1번 댓글이 작성된 게시물의 content 조회
   comment.article.content
   => 'content'
   ```

4. 두번째 댓글 작성해보기

   ```bash
   comment = Comment(content='second comment', article=article)
   comment.save()
   
   comment.pk
   => 2
   
   comment
   => <Comment: second comment>
   
   comment.article_id
   => 1
   ```

### Related manager

**관계 모델 참조**

- Related manager는 N:1 혹은 M:N 관계에서 사용 가능한 context 문맥

- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 **역참조**할 때에 사용할 수 있는 manager를 생성

  - 모델 생성 시 **object**라는 매니저를 통해 queryset api를 사용했던 것처럼, related manager를 통해 queryset api를 사용할 수 있게 됨

  > https://docs.djangoproject.com/en/3.2/ref/models/relations/

**역참조**

- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
- 즉, 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
- N:1 관계에서는 1이 N을 참조하는 상황
  - 외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조 (글 : 댓글)

```python
article.comment_set.method()
```

- Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저
- article. comment 형식으로는 댓글 객체를 참조할 수 없음
  - 실제로 Article 클래스에는 Comment 모델과의 어떠한 관계도 작성되어 있지 않음
- 대신 Django가 역참조 할 수 있는 **comment_set** manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음
  - **N:1 관계에서 생성되는 Related manager의 이름은 참조하는 “모델명_set” 이름 규칙으로 만들어짐**
- 반면 참조 상황(Comment -> Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능

**Related manager 연습하기**

- shell_plus 실행

  ```bash
  $ python manage.py shell_plus
  ```

1. 1번 게시글 조회하기

   ```bash
   article = Article.objects.get(pk=1)
   ```

2. dir() 함수를 사용해 클래스 객체가 사용할 수 있는 메서드를 확인하기

   ```bash
   dir(article)
   
   [
    ...중략...
    'comment_set',
    ...중략
   ]
   ```

3. 1번 게시글에 작성된 모든 댓글 조회하기 (역참조)

   ```bash
   article.comment_set.all()
   => <QuerySet [<Comment: first comment>, <Comment: second comment>]>
   ```

4. 1번 게시글에 작성된 모든 댓글 출력하기

   ```python
   comments = article.comment_set.all()
   
   for comment in comments:
       print(comment.content)
   ```

**ForeignKey arguments - `related_name`**

```python
# articles/models.py

from django.db import models

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
```

- ForeignKey 클래스의 선택 옵션
- 역참조 시 사용하는 model_set manager 매니저 이름을 변경할 수 있음
- 작성 후, migration 과정이 필요
- 선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 생기기도 함
- 작성 후 다시 원래 코드로 복구
  - **위와 같이 변경 하면 기존 article.comment_set은 더 이상 사용할 수 없고, article.comments로 대체됨**

**admin site 등록**

- 새로 작성한 Comment 모델을 admin site에 등록하기

  ```python
  # articles/admin.py
  
  from django.contrib import admin
  from .models import Article, Comment
  
  admin.site.register(Article)
  admin.site.register(Comment)
  ```

### Comment 1

**CREATE**

- 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성

  ```python
  # articles/forms.py
  
  from django import forms
  from .models import Comment
  
  class CommentForm(forms.ModelForm):
      
      class Meta:
          model = Comment
          fields = '__all__'
  ```

- detail 페이지에서 CommentForm 출력 (view 함수)

  ```python
  # articles/views.py
  
  from .models import Article
  from .forms import CommentForm
  
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm()
      context = {
          'article': article,
          'comment_form': comment_form,
      }
      return render(request, 'articles/detail.html', context)
  ```

  - **기존에 ArticleForm 클래스의 인스턴스명을 form으로 작성했기 때문에 헷갈리지 않도록 comment_form으로 작성**

- detail 페이지에서 CommentForm 출력 (템플릿)

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <a href="{% url 'articles:index' %}">back</a>
    <hr>
    <form action="#" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  {% endblock content %}
  ```

- detail 페이지에 출력된 CommentForm

- 실 서비스에서는 댓글을 작성할 때 댓글을 어떤 게시글에 작성하는지 직접 게시글 번호를 선택하지 않음

- 실제로는 해당 게시글에 댓글을 작성하면 자연스럽게 그 게시글에 댓글이 작성되어야 함

- 다음과 같이 출력되는 이유는 Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요하기 때문에 출력 되고 있는 것

- 하지만, 외래 키 필드는 **사용자의 입력으로 받는 것이 아니라 view 함수 내에서 받아 별도로 처리되어 저장**되어야 함

- 외래 키 필드를 출력에서 제외 후 확인

  ```python
  # articles/forms.py
  
  from django import forms
  from .models import Comment
  
  class CommentForm(forms.ModelForm):
      
      class Meta:
          model = Comment
          fields = ('article',)
  ```

- 출력에서 제외된 외래 키 데이터는 어디서 받아와야 할까?

- detail 페이지의 url을 살펴보면 path(‘`<int:pk>`/’, views.detail, name=‘detail’) url에 해당 게시글의 pk 값이 사용되고 있음

- 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값

- url을 통해 변수를 넘기는 **variable routing**을 사용

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('<int:pk>/comments/', views.comments_create, name='comments_create'),
  ]
  ```

  ```python
  # articles/views.py
  
  from .models import Article
  from .forms import CommentForm
  
  def comments_create(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          # article 객체는 언제 저장할 수 있을까?
          comment_form.save()
      return redirect('articles:detail', article.pk)
  ```

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  {% endblock content %}
  ```

- 작성을 마치고 보면 article 객체 저장이 이루어질 타이밍이 보이지 않음

- 그래서 save() 메서드는 데이터베이스에 저장하기 전에 객체에 대한 추가적인 작업을 진행할 수 있도록 인스턴스만을 반환해주는 옵션 값을 제공

**The `save()` method**

- save(commit=False)

  - “Create, but don’t save the new instance.”
  - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
  - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용

  > https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method

- save 메서드의 commit 옵션을 사용해 DB에 저장되기 전 article 객체 저장하기

  ```python
  # articles/views.py
  
  from .models import Article
  from .forms import CommentForm
  
  def comments_create(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.article = article
          comment_form.save()
      return redirect('articles:detail', article.pk)
  ```

**READ**

- 작성한 댓글 목록 출력하기

- 특정 article에 있는 모든 댓글을 가져온 후 context에 추가

  ```python
  # articles/views.py
  
  from .models import Article
  from .forms import CommentForm
  
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm()
      comments = article.comment_set.all()
      context = {
          'article': article,
          'comment_form': comment_form,
          'comments': comments,
      }
      return render(request, 'articles/detail.html', context)
  ```

- detail 템플릿에서 댓글 목록 출력하기

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <a href="{% url 'articles:index' %}">back</a>
    <hr>
    <h4>댓글 목록</h4>
    <ul>
      {% for comment in comments %}
        <li>{{ comment.content }}</li>
      {% endfor %}
    </ul>
    <hr>
  {% endblock content %}
  ```

**DELETE**

- 댓글 삭제 구현하기 (url, view)

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
  ]
  ```

  ```python
  # articles/views.py
  
  from .models import Comment
  
  def comments_delete(request, article_pk, comment_pk):
      comment = Comment.objects.get(pk=comment_pk)
      comment.delete()
      return redirect('articles:detail', article_pk)
  ```

- 댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력 될 수 있도록 함

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h4>댓글 목록</h4>
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE">
          </form>
        </li>
      {% endfor %}
    </ul>
    <hr>
  {% endblock content %}
  ```

**댓글 수정을 지금 구현하지 않는 이유**

- 댓글 수정도 게시글 수정과 마찬가지로 구현이 가능
  - 게시글 수정 페이지가 필요했던 것처럼 댓글 수정 페이지가 필요하게 됨
- 하지만 일반적으로 댓글 수정은 수정 페이지로 이동 없이 현재 페이지가 유지된 상태로 댓글 작성 Form 부분만 변경되어 수정 할 수 있도록 함
- 이처럼 페이지의 일부 내용만 업데이트 하는 것은 JavaScript의 영익

### Comment 2

- 댓글에 관련된 아래 2가지 사항을 작성하면서 마무리하기
  1. 댓글 개수 출력하기
     1. DTL filter - **length** 사용
     2. Queryset API - **count()** 사용
  2. 댓글이 없는 겨우 대체 컨텐츠 출력하기

**댓글 개수 출력하기**

1. DTL filter - **length** 사용

   ```django
   {{ comments|length }}
   
   {{ article.comment_set.all|length }}
   ```

2. Queryset API - **count()** 사용

   ```django
   {{ comments.count }}
   
   {{ article.comment_set.count }}
   ```

- detail 템플릿에 작성하기

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h4>댓글 목록</h4>
    {% if comments %}
      <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
    {% endif %}
  {% endblock content %}
  ```

**댓글이 없는 경우 대체 컨텐츠 출력하기**

- DTL **for empty** 활용하기

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      </li>
      {% empty %}
        <p>댓글이 없어요..</p>
    {% endfor %}
  {% endblock content %}
  ```

## 3. N-1 (Article - User)

- Article(N) - User(1)
- Article 모델과 User 모델 간 관계 설정
- “0개 이상의 게시글은 1개의 회원에 의해 작성 될 수 있음”

### Referencing the User model

**Django에서 User 모델을 참조하는 방법**

1. settings.AUTH_USER_MODEL
   - 반환 값 : ‘accounts.User’ (문자열)
   - User 모델에 대한 외래 키 또는 M:N 관계를 정의 할 때 사용
   - **models.py의 모델 필드에서 User 모델을 참조할 때 사용**
2. get_user_model()
   - 반환 값 : User Object (객체)
   - 현재 active 활성화된 User 모델을 반환
   - 커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User를 반환
   - **models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용**

**Django에서 User 모델을 참조하는 방법 정리**

- 문자열과 객체를 반환하는 특징과 Django의 내부적인 실행 원리에 관련된 것
- User 모델을 참조할 때
  - models.py에서는 **setting.AUTH_USER_MODEL**
  - 다른 모든 곳에서는 **get_user_model()**

### model relationship

**Article과 User간 모델 관계 설정**

- Article 모델에 User 모델을 참조하는 외래 키 작성

  ```python
  # articles/models.py
  
  from django.db import models
  from django.conf import settings
  
  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ```

**Migration 진행**

- 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정이 필요

  ```bash
  $ python manage.py makemigrations
  You are trying to add a non-nullable field 'user' to article without a default;
  we cannot do that (the database needs something to populate existing rows).
  Please select a fix:
   1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
   2) Quit, and let me add a default in models.py
  Select an option:
  ```

- 첫번째 화면

  - 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
  - 그래서 기본값을 어떻게 작성할 것인지 선택해야 함
  - 1을 입력하고 Enter 진행 (다음 화면에서 직접 기본 값 입력)

  ```bash
  Please enter the default value now, as valid Python
  The datetime and jango.utils.timezone modules are available, 
  so you can do e.g. timezone.now
  Type 'exit' to exit this prompt
  >>>
  ```

- 두번째 화면

  - article의  user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함
  - 마찬가지로 1 입력하고 Enter 진행
  - 그러면 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됨

### CREATE

- 인증된 회원의 게시글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행

**ArticleForm**

- ArticleForm 출력을 확인해보면 create 템플릿에서 불필요한 user 필드가 출력됨
- 사용자로부터 받는 것이 아니라  url의 variable routing을 통해 처리해야 함

- ArticleForm의 출력 필드 수정

  ```python
  # articles/forms.py
  
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
      
      class Meta:
          model = Article
          fields = ('title', 'article',)
  ```

**외래 키 데이터 누락**

- 게시글 작성 시 NOT NULL constraint failed: articles_article.user_id 에러 발생
- “NOT NULL 제약 조건이 실패했다: articles_article 테이블의 user_id 컬럼에서”
- 게시글 작성 시 외래 키에 저장되어야 할 작성자 정보가 누락 되었기 때문

- 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션을 활용

  ```python
  # articles/views.py
  
  from django.shortcuts import redirect
  from django.views.decorators.http import require_http_methods
  from django.contrib.auth.decorators import login_required
  from .forms import ArticleForm
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save(commit=False)
              article.user = request.user
              article.save()
              return redirect('articles:detail', article.pk)
  ```

### DELETE

**게시글 삭제 시 작성자 확인**

- 이제 게시글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제 할 수 있도록 함

  ```python
  # articles/views.py
  
  from django.shortcuts import redirect
  from django.views.decorators.http import require_POST
  from .models import Article
  
  @require_POST
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      if request.user.is_authenticated:
          if request.user == article.user:
              article.delete()
              return redirect('articles:index')
      return redirect('articles:detail', article.pk)
  ```

### UPDATE

**게시글 수정 시 작성자 확인**

- 수정도 마찬가지로 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정 할 수 있도록 함

  ```python
  # articles/view.py
  
  from django.shortcuts import redirect
  from django.views.decorators.http import require_http_methods
  from django.contrib.auth.decorators import login_required
  from .models import Article
  from .forms import ArticleForm
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      if request.user == article.user:
          if request.method == 'POST':
              form = ArticleForm(request.POST, instance=article)
              if form.is_valid():
                  form.save()
                  return redirect('articles:detail', article.pk)
          else:
              form = ArticleForm(instance=article)
      else:
          return redirect('articles:index')
  ```

- 추가로 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 함

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    {% if request.user == article.user %}
      <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
      <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    {% endif %}
  {% endblock content %}
  ```

### READ

**게시글 작성자 출력**

- index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력

  ```django
  <!-- articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    {% for article in articles %}
      <p><b>작성자 : {{ articles.user }}</b></p>
      <p>글 번호 : {{ article.pk }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
      <hr>
    {% endfor %}
  {% endblock content %}
  ```

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3>
    <hr>
    <p><b>작성자 : {{ articles.user }}</b></p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성 시각 : {{ article.created_at }}</p>
    <p>수정 시각 : {{ article.updated_at }}</p>
    <hr>
  {% endblock content %}
  ```

## 4. N-1 (Comment - User)

- Comment(N) - User(1)
  - Comment 모델과 User 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음”

### model relationship

**Comment와 User간 모델 관계 설정**

- Comment 모델에 User 모델을 참조하는 외래 키 작성

  ```python
  # articles/models.py
  
  from django.db import models
  from django.conf import settings
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ```

**Migration 진행**

- 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정이 필요

  ```bash
  $ python manage.py makemigrations
  ```

  ```bash
  You are trying to add a non-nullable field 'user' to article without a default;
  we cannot do that (the database needs something to populate existing rows).
  Please select a fix:
   1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
   2) Quit, and let me add a default in models.py
  Select an option:
  ```
  
- 첫번째 화면

  - 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
  - 그래서 기본값을 어떻게 작성할 것인지 선택해야 함
  - 1을 입력하고 Enter 진행 (다음 화면에서 직접 기본 값 입력)

  ```bash
  Please enter the default value now, as valid Python
  The datetime and jango.utils.timezone modules are available, 
  so you can do e.g. timezone.now
  Type 'exit' to exit this prompt
  >>>
  ```

- 두번째 화면

  - comment의  user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함
  - 마찬가지로 1 입력하고 Enter 진행
  - 그러면 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됨
  

### CREATE

인증된 회원의 댓글 작성 구현하기

작성하기 전 로그인을 먼저 진행한 상태로 진행

**CommentForm**

- CommentForm 출력을 확인해보면 create 템플릿에서 불필요한 user 필드가 출력됨

- 사용자로부터 받는 것이 아니라 url의 variable routing을 통해 처리해야 함

- CommentForm의 출력 필드 수정

  ```python
  # articles/forms.py
  
  from django import forms
  from .models import Comment
  
  class CommentForm(forms.ModelForm):
      
      class Meta:
          model = Comment
          fields = ('article', 'users', )
  ```

**외래 키 데이터 누락**

- 게시글 작성 시 NOT NULL constraint failed: articles_comment.user_id 에러 발생

- “NOT NULL 제약 조건이 실패했다: articles_comment 테이블의 user_id 컬럼에서”

- 댓글 작성 시 외래 키에 저장되어야 할 작성자 정보가 누락 되었기 때문

- 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션을 활용

  ```python
  # articles/views.py
  
  from .models import Article
  from .forms import CommentForm
  
  def comments_create(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.article = article
          comment.user = request.user
          comment_form.save()
      return redirect('articles:detail', article.pk)
  ```

### READ

**댓글 작성자 출력**

- detail 템플릿에서 각 게시글의 작성자 출력

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  
    <h4>댓글 목록</h4>
  
    <ul>  
      {% for comment in comments %}
        <li>
          {{ comment.user }} - {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE">
          </form>
        </li>
      {% endfor %}
    </ul>
  {% endblock content %}
  ```

### DELETE

**댓글 삭제 시 작성자 확인**

- 댓글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제 할 수 있도록 함

  ```python
  # articles/views.py
  
  from .models import Comment
  
  def comments_delete(request, article_pk, comment_pk):
      comment = Comment.objects.get(pk=comment_pk)
      if request.user == comment.user:
          comment.delete()
      return redirect('articles:detail', article_pk)
  ```

- 추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  
    <ul>  
      {% for comment in comments %}
        <li>
          {{ comment.user }} - {{ comment.content }}
          {% if request.user == comment.user %}
            <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
              {% csrf_token %}
              <input type="submit" value="DELETE">
            </form>
          {% endif %}
        </li>
      {% endfor %}
    </ul>
  {% endblock content %}
  ```

### is_authenticated

- is_authenticated 와 View decorator를 활용하여 코드 정리하기

**인증된 사용자인 경우만 댓글 작성 및 삭제하기**

```python
# articles/views.py

from django.views.decorators.http import require_POST
from .models import Article
from .forms import CommentForm

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
	    article = Article.objects.get(pk=pk)
	    comment_form = CommentForm(request.POST)
	    if comment_form.is_valid():
	        comment = comment_form.save(commit=False)
	        comment.article = article
	        comment.user = request.user
	        comment_form.save()    
	    return redirect('articles:detail', article.pk)
    return redirect('accounts:login')

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```

**비인증 사용자는 CommentForm을 볼 수 없도록 하기**

```django
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
<hr>
  {% if request.user.is_authenticated %}
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  {% else %}
    <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요.]</a>
  {% endif %}

{% endblock content %}
```

## 마무리

- A many-to-one relationship
  - Foreign Key
  - Django Relationship fields
  - Related manager
- N:1 모델 관계 설정
  1. Comment - Article
  2. Article - User
     - Referencing the User model
  3. Comment - User