---
layout: post
title: "django document정리"
date: 2017-01-01 14:19:51 +0900
categories: programming
---

# Django Tutorial
### url patterns
path()
+ path(route, view, kwargs=None, name=None)
+ New in Django 2.0.

# The view layer
## Introduction to class-based views
+ Adventages:
    - Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.
    - Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components.
+ Django's URL resolver expects to send request and associated arguments to a callable function, this is, why class-based views have an as_view() class method
+ as_view() function creates an instance of the class and calls its dispatch() method
+ dispatch looks at the request to determine whether it is a GET, POST, etc, and relays the request to matching method if one is defined, or raises HttpResponseNotAllowed if not
