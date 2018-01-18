---
layout: post
title:  "zsh"
date:   2017-01-01 14:19:51 +0900
categories: tools
---

### 설치

```bash
# zsh설치
$ sudo apt-get install zsh

# og my zsh 설치
$ wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh

# zsh을 디폴트로 설정
$ chsh -s `which zsh`

# os restart
$ sudo shutdown -r 0
```
.zshrc 의 ZSH_THEME="agnoster"로 수정
```bash
$ git clone https://github.com/powerline/fonts.git
$ cd fonts; sh install
```
까지 해도 글씨가 깨짐

font바꾸면 됌 ex) D2Coding for Powerline Regular   
