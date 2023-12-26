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

For jupyter theme
```python
jt -t oceans16 -nfs 22 -tfs 22 -fs 20 -cellw 1280 -lineh 150 -ofs 16 -dfs 16
```

# 5 Notebook on internal server

These tricks will be done by 'ssh-tunel'. The structure of the command is `ssh -N<param,> <localport>:localhost:<remoteport> <usr>@<addr>`.
`ssh -fNR` local-to-remote, `ssh -N -L` remote-to-local. 

For your convenience, add ssh public-key before, or type password every login.


## 5.1 Only ssh are allowed on server

We can access server via ssh, but other ports of server were baned.

The user name of local PC `user`, the port your want to use `P-PC`; IP of server : `IP-S`, the port of server you want to bind `P-S`

```shell
# run on your local PC
ssh -N -L P-PC:localhost:P-S user@IP-S
```

For an example: A GPU server at `172.111.23.5`, with a jupyter-notebook opened at `8888` port. You want use browser with `127.0.0.1:1234` to use notebook locally.

```shell
# run on your local PC
ssh -N -L 1234:localhost:8888 user@172.111.23.5
```

## 5.2 Notebook server in LAN, you and the server have access in another server. 

You need do transfer twice. First, in notebook server, transfer prot to another server `ssh -fNR ...`. Then, in your local PC, transfer **binded** port in another server `ssh -N -L`.

Sounds complex, there is a situation:

```txt
PC --> ServerA <-- ServerB

ServerB is your notebook server, ServerA is common accessable.

PC want use 1234 at browser, ServerB(userB@192.168.1.5) have 8888 on jupyter-notenook, ServerA(userA@200.100.5.3) coud use 9999 to bind.
```

```shell
# Run at ServerB
ssh -fNR 8888:localhost:9999 userA@200.100.5.3
ssh -N -L 1234:localhost:9999 userA@200.100.5.3
```