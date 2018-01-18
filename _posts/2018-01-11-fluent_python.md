---
layout: post
title: "fluent python"
date: 2017-01-01 14:19:51 +0900
categories: python
---

# 파이썬 데이터 모델
+ 파이선 최고의 장점은 일관성
+ '파이썬 데이터 모델': 일종의 프레임 워크, 파이썬을 설명하는것, 시퀀스, 반복자, 함수, 클래스, 관리자 등 언어 자체의 구성 단위에 대한 인터페이스를 제공
+ 파이썬 인터프리터는 특별메서드를 호출해서 기본적인 객체 연산을 수행
ex) my_collection[key]를 평가하기 위해 인터프리터는 ```my_collection.__getitem__()```를 호출
+ 특별메서드는 구현된 객체가 반복, 컬렉션, 속성접근, 연산자 오버로딩, 함수및 메서드 호출, 객체 생성 및 제거, 문자열 표현 및 포맷, 블록 등 콘텍스트 관리,, 같은 기본적인 구조체를 구현하고 지원하고 함께 사용할 수 있게 해줌

## 파이썬 카드 한벌
```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suite'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                    for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
```
```bash
>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suite='diamonds')
>>> deck = FrenchDeck()
>>> len(deck)
52
>>> deck[0]
Card(rank='2', suite='spades')
>>> deck[-1]
```
파이썬은 시퀀스에서 항목을 무작위로 골라내는 random.choice() 메서드 제공
```bash
>>> from random import choice
>>> choice(deck)
Card(rank='3', suite='hearts')
```
Q: 시퀀스라.. ```__getitem__()```을 구현하면 시퀀스가 있는건가??

```__getitem__()``` 메서드가 없는경우 인덱싱이 지원되지 않으며 시퀀스가 아니기 때문에 choice메서드 사용불가
```bash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jay/.pyenv/versions/3.6.3/lib/python3.6/random.py", line 258, in choice
    return seq[i]
TypeError: 'FrenchDeck' object does not support indexing
```
#### 특별 메서드를 이용함으로 생기는 장점
+ 사용자가 표준연산을 수행하기 위해 클래스 자체에서 구현한 임의 메서드명을 암기할 필요가 없음
+ 파이썬 표준 라이브러리에서 제공하는 풍부한 기능을 별도로 구현할 필요 없이 바로 사용할 수 있음. 이 기능들은 많은경우 특별메서드를 이용. 예) choice함수
+ ```__getitem__()``` 메서드는 self._cards의 [] 연산자에 작업을 위임하므로 deck객체는 슬라이싱도 자동 지원
+ ```__getitem__()```로 인해 반복문에서도 deck(FrenchDeck의 객체)을 사용 가능
+ ```__contains__()``` 메서드가 없다면 in 연산자는 차례대로 검색. deck의경우 반복가능함으로 in 이 작동
+ sorting

```python
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
```
정렬을 한 결과출력
```bash
for card in sorted(deck, key=spades_high):
    print(card)

Card(rank='2', suit='clubs')
Card(rank='2', suit='diamonds')
....
```
+ FrenchDeck은 불변객체이기 때문에 셔플링 할 수 없음. 캡슐화를 어기고 _cards 속성을 직접 조작하지 않는한 카드의 위치를 바꿀수 없음. 그래서 ```__setitem__()```메서드 도입.
+ 특별메서드는 우리가 아니라 파이썬 인터프리터가 호출하기 위한 것. 예외적으로 list, str, bytearray등과 같은 내장자료형의 경우 특별메서드보다 더 손쉬운 방법을 선택. Cpython의 경우 len()메서드는 메모리에있는 모든 가변 크기 내장 객체를 나타내는 PyVarObject C구조체의 ob_size필드 값을 반환. 특별메서드는 종종 암묵적으로 호출. 예를들어 for i in x: 문의 경우 실제로는 iter()를 호출, 이 함수는 다시 ```x.__iter__()```를 호출
+ ```__init__()```메서드를 제외하고는 특별메서드를 직접 호출하는 경우는 많지도 않으며 일반적으로 len(), iter(), str()등 관련된 내장함수를 호출하는것이 더 좋음.

#### 수치형 흉내내기
+ ```__repr__()```특별메서드는 객체를 문자열로 표현하기 위함

|  | formating방법 |
| -- |----------- |
| Old | '%s %s' % ('one', 'two') |
| New | '{} {}'.format('one', 'two') |
| Output | one two |
| Old |'%d %d' % (1, 2) |
| New | '{} {}'.format(1, 2) |
| Output | 1 2 |
+ %s대신 %r을 사용. string은 따옴표를 넣어서 파싱함.
+ ```__add__()```, ```__mul__()```는 +, * 연산자를 구현. 객체를 새로 만들어서 반환하며 피연산자는 변경하지 않음.
+ ```__bool__()``` 항상 True나 False를 반환. ```__bool__()```이나 ```__len__()```을 구현하지 않은경우 사용자정의 클래스객체는 항상 참. bool(x)는 ```x.__boll__()```을 호출한 결과를 이용. ```__bool__()```이 구현되어 있지 않으면 파이썬은 ```x.__len__()```을 호출하며, 이 특별메서드가 0 을 반환하면 bool(x)은 False를, 그렇지 않으면 True를 반환.
