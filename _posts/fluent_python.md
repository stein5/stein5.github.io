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
ex) my_collection[key]를 평가하기 위해 인터프리터는 my_collection.__getitem__()를 호출
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
Q: 시퀀스라.. __getitem__()을 구현하면 시퀀스가 있는건가??

__getitem__() 메서드가 없는경우 인덱싱이 지원되지 않으며 시퀀스가 아니기 때문에 choice메서드 사용불가
```bash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jay/.pyenv/versions/3.6.3/lib/python3.6/random.py", line 258, in choice
    return seq[i]
TypeError: 'FrenchDeck' object does not support indexing
```
특별 메서드를 이용함으로 생기는 두가지 장점
+ 사용자가 표준연산을 수행하기 위해 클래스 자체에서 구현한 임의 메서드명을 암기할 필요가 없다
