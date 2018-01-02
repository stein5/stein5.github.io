---
layout: post
title: "Django Channels와 Websocket을 활용해서 실시칸 채팅 만들기"
date: 2017-12-14 23:00:00 +0900
categories: django
---

## Websocket
+ is a computer communication protocol
+ communicates channels over a single TCP connection
+ provides full-duplex communication(Unlike HTTP). This is the key point to use it to build a web based chatting application

## Redis
Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries

## install packages
```bash
pip install django
pip install channels
pip install asgi-redis
pip install daphne
```

https://gearheart.io/blog/creating-a-chat-with-django-channels/

## Django Channels
### what is channel?
+ Django is a request/response based framework, but now has a complete architectural change with Django Channels
![django](./django1.png)
+ Channels allow (Django) servers to communicate with Websockets
+ Django runs with Channels "event oriented", is responding not just to requests but also to a wide array of events
![channels](./channels.png)
+ A **consumer** is a **event handler**, which is called independently in a way much like a view is called
+ The core of the system is a datastructure called a channel. It ist based the first-in first-out queue
+ **messages** are put onto the channel **by producers**, and then given **to just one of the consumers** listening to that channel
+ A lot of producers can write lots of messages into a channel with no consumers and then a consumer can come along later and will start getting served those queued messages
+ Django channels are network-transparent
+ identified uniquely by a name string from any connected machine

### How do we use channels?
+ assign a function to consume a channel in channel_routing
+ the function get a message object as a parameter, that have:
    - content, attribute which is a dict data
    - channel, attribute which is the channel came from
+ Django runs in three separate layers:
    - Interface servers, WSGI adapter and Websocket server
    - The channel backend, a datastore
    - The workers, to listen on all relevant channels
+ A **consumer** takes a channel message and can write out zero to many other channel messages
+ The interface servers transform connections from the outside world(HTTP, WebSockets, etc) into messages on channels, and than worker are to write to handle these messages
```python
# Listens on http.request
def my_consumer(message):
    # Decode the request from message format to a Request object
    django_request = AsgiRequest(message)
    # Run view
    django_reponse = view(django_request)
    # Encode the reponse into message informat
    for chunk in AsgiHandler.encode_reponse(django_reponse):
        message.reply_channel.send(chunk)
```
    - Usually normal HTTP is handled by Django's built-in consumers that plug it into the view/template system, but it can be overridden to add functionality
+ In response to any event, code can run(and can be sent on channel)
    - trigger on model saves
    - trigger on other incomming messages
    - from code paths inside views and templates

### ws.send('hello')전에...
+ INSTALLED_APPS 에 'channels'추가 누락 --> handshake에러
+ brew install redis, brew services start redis 누락
    - https://stackoverflow.com/questions/37761162/django-development-server-showing-error-61-connection-refused-with-redis
    - https://superuser.com/questions/504892/how-do-i-restart-redis-that-i-installed-with-brew

### login페이지 열기 전에...
+ settings.py에 TEMPLATES - 'DIRS' 에 'templates'추가
