---
layout: post
title: "about django apps"
date: 2017-12-14 23:00:00 +0900
categories: django
---

## **장고 앱 디자인의 기본**
누구나 장고에서 쓰이는 '앱(app)'이란 낱말에 대해 혼란스러움을 느낌. 몇가지 개념에 대한 정리 필요

+ 장고 프로젝트: 장고 웹 프레임워크를 기반으로 한 웹 어플리케이션을 지칭
+ 장고 앱: 프로젝트의 한 기능을 표현하기 위해 디자인된 작은 라이브러리. 장고 프로젝트는 다수의 장고 앱으로 구성. 앱 중 일부는 프로젝트 내부적으로 한 번만 이용되고 재사용 되지 않음(때때로 외부 장고 패키지를 지칭하기도 함)
+ INSTALLED_APPS: 프로젝트에서 이용하려고 INTALLED_APPS 세팅에 설정한 장고 앱들을 지칭
+ 서드파티 장고 패키지: 파이썬 패키지 도구들에 의해 패키지화된, 재사용 가능한 플러그인 형태로 이용 가능한 장고 앱을 지칭

## 장고 앱 지다인의 황금률
"좋은 장고 앱을 정의하고 개발하는 것은 더글라스 맥얼로이(Douglas Mcllroy)의 유닉스 철학을 따르는 것이다. '한 번에 한 가지 일을 하고 그 한 가지 일을 매우 충실히 하는 프로그램을 짜는 것이다'" - 제임스 베넷, 장고 코어 개발자이자 릴리즈 매니저

핵심은 **각 앱이 그 앱의 주어진 임무에만 집중할 수 있어야 한다는 것.** 어떤 앱의 성격과 기능을 한 문장으로 설명 할 수 없거나 그 앱을 설명하기 위해 '그리고/또한'이란 단어를 한 번 이상 사용해야 한다면, 이미 그 앱은 너무 커질대로 커져 여러 개로 나누어야 할 때가 되었다는 의미.

### 예
예를들어 'Two Scoops'라는 가상의 아이스크림 상점을 위한 웹 애플리케이션을 만든다고 가정했을 때 바람직한 구조는 다음과 같음
```bash
twoscoops_project
├── config
│   ├── __init__.py
│   ├── settings
│   │   ├── local.py
|   |   ├── dev(test).py
|   |   ├── stage.py            
│   |   └── production.py
│   ├── urls.py      
│   └── wsgi.py      
├── docs
├── twoscoops
│   ├── media
│   ├── static
│   ├── templates
│   ├── favors  # 상점의 모든 아이스크림 종류가 기록되고 그 목록을 웹사이트에 보여주는 앱
│   ├── blog  # 상점 Two Scoops의 공식 블로그
│   ├── events  # 상점의 행사 내용을 상점 웹 사이트에 보여주는 앱
│   ├── shop  # 온라인 주문을 통해 아이스크림을 판매하는 앱
│   └── ticket  # 무제한 아이스 크림 행사에 이용 될 티켓 판매를 관리하는 앱
├── .gitignore
├── requirements.txt
└── manage.py
```
각 앱을 살펴보면 각각의 앱은 하나의 역할만 수행. 물론 각 앱은 서로 연관 관계에 있음. tickets앱이 events와 분리되어 있다는 점에 주목. 티켓을 팔기위해 events앱을 확장하는 대신 tickets앱을 새로 생성. 대부분의 이벤트가 티켓을 필요로 하는 것이 아니며, 사이트가 성장함에 따라 이벤트 캘린더와 티켓 판매 사이에 복잡한 로직이 생겨 날 수도 있기 때문.

### 확신 없이는 앱을 확장하지 않는다
앱을 디자인하는데 너무 완벽해 지려고 하지 않아야함. 때때로 만들어진 앱을 다시 만들거나 여러개로 쪼개야 할 때도 있을 것. 앱들을 될 수 있으면 작게 유지하려고 해야함... 황당하게도 왜! 그런가에 대한 설명은 이책에 상당히 부족함...

### a reusable app, 이식 가능 앱요
http://django-reusable-app-docs.readthedocs.io/en/latest/
https://docs.djangoproject.com/en/2.0/intro/reusable-apps/

### 앱 모듈
#### 공통 앱 모듈
```bash
favors
├── __init__.py
├── admin.py
├── forms.py
├── management/
├── migrations/
├── models.py
├── templatetags/
├── tests/
├── urls.py
└── views.py
```
#### 비공통 앱 모듈
```bash
favors
├── __init__.py
├── admin.py
├── forms.py
├── management/
├── migrations/
├── models.py
├── templatetags/
├── tests/
├── urls.py
├── views.py
├── behavior.py  # 믹스인 위치에 대한 옵션
├── constants.py
├── decorators.py
├── db/  # 여러 프로젝트에서 이용되는 커스텀 모델이나 컴포넌트
├── field.py  # 폼필드에 이용
├── factories.py  # 테스트데이터 팩터리 파일
├── helpers.py  # 헬퍼함수. 뷰와 모델을 가볍게 하기 위해 뷰와 모델에서 추출한 코드
├── utils.py  # helpers.py와 같은 기능
├── managers.py  # models.py가 너무 커질경우, 커스텀 모델 매니저 작성
├── signals.py  # 커스텀 시그널 작성
└── viewmixins.py
```
## **장고에서 모델 이용하기**
## 시작하기
### 모델이 너무 많으면 앱을 나눈다
앱 하나에 모델이 스무 개 이상 있다면 앱이 너무 많은 일을 하고 있다는 증거. 크기가 작은 앱으로 분리 하는 것을 고려해야 할 것. 각 앱이 가진 모델수가 다섯 개를 넘지 않아야 한다는 게 우리의 의견.  
### 모델 상속에 주의하자
장고는 세가지 모델 상속 방법을 제공. 추상화 기초 클래스(abstract base class), 멀티테이블 상속(multitable inheritance), 프락시 모델(proxy model)
+ 모델 사이에 중복되는 내용이 최소라고 한다면(오직 한두 개의 명확한 필드만이 여러 개의 모델 사이에서 공유되는 경우), 모델의 상속자체가 필요없을것. 그냥 모델 두 곳에 필드를 추가함
+ 모델들 사이에 중복된 필드가 혼란을 야기하거나 의도하지 않은 실수를 유발할 정도로 많을때, 대부분의 경우 공통 필드 부분이 추상화 기초 모델로 이전 될 수 있게 리팩터링
+ 프락시 모델은 종종 편리하게 이용되지만 다른 두가지 모델 상속방식과는 사뭇 다르게 동작함을 주의
+ 멀티테이블 상속은 혼란과 상당한 부하를 일으키므로 반드시 피하도록 함. 멀티테이블 상속을 이용하는 대신 모델들 사이에서 좀 더 명확한 OneToOneFields와 ForeignKeys를 이용함

