---
layout: post
title: Orange Pi 5 Plus Set up
description: Env set up
keywords: 
date: [2023-12-21]
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---

**Preparation**: Debian flashed board.

# 1. Proxy

## 1.1 Clash

After Dreamacro delete clash-kernel repo for politic pressure, I found a back up of this repo at [Kuingsmil](https://github.com/Kuingsmile/clash-core/releases)

Download [arm64 core](https://github.com/Kuingsmile/clash-core/releases/download/premium/clash-linux-arm64-2023.08.17.gz).

```shell
gzip -d clash-linux-arm64-2023.08.17.gz
mv clash-linux-arm64-2023.08.17 clash
sudo chmod 755 clash
sudo chmod +x clash
```

And proxychains

```shell
sudo apt install proxychains4
```

Replace list in `/etc/proxychains4.conf` to `http 	127.0.0.1 7890`

After zsh and powerlevel10k installed, add `alias sshd= "nohup /home/orangepi/clash -f dslab.yml &"` to .zshrc

# 2 VNC settings

Allow copy and paste between pi and PC by [this](https://superuser.com/questions/1081489/how-to-enable-text-copy-and-paste-for-vnchttps://superuser.com/questions/1081489/how-to-enable-text-copy-and-paste-for-vnc)

```shell
sudo apt-get install autocutsel
```
Add the line `autocutsel -fork` to ~/.vnc/xstartup: like

```txt
#!/bin/bash
#xrdb $HOME/.Xresources
#startxfce4 &

unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
startxfce4 &
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey &
vncconfig -iconic &
autocutsel -fork
```

Add `alias vncs="vncserver -geometry 1600x900"` to zshrc/bashrc to open a desktop with good resolution.


# 3 Web Scrxping

Follow the selenium [doc](https://www.selenium.dev/documentation/webdriver/browsers/firefox/), download the latest geckodriver.

```shell
wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux-aarch64.tar.gz
gzip -d geckodriver-v0.34.0-linux-aarch64.tar.gz
sudo tar -C /usr/local/bin/ -xvf  geckodriver-v0.34.0-linux-aarch64.tar
```

Selenium said they don't support on arm64(arrch64) system [answer](https://github.com/SeleniumHQ/selenium/issues/12778#issuecomment-1726073892), so the problem `OSError: [Errno 8] Exec format error: 'PATH/selenium/webdriver/common/linux/selenium-manager'` oocurs. 

And I found it could be fixed by [this](https://stackoverflow.com/a/77099069/7064406), skiping selenium-manager by define driver start point.

```shell
sudo apt install binfmt-support qemu qemu-user-static
```

Use selenium via manually configuration. python example:

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'/usr/bin/firefox-esr'
from selenium.webdriver.firefox.service import Service
driver = webdriver.Firefox(options=options)
# Some jobs
```
