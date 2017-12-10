---
layout: post
title: "tmux"
date: 2017-01-01 14:19:51 +0900
categories: programming
---

## about tmux

### start tmux
```bash
$ tmux  # start
$ exit  # close
```

### creating named session
```bash
$ tmux new-serssion -s basic
$ tmux new -s basic
$ tmux new -s basic -d  # create and detach from the session
```

### command line prefix
Cntrl + b  # tell tmux that the command we're next typing is for tmux
Prefix + t  # show time

### Detaching and Attaching Sessions
```bash
$ tmux list-sessions
$ tmux ls
$ tmux attach (-t basic)
```
Prefix + d  # detach from current session
```bash
$ exit  # destroy a session within the sessions
$ tmux kill-session -t basic  # from outside
```

### Working with Windows
