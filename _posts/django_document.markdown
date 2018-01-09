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
## Class-based views
```python
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html")),
]
```
