---
layout: post
title: "python object and class"
date: 2017-10-13 14:19:51 +0900
categories: programming
---

### 객체와 클래스

#### 객체란?

숫자에서 모듈까지 파이썬의 모든것는 객체
객체 = 데이터(변수, 속성attribute) + 코드(함수, 함수method)
7,8은 int class의 객체
'cat'과 'duck'은  str class의 객체

#### 클래스 선언하기
```python
class Person():
    def __init__(self):
        self.name = name
```
```python
>>> somone = Person('stein')
```
#### 상속은 언제 사용하는가?
어떤 코딩문제를 해결하려 할 때 우선 필요한 대부분의 기능을 수행하는 기존 클래스를 찾음.
그리고 기존 클래스에 필요한 기능을 추가. 이때 필요한 기능을 상속을 통해 우아하게 추가할 수 있음.
재사용, 재정의라는 과정을 거쳐서...

#### 메서드 오버라이드
부모 메서드를 수정하는것

```python
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!")

>>> Car().exclaim()
I'm a Car!
>>> Yugo().exclaim()
I'm a Yugo!
```

#### 부모에게 도움받기:super
자식 클래스에서 부모 클래스의 메서드를 호출하고 싶을때.
```python
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        # Person.__init__()을 실행하며 첫번재 인자로 EmailPerson을 던져줌.
        super().__init__(name)  
        self.email = email

>>> bob = EmailPerson('Bob', 'bob@gmail.com')
>>> bob.name
Bob
>>> bob.email
bob@gmail.com
```
이와 같이 상속을 사용할 경우 Person클래스의 정의가 변경되더라도 EmailPerson클래스에도 반영됨.

#### 자신: self
```python
>>> car = Car()  # car객체의 Car클래스를 찾음.
>>> car.exclaim()  # car객체를 Car클래스의 exclaim()메서드의 self매개변수에 전달.
I'm a Car!
>>> Car.exclaim(car)
I'm a Car!
```

#### get/set속성값과 프로퍼티
python에서는 private속성이 따로 없으며 모든 속성이 public.
getter와 setter작성 가능 하지만 property작성을 권고.
```python
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

>>> fowl = Duck('Howard')
>>> fowl.name  # fowl.get_name()과 같다.
inside the getter
'Howard'

>>> fowl.name = 'Daffy'  # fowl.set_name('Daffy')와 같다.
inside the setter
>>> fowl.name
inside the getter
'Daffy'
```
property내장함수를 사용하는 방법 외에 데커레이터를 통한 프로퍼티 지정.
```python
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
```
또한 프로퍼티는 계산된 값을 참조 가능.
```python
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
```
속성에 대한 setter프로퍼티를 명시하지 않았음으로 이 속성을 설정할 수 없음.

#### private 네임 맹글링
클래스 정의 외부에서 볼 수 없도록 하는 속성에 대한 네이밍 컨벤션이 존재.
속성 이름 앞에 두 언더스코어(__)를 붙이면 됨.
```python
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

>>> fowl = Duck('Howard')
>>> fowl.__name
Traceback (most recent call last):
    ....
>>> fowl._Duck__name
Howard
```
getter와 setter는 잘 동작함. 하지만 Duck클래스의 인스선트에서 __name으로 접근이 불가능
이처럼 파이썬은 이 속성이 우연히 외부코드에서 발견할 수 없도록 이름을 맹글링함.

#### 메서드 타입
###### 인스턴스 메서드
###### 클래스 메서드
클래스전체와 클래스에 대한 어떤 변화가 있을때 모든 객체에 영향을 미침.
@classmethod데커레이터로 구현. 이 메서드의 첫번째 매개변수는 클래스 자신.(보통 cls로 표기)
```python
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

>>> easy_a = A()
>>> breezy_a = A()
>>> wheezy_a = A()
>>> A.kids()
A has 4 little objects.
```
###### 정적 메서드
@staticmethod데커레이터가 붙어 있으며, 첫번째 매개변후로 self나 cls가 없음.
주로 클래스의 상태 또는 인스턴스의 상태와 관계 없이 바로 실행시킬 수 있는 용도로 사용함.

#### 덕 타이핑
파이썬은 다형성을 느슨하게 구현: 클래스에 상관없이 같은 동작을 다른 객체에 적용 할 수 있음.
```python
class Quote():
    def __init__(self,person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'
