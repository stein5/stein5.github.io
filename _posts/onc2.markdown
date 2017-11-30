---
layout: post
title: "python object and class2"
date: 2017-10-13 14:19:51 +0900
categories: programming
---

### 특수메서드
두 언더스코어 __로 시작
```python
class Word():
    def __init__(self, text):
        self.text = text
    def __equals__(self, word2):
        return self.text == word2.text

>>> first = Word('HA')
>>> second = Word('ha')
>>> third = Word('ah')

>>> first == second
True
>>> first == third
False
```
