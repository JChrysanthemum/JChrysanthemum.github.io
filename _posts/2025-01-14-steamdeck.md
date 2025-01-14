---
layout: post
title: Steamdeck system settings
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

