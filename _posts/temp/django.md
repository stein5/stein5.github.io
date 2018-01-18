---
layout: post
title: "장고"
date: 2017-12-18 23:00:00 +0900
categories: django
---

# 장고 기초

## 장고 views
+ 뷰 함수는 첫번쨰 매개변수로 HttpRequest를 전달받음. HttpResponse를 반환함.

## 장고 URLConf
+ r문자로 원시문자열 작성 가능, 원시문자열은 백슬래시를 이스케이프 하는데 사용
+ 캐럿은 해당 패턴이 문자열의 시작과 일치해야 한다는 것을 의미
+ 달러기호는 패턴이 문자열의 끝과 일치해야 한다는 것을 의미
+ URL패턴과 일치하지 않고 슬래시로 끝나지 않는 URL에 대한 모든 요청은 후행 슬래시가 있는 동일한 URL로 리다이렉트됨
+ 와일드 카드 데이터를 뷰 함수에 전달하는 방법은 저장하려는 URL패턴의 데이터 주변에 괄호를 배치
+ 뷰모듈 자체를 가져와 임포트
```python
from . import views
urlpatterns = [
    url('r^hello/$', views.hello),
    ...
]
```
+ 디버그 모드의 특수 케이스 URL
```python
urlpatterns = [
    ...
]
if setting.DEBUG:
    urlpatterns += [url('r^debuginfo/$', views.debug),]
```

### 정규표현식
| 기호 | 일치 유무 검색 대상 |
| --- | --------------- |
| .(dot) | 모든 단일 숫자 |
| \d | 모든 단일 숫자 |
| [A-Z] | A에서 Z까지의 모든 문자(대문자) |
| [a-z] | a에서 z까지의 모든 문자(소문자) |
| [A-Za-z] | a에서 z까지의 모든 문자(대소문자 구분) |
| + | 이전 표현 중의 하나 이상(예: \d+는 1개 이상의 숫자가 일치하는지 알아낸다.) |
| [^/]+ | 슬래시(/)까지 1개 이상 문자(슬래시는 포함하지 않는다) |
| ? | 이전 표현 중의 0개 또는 1개 |
| * | 이전 표현 중의 0개 또는 그 이상 |
| {1,3} | 이전 표현 중의 1과 3(포함) 사이 |
| d{1,2} | 하나 또는 두자리 숫자만 허용 |

### HttpRequest객체에 대한 몇가지 정보
| 속성/메서드 | 설명 | 예제 |
|-- | -- | -- |
| request.path | 전체 경로, 도메인을 포함하지 않고 선행 슬래시를 포함 | "/hello/" |
| request.get_host() | 호스트(즉, "도메인", 공통 용어) | "127.0.0.1:8000" 또는 "www.example.com" |
| request.get_full_path() | 경로와 쿼리 문자열(사용할 수 있는 경우) | "/hello/?print=true" |
| request.is_secure() | 요청이 HTTPS를 통해 이뤄진 경우 True다. 그렇지 않으면 False | True 또는 False |

### request.META
+ 사용자의 IP주소와 에이전트를 포함해 지정된 요청에 대해 사용 할 수 있는 모든 HTTP 헤더를 포함하는 파이썬 딕셔너리
+ HTTP_REFERER: 참조 URL(있는 경우), REFERER의 철자 오류가 있다는 것에 유의 한다
+ HTTP_USER_AGENT: 사용자 웹 브라우저의 사용자 에이전트 문자열(있는경우)
+ REMOTE_ADDR: 클라이언트의 IP주소
+ 딕셔너리임으로 존재하지 않는 키에 접근시 에러발생. try/except절이나 get()메서드를 사용하여 이용

### 명명된 그룹
+ URL에서는 뷰를 인수로 전달하기 위해 괄호를 사용
+ 명명된 정표현식을 사용해 URL캡쳐 가능
+ (? P<name> pattern)의 형태이며 name은 그룹의 이름이고 pattern은 일치시킬 패턴
```python
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'reviews/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    ...
]
```
+ /reviews/2005/03/에 대한 요청은 view.month_archive(request, year='2005', month='03')함수를 호출

## 장고 모델
+ 모델체크
```bash
python manage.py makemigrations books
```
+ order_by매서드를 이용한 정렬에 여러 인수 사용 가능
+ Meta클래스를 이용하여 정렬 가능
```python
class Meta:
    ordering = ['name']
```
+ update() 메서드는 모든 QuerySet에 작동. 여러쿼리를 대량으로 편집
```shell
>>> Publisher.objects.all().update(country = 'USA')
2  # 변경된 레코드의 수를 나타내는 정수
```
+ 모든 데이터 삭제
```python
>>> Publisher.objects.all().delete()
```
+ foreign key를 역으로 찾아들어가거나 다대일 값 액세스
```python
>>> p.book_set.all()
>>> p.book_set.filter(title__icontains='django')  # title은 Book의 속성
```
### 모델관리자
+ 모델관리자는 장고 모델이 데이터베이스 쿼리를 수행하는 객체
+ 각 장고 모델에는 최소한 하나의 관리자가 있으며 여분의 메서드 추가 또는 기존메서드를 수정하기 위해 사용자 정의 관리자 생성 가능
```python
from django.db import models
class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()
class Book(models.Model):
    ....
    objects = BookManager()
```
+ 코드를 복제 할 필요가 없도록 일반적으로 실행되는 쿼리를 캡슐화 함

### 초기관리자 QuerySet수정
+ Manager.get_queryset()메서드를 오버라이드 해서 기본 QuerySet을 재정의 할 수 있음
+ get_queryset()은 필요한 속성으로 QuerySet을 반환해야 함
+ get_queryset()은 QuerySet을 반환하기 때문에 filter(), exclude()및 기타 모든 QuerySet메서드를 사용할 수 있음
```python
from django.db import models
class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super(DahlBookManager, self).get_queryset().filter(author='Roald Dahl')
class Book(models.Model):
    .....
    objects = models.Manager()  # 기본설정 관리자
    dahl_objects = DahlBookManager()

Book.dahl_objects.all()
Book.dahl_objects.filter(title='Matilda')
Book.dahl_objects.count()
```
```python
class MaleManager(models.Manager):
    def get_queryset(self):
        return super(MaleManager, self).get_queryset().filter(sex='M')

class FemaleManager(models.Manager):
    def get_queryset(self):
        return super(FemaleManager, self).get_queryset().filter(sex='M')

class Person(models.Model):
    ...
    people = models.Manager()
    men = MaleManager()
    woman = FemailManager()
```
+ 장고는 클래스에서 정의된 첫번재 Manager를 기본 Manager로 해석하고, 장고의 일부가 해당 모델에만 해당 Manager를 사용 할 것이다(???번역이 이상한건지 이해가 안감)

### 모델 메서드
+ 커스텀 메서드 작성
+ 각 모델에 자동으로 부여된 메서드 오버라이드, 예) __str__(), save(), delete()

### 원시 쿼리 수행
```python
Manager.raw(raw_query, params=None, translations=None)
```
