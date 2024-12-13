---
layout: post
title: Decky for steamdeck
categories: [Fun]
description: Decky config and install notes
keywords: game, diy
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---


# 1.Install script

Official [Decky](https://decky.xyz/)

Chinese 大陆 [ohmydeck](https://ohmydeck.net/d/37)

# 2. Debug

Plugin icon not appears after installation. So we need the log of decky. 

Basic linux system knowledge and CLI commands required (at least, deck system readonly disabled, root password ackonwledged, Konsole available).

## **Step 1.** Log into desktop mode and see if the decky service alive. 

```shell
sudo systemctl status plugin_loader.service
```

If you see a green `active (running)`, jump to step 2. If you see a red `failed`, continue.

First, check the console output of this cmd, see if anything usefull. If nothing help, see detail fail log.

```shell
sudo journalctl -u plugin_loader.service -b
``` 

Search in google and fix it. 

case 1: wrong `PYTHONHOME`: Install python by pacman `sudo pacman -S python3`

case 2: mess locale `LookupError: unknown encoding: EUC-TW`: Change locale, find a locale by `locale -a`, here I choose **zh_CN.utf8**; `sudo localectl set-locale LANG=zh_CN.utf8`

## **Step 2.** See decky log and find issues in github.

Decky [enviroment config](https://wiki.deckbrew.xyz/en/plugin-dev/env-vars). 

We need to know the decky default install location is `~/homebrew`. Detail official [debugging instruction](https://wiki.deckbrew.xyz/en/plugin-dev/cef-debugging)




