---
layout: post
title:  "jekyll"
date:   2017-01-01 14:19:51 +0900
categories: jekyll update
---

sudo apt-get install ruby ruby-dev
(brew install ruby)
gem -v
gcc -v
make -v

sudo gem install jekyll bundler
jekyll —version
gem list jekyll

sudo gem install minima
sudo gem install jekyll-feed

~/ 에서
jekyll new my_blog
jekyll build —destination my_blog
cd my_blog
bundle install
jekyll serve  # 또는 bundle exec jekyll serve
