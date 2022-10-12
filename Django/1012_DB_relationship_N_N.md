[DB relationship N-N](#db-relationship-n-n)

1. [Many to many relationship](#1-many-to-many-relationship)
   + [Intro](#intro)

2. [ManyToManyField](#2-manytomanyfield)

3. [M-N Article-User](#3-m-n-article-user)
   + [Like](#like)

4. [M-N User-User](#4-m-n-user-user)

   + [Profile](#profile)

   + [Follow](#follow)

* [finish](#finish)

# DB relationship N-N

## 1. Many to many relationship

**RDB에서의 관계**

M:N

- Many-to-many relationships
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
- 양쪽 모두에서 N:1 관계를 가짐

### Intro

**용어**

- target model
  - 관계 필드를 가지지 않은 모델
- source model
  - 관계 필드를 가진 모델

**Django ManyToManyField**

- ManyToManyField를 통해 중개 테이블을 자동으로 생성
  ```sql
  patient1.doctors.add(doctor1)
  doctor1.patient_set.all()
  patient2.doctors.remove(doctor1)
  ```

**`related_name` argument**

- target model이 source model을 참조할 때 사용할 manager name
- ForeignKey()의 related_name과 동일

**`through` argument**

- 중개 테이블을 수동으로 지정하려는 경우 **through** 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음

- 가장 일반적인 용도는 **중개테이블에 추가 데이터를 사용**해 다대다 관계와 연결하려는 경우

- through 설정, Resrvation Class에 필드 추가

  ```sql
  reservation1 = Reservation(
      doctor=doctor1, patient=patient1, symptom='headache')
  ```
  
  ```sql
  patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
  ```

**정리**

- M:N 관계로 맺어진 두 테이블에는 변화가 없음
- Django의 ManyToManyField 는 중개 테이블을 자동으로 생성함
- Django의 ManyToManyField 는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
  - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
- N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두 가지 형태로 모두 표현이 가능한 것

## 2. ManyToManyField

**ManyToManyField 란**

- ManyToManyField(to, `**options`)
- M:N, many-to-many 다대다 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음
  - add(), remove(), create(), clear()

**데이터베이스에서의 표현**

- Django는 다대다 관계를 나타내는 중개 테이블을 만듦
- 테이블 이름은 ManyToManyField 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성됨
- `db_table` arguments를 사용하여 중개 테이블의 이름을 변경할 수도 있음

**ManyToManyField’s Arguments**

1. related_name

   - target model이 source model을 참조할 때 사용할 manager name
   - ForeignKey의 related_name과 동일

2. through

   - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
   - 일반적으로 중개 테이블에 extra data with a many-to-many relationship 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 사용됨

3. symmetrical

   - 기본 값: True

   - ManyToManyField가 on self 동일한 모델을 가리키는 정의에서만 사용

     ```python
     class Person(models.Model):
         friends = models.ManyToManyField('self')
     ```

   - True일 경우

     - `_set` 매니저를 추가 하지 않음
     - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)

   - 대칭을 원하지 않는 경우 False로 설정

**Related Manager**

- N:1 혹은 M:N 관계에서 사용 가능한 context 문맥
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조시에 사용할 수 있는 manager를 생성
  - related manager를 통해 queryset api를 사용할 수 있게 됨
- 같은 이름의 메서도여도 각 관계(N:1, M:N)에 따라 다르게 사용 및 동작됨
  - N:1에서는 target 모델 객체만 사용 가능
  - **M:N 관계에서는 관련된 두 객체에서 모두 사용 가능**
- 메서드 종류
  - **add(), remove(),** create(), clear(), set() 등

**methods(M:N)**

- **add()**
  - “지정된 객체를 관련 객체 집합에 추가”
  - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
  - 모델 인스턴스, PK 필드 값을 인자로 허용
- **remove()**
  - “관련 객체 집합에서 지정된 모델 개체를 제거”
  - 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
  - 모델 인스턴스, PK 필드 값을 인자로 허용

**중개 테이블 필드 생성 규칙**

1. source model 소스 모델 및 target model 대상 모델이 다른 경우
   - `id`
   - `<containing_model>_id`
   - `<other_model>_id`
2. ManyToManyField가 동일한 모델을 가리키는 경우
   - `id`
   - `from_<model>_id`
   - `to_<model>_id`

## 3. M-N Article-User

Article과 User의 M:N 관계 설정을 통한 좋아요 기능 구현하기

### Like

**모델 관계 설정**

- ManyToManyField 작성

  ```python
  # articles/models.py
  
  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
  ```

- Migration 진행 후 에러 확인

- like_user 필드 생성 시 자동으로 역참조에는 `.article_set` 매니저가 생성됨

- 그러나 이전 N:1(Article-User) 관계에서 이미 해당 매니저를 사용 중

  - **user가 작성한 글들과 user가 좋아요를 누른 글을 구분할 수 없게 됨**

- user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 함

- ManyToManyField에 related_name 작성 후 Migration

  ```python
  # articles/models.py
  
  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
      like_users = models.ManyToManyField(
          settings.AUTH_USER_MODEL, related_name='like_articles')
  ```

- User - Article간 사용 가능 한 related manager 정리

  - article.user
    - 게시글을 작성한 유저 - N:1
  - user.article_set
    - 유저가 작성한 게시글(역참조) - N:1
  - article.like_users
    - 게시글을 좋아요한 유저 - M:N
  - user.like_articles
    - 유저가 좋아요한 게시글(역참조) - M:N

**LIKE 구현**

- url 및 view 함수 작성

  ```python
  # articles/urls.py
  
  urlpatterns = [
      path('<int:article_pk>/likes/', views.likes, name='likes'),
  ]
  ```

  ```python
  # articles/views.py
  
  def likes(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      
      if article.like_users.filter(pk=request.user.pk).exists():
          article.like_users.remove(request.user)
      else:
          article.like_users.add(request.user)
      return redirect('articles:index')
  ```

- **`.exists()`**

  - QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
  - 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

  ```django
  <!-- articles/index.html -->
  
  {% extends 'base.html' %}
  {% block content %}
  
  {% for article in articles %}
  <div>
    <form action="{% url 'articles:likes' article.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
      <input type="submit" value="좋아요 취소">
      {% else %}
      <input type="submit" value="좋아요">
      {% endif %}
    </form>
  </div>
  {% endfor %}
  
  {% endblock content %}
  ```

- 데코레이터 및 is_authenticated 추가

  ```python
  # articles/views.py
  
  @require_POST
  def likes(request, article_pk):
      if request.user.is_authenticated:
  	    article = Article.objects.get(pk=article_pk)
      
  	    if article.like_users.filter(pk=request.user.pk).exists():
  	        article.like_users.remove(request.user)
  	    else:
  	        article.like_users.add(request.user)
  	    return redirect('articles:index')
      return redirect('accouts:login')
  ```

## 4. M-N User-User

- User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현하기

### Profile

- 자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성

**Profile 구현**

- url 및 view 함수 작성

  ```python
  # accounts/urls.py
  
  urlpatterns = [
      path('profile/<username>/', views.profile, name='profile'),
  ]
  ```

  ```python
  # accounts/views.py
  
  from django.contrib.auth import get_user_model
  
  def profile(request, username):
      User = get_user_model()
      person = User.objects.get(username=username)
      context = {
          'person': person,
      }
      return render(request, 'accounts/profile.html', context)
  ```

- profile 템플릿 작성

  ```django
  <!-- accounts/index.html -->
  
  {% extends 'base.html' %}
  {% block content %}
  <h1>{{ person.username }}님의 프로필 </h1>
  
  <hr>
  
  <h2>{{ person.username }}'s 게시글</h2>
  {% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
  {% endfor %}
  
  <hr>
  
  <h2>{{ person.username }}'s 댓글</h2>
  {% for article in person.comment_set.all %}
  <div>{{ comment.content }}</div>
  {% endfor %}
  
  <hr>
  
  <h2>{{ person.username }}'s 좋아요한 게시글</h2>
  {% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
  {% endfor %}
  
  <hr>
  
  <a href="{% url 'articles:index' %}">back</a>
  {% endblock content %}
  ```

- profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성

  ```django
  <!-- base.html -->
  
  <body>
    <div class="container">
      {% if request.user.is_authenticated %}
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
    </div>
  </body>
  ```
  
  ```django
  <!-- articles/index.html -->
  <p>
    <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
  </p>
  ```

### Follow

**모델 관계 설정**

- ManyToManyField 작성 및 Migration 진행

  ```python
  # accounts/models.py
  
  class User(AbstractUser):
      followings = models.ManyToManyField(
          'self', symmetrical=False, related_name='followers')
  ```

**Follow 구현**

- url 및 view 함수 작성

  ```python
  # accounts/urls.py
  
  urlpatterns = [
      path('<int:user_pk>/follow/', views.follow, name='follow'),
  ]
  ```

  ```python
  # accounts/views.py
  
  from django.contrib.auth import get_user_model
  
  def follow(request, user_pk):
      User = get_user_model()
      person = User.objects.get(pk=user_pk)
      if person != request.user:
          if person.followers.filter(pk=request.user.pk).exists():
              person.followers.remove(request.user)
          else:
              person.followers.add(request.user)
      return redirect('accounts:profile', person.username)
  ```

- 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성

  ```django
  <!-- accounts/profile.html -->
  
  {% extends 'base.html' %}
  {% block content %}
  
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    <div>
      팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
    </div>
    {% if request.user != person %}
    <div>
      <form action="{% url 'articles:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
        <input type="submit" value="Unfollow">
        {% else %}
        <input type="submit" value="Follow">
        {% endif %}
      </form>
    </div>
    {% endif %}
  </div>
  {% endblock content %}
  ```

- 데코레이터 및 is_authenticated 추가

  ```python
  # accounts/views.py
  
  from django.contrib.auth import get_user_model
  
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
  	    User = get_user_model()
  	    person = User.objects.get(pk=user_pk)
  	    if person != request.user:
  	        if person.followers.filter(pk=request.user.pk).exists():
  	            person.followers.remove(request.user)
  	        else:
  	            person.followers.add(request.user)
  	    return redirect('accounts:profile', person.username)
      return redirect('accounts:login')
  ```

## finish

- Many-to-many relationship
  - ManyToManyField()
- M:N (Article-User)
  - Like
- M:N (User-User)
  - Profile
  - Follow