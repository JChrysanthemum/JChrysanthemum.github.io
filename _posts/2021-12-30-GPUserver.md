---
layout:     post
title:      [DL server backup]
subtitle:   [Common command]
date:       [2021-12-30]
author:     J.C.
header-img: img/post-bg-article.jpg
catalog: true
tags:
    - DL server
onTop: False
comments: true
---

# Location

 Name | Cabinets| Other
---|---|---
 V100 | c7 | 9-12u  
 Synology | c7 | 14u 

Get Address form Admin
  
# 1. SSH Config

Config the sshd config
```
sudo vim /etc/ssh/sshd_config
```

Raw 37 `PubkeyAuthentication yes`

Raw 40 uncomment `AuthorizedKeysFile      .ssh/authorized_keys .ssh/authorized_keys2`

Raw 56 uncomment `PasswordAuthentication no`

# 2. set uid gid
`sudo usermod -u <uid> -g <gid> <usr>`

example:  `sudo usermod -u 1001 -g 100 dslab`

# 3. CUDA install

DL has install web-cuda installer,so you can isntall anycuda just by
`sudo apt isntall cuda-x-x`

# 4. fstab
Add one like this `192.168.233.1:/volume1/homes/jiangxt21    /home/jiangxt21/synData    nfs    noexec    0     0`
Then `sudo mount -a`

## 4.1 netplan
Apply local ip for syn

edit the file `/etc/netplan/00-installer-config.yaml`

```bash
enp94s0f0:
      optional: true
enp94s0f1:
      addresses: [192.168.233.2/30] # the port for syn
      optional: true
```

```bash
sudo netplan apply
sudo systemctl restart NetworkManager.service
```


# 5.Flow

1. Send readme doc to them
2. Adduser with public key, set a default password
3. Add a `synData` folder to their home
4. After all user, edit /etc/fstab