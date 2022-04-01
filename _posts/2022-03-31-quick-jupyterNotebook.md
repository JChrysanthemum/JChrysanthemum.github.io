---
layout:     post
title:      [Quick jupyter on server]
subtitle:   [JupyterNotebook config and web on local]
date:       [2022-03-31]
author:     J.C.
header-img: img/post-bg-article.jpg
catalog: true
tags:
    - Jupyter Notebook
onTop: false
comments: true
---

# 1.Instal jupyter notebook by pip

```bash
pip3 install jupyterlab
```

or 
```bash
pip3 install jupyter
```

# 2.Edit config

## 2.1 Define password

Type password and get agon by python shell

```python
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("s3kr3tp4ssw0rd") 
# '$argon2id$v=19$m=102400,t=2,p=8$tSm+JOWigOgPZx/44K5fQ$WDyus6py50bVFIPkjA28lQ' 
```

Edit file `.jupyter/jupyter_notebook_config.json `
```json
{
  "NotebookApp": {
    "password": "'$argon2id$v=19$m=102400,t=2,p=8$tSm+JOWigOgPZx/g44K5fQ$WDyus6py50bVFIPkjA28lQ'"
  }
}
```

## 2.2 Edit port and browser

Edit file `.jupyter/jupyter_notebook_config.py `

```python
c.NotebookApp.open_browser = False

c.NotebookApp.port = 9999
```

## 2.3 Startup
run this in tmux or screen.

```bash
jupyter notebook
```

# 3 Use SSH tunnel to boardcast your web
Note: Xmanger is slow

```bash
ssh -N -L <localport>:localhost:<remoteport> <usr>@<addr> 
ssh -N -L 1111:localhost:2222 user@0.0.0.0
```

# 4 Add venv to jupyter

Keep your venv acivated `(venv) ~/PATH`

```bash
 python -m ipykernel install --user --name=<NAME>
```

Then it will auto config the kernel.json file