### 데이터베이스 마이그레이션
migration tip
+ 자체적인 django.db.migrations스타일로 이루어지지 않은 외부 앱에 대해 마이그레이션을 처리할 때에는 MIGRATION_MODULES세팅을 이용
+ 생성되는 마이그레이션 수가 너무 많아서 불편하다면 squashmigrations를 이용

배포 tip
+ 배포전 rollback할수 있는지 확인
+ 스테이징 서버에서 비슷한 크기의 데이터에 대해 충분히 테스트
+ MySQL을 이용한다면
    + 스키마를 변환ㅎ기 전에 데이터베이스를 반드시 백업. MySQL은 스키마 변경에 대해 트랜잭션을 지원하지 않음. 따라서 롤백이 불가능
    + 가능하다면 데이터베이스를 변경하기 전에 프로젝트를 읽기 전용(readonly)모드로 변경
    + 상당히 큰 테이블의 경우 주의하지 않으면 스키마 변경에 몇시간이 걸릴수도 있음

## 장고 모델 디자인
### 정규화하기
### 캐시와 비정규화
### 반드시 필요한 경우에만 비정규화를 진행
### 언제 널을 쓰고 언제 공백을 쓸것인가


| 필드 타입 | null=True로 설정하기 | blank=True로 설정하기 |
| ------- | -----------------  | ------------------- |
| CharField, TextField, SlugField, EmailField, CommaSeperatedIntegerField, UUIDField | 이용하지 않음. 장고 표준 빈 값(empty value)을 빈 문자열(empty string)로 저장하는것. 일관성을 위해 널값 또는 빈 값을 빈 문자열에 대해 반환하도록 함 | 이용함. 위젯이 빈 값을 허용하기를 원한다면 설정. 이렇게 설정하면 데이터베이스 에서는 빈 값이 빈 문자열로 저장 됨 |
| FileField, ImageField | 이용하지 않음. 장고는 MEDIA_ROOT의 경로를 CharField에 파일 또는 이미지로 저장함. 따라서 같은 패턴이 FileField에도 적용됨. | CharField와 마찬가지로 이용함 |
| IntegerField, FloatField, DecimalField, DuationField 등 | 해당 값이 데이터베이스에 NULL로 들어가도 문제가 없다면 이용 | 위젯에서도 해당 값이 빈 값을 받아 와도 문제가 없다면 이용. 그럴 경우 null=True와 같이 이용 |
| DateTimeField, DateField, TimeField 등 | 데이터베이스에서 해당 값들을 NULL로 설정하는게 가능하다면 이용 | 위젯에서 해당값이 빈값을 받아와도 문제가 없다거나 auto_now나 auto_now_add를 이용하고 있다면 이용. 그럴 경우 null=True와 같이 이용 |
| ForeinKey, ManyToManyField, OneToOneField, GenericIPAddressField | 데이터베이스에 해당 값들을 NULL로 설정하는게 가능하다면 이용 | 위젯에서 해당값(예를들어 셀렉트 박스)이 빈값을 받아와도 괜찮다면 이용 |


### BinaryField
장고 1.8부터 추가됐으며 raw binary data또는 byte저장. filter, exclude, 기다 SQL액션들이 적용되지 않음. 개인적인 의견으로 파일시스템이 훨씬 빠르므로 별로 쓰일꺼같진 않음
### 범용관계 피하기
GenericForignKey지양
## 모델 매니저
커스텀 objects어트리뷰트 활용
## 거대모델 이해하기
거대 모델(fat model) 개념은 데이터 관련 코드를 뷰나 템플릿에 넣기 보다는 모델메서드, 클래스메서드, 프로퍼티, 매니저 메서드 안에 넣어 캡슐화
+ 장점: 어떤 뷰나 여타의 작업일지라도 같은 로직을 이용 할 수 있도록 하는것
+ 단점: 모델 코드의 크기를 신의 객체(god object) 수준으로 폭발적으로 증가시킬 수 있음. 이러한 안티패턴의 결과로 모델클래스가 수백, 수천, 심지어 수만줄을 코드가 될 수 있음. 이애하기 어려우며 테스트나 유지보수 어려움

### 모델 행동(믹스인)
추상화 모델로 부터 로직을 상속받음. 클래스기반 뷰 사용
### 상태 없는 헬퍼 함수
모델로 부터 로직을 떼어내 유틸리티 함수로 넣음으로써 좀 더 독립적인 구성이 가능. 독립적으로 구성시 로직에 대한 테스트가 좀 더 쉬워짐. 단점은 해당 함수들이 자신의 상태를 가지지 않음(stateless)으로 함수에 더 많은 인자가 필요
