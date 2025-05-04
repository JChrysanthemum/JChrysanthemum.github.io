---
layout: post
title: Steamdeck system settings and fixup
categories: [Fun]
description: 
keywords: game
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---

Steamdeck CLI, proxy and update debug & fixing.
Along with stardew valley with SMAPI.

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
sudo pacman -Sy krfb
```

If the krfb forget the unattended password every boot, try x11nvc

```shell
sh -c "$(curl -fsSL https://gist.githubusercontent.com/x43x61x69/9a5a231a25426e8a2cc0f7c24cfdaed9/raw/vnc_install.sh?$RANDOM)"
```

# 2.Game launch option with proton (steamdeck launch stardewvalley with SMAPI)

If you want launch extra mod-embedding for your game on deck, like SMAPI for stardewvalley, you need to make `steam launch option`.

1. You need to find your game's APP ID, `settings->perproties->update`, for me is `413150`.
2. Then check path for proton. `/home/$USER/.local/share/Steam/steamapps/common/Proton 8.0/proton` if you want steam's proton version. `/home/$USER/.local/share/Steam/compatibilitytools.d/GE-Proton9-5/proton` if you want customed proton.
3. And your modding executable path. I installed SMAPI into the same location of game.

Here is a sample script

```bash
#! /usb/bin/bash

export STEAM_COMPAT_DATA_PATH="/home/$USER/.local/share/Steam/steamapps/compatdata/413150"
export STEAM_COMPAT_CLIENT_INSTALL_PATH=STEAM_COMPAT_DATA_PATH
/home/$USER/.local/share/Steam/compatibilitytools.d/GE-Proton9-5/proton run "/home/$USER/.local/share/Steam/steamapps/common/Stardew Valley/StardewModdingAPI.exe"
```

4. Write into a script and fill it in launch options `bash /home/$USER/Scripts/launch_SMAPI.sh %command%`

# 3 steam os update debug 

Deck can not install new steam OS, and even can not reset.

Go to desktop mode

```shell
# Manually update and check the output
steamos-update
```

## 3.1 Check network access

If deck can not access the image and have no proxy installed.

Download steam-os file manually: [steam-os ftp](https://steamdeck-images.steamos.cloud/steamdeck)

```shell
# example

wget https://steamdeck-images.steamos.cloud/steamdeck/20250409.1001/steamdeck-20250409.1001-3.8.0.raucb

sudo rauc install steamdeck-20250402.1001-3.8.0.raucb
```

## 3.2 rauc install error

```shell
rauc Installation error: Failed updating slot rootfs.0: failed to run casync extract
```

Then check what happened in rauc: `journalctl -u rauc` and it shows `error while loading shared libraries: libcrypto.so.1.1`

Then, update pacman and try to reinstall openssl 1.1 to fix this. First, you need your root name and password.

If any dependecies break shows, just install it.
e.g., ostree depends on openssl-3.6, `pacman -Su ostree` 

If `pacman` or `sudo` throughs "libcrypto error" too, switch into root `su root`.

If openssl not installed, try to download your opensll **SAME as YOUT VERSION**.

openssl package [ftp](https://steamdeck-packages.steamos.cloud/archlinux-mirror/core-3.3/os/x86_64/?C=M&O=D)

```shell
tar -xvpf openssl-1.1.1.m-1-x86_64.pkg.tar.zst -C / --exclude .PKGINFO --exclude .INSTALL --exclude .MTREE --exclude .BUILDINFO
```

# 4 Install trial-steam version

delete `Steam_appid.txt`, add `WINEDLLOVERRIDES="amd_ags_x64.dIl=b"
%command%`, use proton-GE-xx


