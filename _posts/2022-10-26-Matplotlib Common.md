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
Seaborn detail in [SeabornPlotConfig.md](2024-09-23-SeabornPlotConfig.md)

# 2. Color
https://matplotlib.org/stable/users/prev_whats_new/dflt_style_changes.html

Color|Hex
---|---
<span style="color:#1f77b4">████████████████ </span> | '#1f77b4'
<span style="color:#ff7f0e">████████████████ </span> | '#ff7f0e'
<span style="color:#2ca02c">████████████████ </span> | '#2ca02c'
<span style="color:#d62728">████████████████ </span> | '#d62728'
<span style="color:#9467bd">████████████████ </span> | '#9467bd'
<span style="color:#8c564b">████████████████ </span> | '#8c564b'
<span style="color:#e377c2">████████████████ </span> | '#e377c2'
<span style="color:#7f7f7f">████████████████ </span> | '#7f7f7f'
<span style="color:#bcbd22">████████████████ </span> | '#bcbd22'
<span style="color:#17becf">████████████████ </span> | '#17becf'

## 3 Custom table width percentage

Add width control before markdown table

```text
<style>
table th:first-of-type {
    width: 15%;
}
table th:nth-of-type(2) {
    width: 65%;
}
table th:nth-of-type(3) {
    width: 15%;
}
</style>
```