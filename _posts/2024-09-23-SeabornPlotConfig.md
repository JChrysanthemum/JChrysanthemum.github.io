---
layout: post
title: Seaborn config for fonts and figure size
categories: [Paper]
description: Font size and figure (one and multi) size for high resolution.
keywords: python, plot
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---


# 1.Font config

[Matplotlib Common](./2022-10-26-Matplotlib%20Common.md) to install font **Times New Roman**. A little different in font rc settings for seaborn.

```python
import matplotlib.pyplot as plt
import seaborn as sns

SMALL_SIZE = 60
MEDIUM_SIZE = 80
BIGGER_SIZE = 120

font_rc = {
'font.family':"Times New Roman",   
'font.size':SMALL_SIZE,          # controls default text sizes
'axes.titlesize':MEDIUM_SIZE,    # fontsize of the axes title
'axes.labelsize':MEDIUM_SIZE,    # fontsize of the x and y labels
'xtick.labelsize':SMALL_SIZE,    # fontsize of the tick labels
'ytick.labelsize':SMALL_SIZE,    # fontsize of the tick labels
'legend.fontsize':SMALL_SIZE,    # legend fontsize
'figure.titlesize':BIGGER_SIZE,  # fontsize of the figure title
'legend.title_fontsize':SMALL_SIZE # fontsize of the legend title
}

sns.set_theme(rc=font_rc)
```

# 2. Figure size

## 2.1 For one plot

```python
# 1. Set plot outperface
sns.set_theme(style="whitegrid", palette="pastel",rc=font_rc)

# 2. Width height and DPI
plt.figure(figsize=(28, 20), dpi=300)

# 3. Seaborn plotting here
sns.kdeplot(data=DF,x="data")

# 4. Save by matpltlib
plt.savefig(FILENAME)
plt.clf()
```

## 2.2  For sub plots

```python
# 1. Set plot outperface
sns.set_theme(style="whitegrid", palette="pastel",rc=font_rc)

# 2. Width height and DPI
plt.figure(figsize=(28, 20), dpi=300)

# 3. Create plot axes
f, (ax_top, ax_bottom) = plt.subplots(ncols=1, nrows=2,figsize=(50, 15), dpi=300)

# 4. Seaborn plotting here
sns.kdeplot(data=DF,x="data",ax=ax_top)
sns.kdeplot(data=DF,x="vol",ax=ax_bottom)

# 4. Save by matpltlib
plt.savefig(FILENAME)
plt.clf()
```


# 3. Templates
## 3.1 KDE with broken aixs
```python
def broken_x_kde(tar_name,l1,l2,r1,r2,width_ratios=None, _fig_root = fig_root):
    
    if not os.path.exists(_fig_root):
        os.makedirs(_fig_root,exist_ok=True)
    
    if width_ratios is None:
        width_ratios = ((l2-l1)/(r2-r1), 1)
        
    sns.set_theme(style="whitegrid", palette="pastel",rc=font_rc)
    f, (ax_left, ax_right) = plt.subplots(ncols=2, nrows=1, sharey=True, gridspec_kw={'wspace':0.15} ,figsize=(28, 20), dpi=300, width_ratios = width_ratios)
    
    left_bins = int((r2-l1)/(l2-l1)*40)

    sns.histplot(x=tar_name,data=df, ax=ax_right)
    sns.histplot(x=tar_name,data=df, ax=ax_left,bins=left_bins, edgecolor='black',kde=True,line_kws={"linewidth":5,"color":"white"})

    ax_right.set_xlim(r1, r2)  
    ax_right.set_xlabel("")
    ax_right.xaxis.set
    ax_left.set_xlim(l1, l2)
    ax_left.set_xlabel("")
    
    
    if width_ratios[0] > width_ratios[1]:
        kl = 1
        kr = width_ratios[0]/width_ratios[1]
    else:
        kr = 1
        kl = width_ratios[1]/width_ratios[0]

    ax =  ax_right
    d = .015  # how big to make the diagonal lines in axes coordinates
    x_offset = 0.01 # releated with with_ratios
    
    kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
    # kr = width_ratios[0]/sum(width_ratios)
    ax.plot((-kr*d + kr*x_offset, +kr*d + kr*x_offset), (-0.25*d, +1.75*d), **kwargs)        # top-left diagonal

    ax2 = ax_left

    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((1 - kl*d + kl*x_offset, 1 + kl*d + kl*x_offset), (-0.25*d, +1.75*d), **kwargs)  # bottom-left diagonal
    
    #remove one of the legend
    # ax_right.legend_.remove()
    f.supxlabel(tar_name)
    plt.savefig(pj(_fig_root,'%s.png'%tar_name),
                # transparent=True
                )

broken_x_kde(tar,32,-33,-43,-50,width_ratios=(3,1), _fig_root=_fig_root)
```


