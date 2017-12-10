---
layout: post
title: "django"
date: 2017-01-01 14:19:51 +0900
categories: programming
---

# Setting for Develop with Django in Ubuntu

## install pyenv, virtualenv
https://cjh5414.github.io/ubuntu-pyenv-virtualenv/
(in virtualenv)$ sudo apt-get install python3-dev libpq-dev

## install postgresql
설치: https://www.postgresql.org/download/linux/ubuntu/


postres role로 postgres database에 접근
```bash
$ sudo -u postgres psql postgres
postgres=$ \c
sudo -u postgres psql postgres
```
사용할 디비 생성
```bash
postgres=$ ALTER USER postgres WITH PASSWORD '비밀번호';
postgres=$ CREATE DATABASE 디비명;
postgres=$ CREATE USER 유저명 WITH PASSWORD '비밀번호';
postgres=$ ALTER ROLE 유저명 SET client_encoding TO 'utf8';
postgres=$ ALTER ROLE 유저명 SET default_transaction_isolation TO 'read committed';
postgres=$ ALTER ROLE 유저명 SET timezone TO 'UTC';
postgres=$ GRANT ALL PRIVILEGES ON DATABASE 디비명 TO 유저명;
postgres=$ \q
(in virtualenv)$ pip install psycopg2
```

## install gunicorn, nginx
```bash
(in virtualenv)$ pip install gunicorn
(in virtualenv)$ sudo apt-get install nginx
```

# Developing with Django in Ubuntu
## install django
```bash
(in virtualenv)$ python -m django --version  # test if django is already installed
(in virtualenv)$ pip install django
(in virtualenv)$ python
>>> import django
>>> print(django.get_version())
2.0
```
## creating and setting a django project
```bash
(in virtualenv)$ django-admin startproject 프로젝트명
$ tree  # sudo apt-get install tree로 설치 가능
.
├── 프로젝트명     
│   ├── __init__.py  
│   ├── settings.py  
│   ├── urls.py      
│   └── wsgi.py      
└── manage.py        
```
폴더구조를 좀더 직관적으로 변경
```bash
├── config
│   ├── __init__.py
│   ├── settings.py  
│   ├── urls.py      
│   └── wsgi.py      
├── docs
├── 프로젝트명
│   ├── media
│   ├── static
│   └── templates      
├── .gitignore
├── requirements.txt
└── manage.py


```
### 여러개의 settings파일 이용하기
settings.py대신 setting폴더를 생성하고 개발/배포 환경등 설정을 달리함
```bash
$ tree
├── config
│   ├── __init__.py  
│   ├── settings.py
│   │   ├── base.py
│   │   ├── local.py  
│   │   ├── dev.py      
│   │   └── production.py
│   ...
├── ...
...
```

database세팅
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
