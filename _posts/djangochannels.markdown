---
layout: post
title: "Django Channels와 Websocket을 활용해서 실시칸 채팅 만들기"
date: 2017-12-14 23:00:00 +0900
categories: django
---
## Django Channels
+ Django is a request/response based framework, but now has a complete architectural change with Django Channels
+ Channels allow (Django) servers to communicate with Websockets
+ Django runs with Channels "event oriented", is responding not just to requests but also to a wide array of events
+ The core of the system is a datastructure called a channel. It ist based the first-in first-out queue

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
