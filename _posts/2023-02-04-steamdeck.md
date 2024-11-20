---
layout:     post
title:      [Steam Deck Configs]
subtitle:   [All many good features]
date:       [2023-02-04]
author:     J.C.
header-img: img/post-bg-article.jpg
catalog: true
tags:
    - Game
onTop: false
comments: true
---

# 1. Preparation

Make steam deck available on CLI.

`Linux steamdeck 5.13.0-valve10.3-1-neptune-02176-g5fe416c4acd8`

First, set password and make system writeable

```shell
passwd
sudo steamos-readonly disable 
sudo pacman-key --init 
sudo pacman-key --populate archlinux
```

Then, use clash for proxy

```shell
wget https://github.com/Dreamacro/clash/releases/download/premium/clash-darwin-amd64-2023.03.18.gz
gzip -d lash-darwin-amd64-2023.03.18.gz
mv lash-darwin-amd64-2023.03.18 clash
sudo chmod 755 clash
sudo chmod +x clash
```

Config tun mode, edit your yml configure file:

```text
tun:
  enable: true
  stack: system # or gvisor
  auto-route: true # auto set global route
  auto-detect-interface: true # conflict with interface-name
# proxies seg here
```

In most cases, `clash.gz` and `mmdb` need download by mirrors. And *yaml: invalid Unicode char* means your config.yml contains no unicode emoj

Then install base SWs

```shell
sudo pacman -S openssh net-tools
```
