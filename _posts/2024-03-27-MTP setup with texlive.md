---
layout: post
title: MathTextPro setup in TexLive
categories: [cate1, cate2]
description: some word here
keywords: keyword1, keyword2
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---
MathTextPro(MTP) is a math font package. The lite version is free and good enough for most cases.

**Preparation**: Texlive installed.

# 1. Download mtp font

* [Official website](https://www.pctex.com/mtpro2.html) 
* [CTAN mtp-lite](https://ctan.math.utah.edu/ctan/tex-archive/fonts/mtp2lite.zip)
* [Shared Pro (2013)](http://www.latexstudio.net/wp-content/uploads/2013/02/MathTimePro2-fonts.zip)

# 2. Install

Locate the `texmf-local` folder.

```bash
kpsewhich -var-value=TEXMFLOCAL
```

Copy everything under `mtp2lite.zip\mtp2lite\texmf` to your `texmf-local` folder.

Then update hash.

```bash
texhash
```

Update texlive map.

```bash
updmap-sys –enable Map=mtpro2.map
```