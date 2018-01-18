---
layout: post
title: "lolo python3"
date: 2017-01-012 14:19:51 +0900
categories: python
---

# lolo python2 => python3 변환 이슈
### 문법이슈

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


### 라이브러리이슈

| python2 | python3 | explain |
| ------- | ------- | ------- |
| import HTMLParser | from html.parser import HTMLParser ||
| import StringIO | from io import StringIO ||
| import urlparse | from urllib.parse import urlparse ||
| urllib.quote | urllib.parse.qoute ||
| from urllib import quote as urllib_quote | from urllib.parse import quote as urllib_quote ||
| tablib==0.11.2 | tablib==0.11.5 ||


### 현재 상황 및 남은 과제
+ 새로운가상환경(python3.6.3+requirements.txt)에서 runserver가능
+ 현재 수정완료 페이지 및 기능
    - 메인페이지열기
    - 상품페이지열기
    - 카테고리페이지열기
    - 장바구니담기
    - 장바구니열기
    - 장바구니에서 상품수량 수정
    - 구매
    - 로그인
    - 로그아웃
    - 마이페이지열기
+ 새로운 페이지를 열거나 기능을 실행하여 에러메세지 확인 후 코드수정
    - 대부분 위의 문법이슈 또는 라이브러리이슈 수정 중 누락된 부분일 가능성이 큼
    - 전체검색으로 검색하여 수정하되 예외적인 부분 예의주시
    - 유니코드 관련 부분 수정필요(u'', u"" => '', "" 변환포함)
    - 위의 문법이슈 또는 라이브러리 이슈에 해당하지 않을경우 검색으로 어렵지 않게 찾을수 있음
    - 단순변환이 아닌경우(예를들어 위의 람다, 필터, 맵함수가 포함 되어 어떤 데이터가 생성되어 반환되는 경우 등)에는 python2에서 출력된 결과값이 나오도록만 python3문법으로 맞춰주면 됨
