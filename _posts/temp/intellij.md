---
layout: post
title:  "intellij"
date:   2017-12-22 14:19:51 +0900
categories: linux
---

# intellij를 이용하며 유용했던 정보들...

## intellij 트리얼 계속 이용하기
app을 삭제할 필요 없이 관련파일을 찾아 삭제
```bash
$ find / -n '*jetbrains*'

/private/var/db/BootCaches/D7D026CC-142F-4CA4-9F5F-791AFEA35031/app.com.jetbrains.intellij.playlist
....
/private/var/folders/tz/82dl0m5x6_97tzg4dgx8th640000gn/C/com.jetbrains.intellij
.....
.....
```
위의 파일로부터 1.txt 파일생성
```bash
/private/var/db/BootCaches/D7D026CC-142F-4CA4-9F5F-791AFEA35031/app.com.jetbrains.intellij.playlist
/private/var/folders/tz/82dl0m5x6_97tzg4dgx8th640000gn/C/com.jetbrains.intellij
/private/var/folders/tz/82dl0m5x6_97tzg4dgx8th640000gn/C/com.jetbrains.intellij.ce
/Users/jb/Library/Saved Application State/com.jetbrains.intellij.savedState
/Users/jb/Library/Saved Application State/com.jetbrains.intellij.ce.savedState
/Users/jb/Library/Preferences/com.jetbrains.intellij.ce.plist
/Users/jb/Library/Preferences/jetbrains.jetprofile.asset.plist
/Users/jb/Library/Preferences/com.jetbrains.intellij.plist
/Users/jb/Library/Preferences/jetbrains.idea.d7ab3053.plist
/Users/jb/Library/Caches/IntelliJIdea2017.3
/Users/jb/Library/Caches/IdeaIC2017.3
```
xargs rm -r <1.txt
