---
layout: post
title: "lolo python3"
date: 2017-01-012 14:19:51 +0900
categories: python
---

# lolo python2 => python3 변환 이슈
+ 문법이슈

| python2 | python3 | explain |
| ------- | ------- | ------- |
| except Exception, e: | except Exception as e: ||
| e.message | str(e) ||
| dict_obj.iteritems() | iter(dict_obj.items())) ||
| tab | spaces | python3에서 검열이 더 빡쎈거같음. 혼용된 부분중 에러가 안나던 부분도 python3에서 에러남 |
| ur"" 또는 ur'' | r""또는 r'' ||
| print "" | print("") ||
| lambda (x, y): (x, y) | lambda x, y: x, y ||
| filter (x, y): (x, y) | filter x, y: x, y ||
| map(x, y) | list(map(x, y)) ||
| xrange() | range() ||
| ```__unicode__()``` | ```__str__()``` ||
| None 비교값 0 | int(None or 0) 비교값 0 | 구매프로세스의 order.py에 해당 로직이 몇 있음 |
| unicode() | str() ||


+ 라이브러리 이슈

| python2 | python3 | explain |
| ------- | ------- | ------- |
| import HTMLParser | from html.parser import HTMLParser ||
| import StringIO | from io import StringIO ||
| import urlparse | from urllib.parse import urlparse ||
| urllib.quote | urllib.parse.qoute ||
| from urllib import quote as urllib_quote | from urllib.parse import quote as urllib_quote ||
| tablib==0.11.2 | tablib==0.11.5 ||
