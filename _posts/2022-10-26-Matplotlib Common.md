---
layout:     post
title:      [Matplotlib Common]
subtitle:   [Common settings]
date:       [2022-10-26]
author:     J.C.
header-img: img/post-bg-article.jpg
catalog: true
tags:
    - Infs
onTop: false
comments: true
---

# 1.Font
## 1.1 Times New Romman fonts

Install fonts on Ubuntu

```bash
sudo apt install msttcorefonts -qq
rm ~/.cache/matplotlib -rf
```
Set font in python
```python
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
```

## 1.2 Global font size

```python
import matplotlib.pyplot as plt

SMALL_SIZE = 40
MEDIUM_SIZE = 70
BIGGER_SIZE = 120

plt.rcParams["font.family"] = "Times New Roman"
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
```

# x. Color
https://matplotlib.org/stable/users/prev_whats_new/dflt_style_changes.html

Color|Hex
---|---
<span style="color:#1f77b4">████ </span> | '#1f77b4'

