---
layout: post
title: "spring"
date: 2017-01-012 14:19:51 +0900
categories: java
---

```bash
# 자바 경로는 자바목록에 등록
alternatives --install <link> <name> <path> <priority>
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk1.8.0_161/bin/java 1
echo 1 | sudo update-alternatives --config java  # 목록에서 디폴트 java 설정
sudo update-alternatives --list java  # 자바 목록 보기
nano /etc/environment  # JAVA_HOME설정
JAVA_HOME="/usr/lib/jvm/java1.8.0_161"  # 추가
```

+ gradle 프로젝트 서버 실행
```
gradle bootRun
```

+ lombok
```java
@ToString(exclude={"..."})
```
를 통해 출력에 원하지 않는 스트링을 지정할 수 있음

+ @Data 는 사용이 편하기는 하지만 기피하는것이 맞음
