---
layout: post
title:  "atom editor"
date:   2017-01-01 14:19:51 +0900
categories: jekyll update
---

### atom shortcut

#### Package Manager

Ctrl + ,   #


#### keymap.cson

keymap.cson 파일에 다음의 내용을 추가

```javascript
'body':
  'ctrl-alt-pageup': 'window:focus-pane-on-left'
  "ctrl-alt-pagedown": 'window:focus-pane-on-right'
```
