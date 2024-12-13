---
layout: post
title: RealSense-Open3D
categories: [Robot]
description: 3D recontruction
keywords: Robot, realsense
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---

<!-- ---
layout:     post
title:      [RealSense-Open3D]
subtitle:   [3D recontruction]
date:       [2024-11-17]
author:     J.C.
header-img: img/post-bg-article.jpg
catalog: true
tags:
    - Jupyter Notebook
onTop: false
comments: true
--- -->


Install Realsense SDK on WIN: Intel.RealSense.SDK-WIN10-<version> in [git release](https://github.com/IntelRealSense/librealsense/releases), record a RGBD bag by realsense viewer.

# 1. Installation

Then, install open3D (9d0cfc8) on Ubuntu (22.04 for me), WIN or tensorflow supoort could see full [turtorial](https://www.open3d.org/docs/latest/compilation.html#config).



GCC 5+ and Clang 7+: `sudo apt update && sudo apt install gcc clang`

CMake: 3.24+: [official APT repository](https://apt.kitware.com/)

CUDA 11.8: [Download](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local) deb(local). Open3D `make install` corruptted at CUDA-12

Then set cuda path
```shell
# Add to bash or zsh

# Open3D cuda-11.8
export PATH="/usr/local/cuda-11.8/bin:$PATH"
export LD_LIBRARY_PATH="/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH"
```

Install librealsense from [git-doc](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md), `hwloc` for open3d compile with realsense

```shell
sudo apt-get install librealsense2-dkms librealsense2-utils librealsense2-dev librealsense2-dbg
sudo apt-get -y install hwloc
```

Torch(optional): virtual env recommended

Import error on python3.9+ at [issues](https://github.com/isl-org/Open3D/issues/4917#issuecomment-1076992720)


```shell
sudo apt-get install build-essential gdb lcov pkg-config \
    libbz2-dev libffi-dev libgdbm-dev \
    libgdbm-compat-dev liblzma-dev \
    libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
    lzma lzma-dev tk-dev uuid-dev zlib1g-dev libmpdec-dev

wget https://www.python.org/ftp/python/3.9.8/Python-3.9.8.tgz
tar -xf Python-3.9.8.tgz
cd Python-3.9.8
./configure --enable-optimizations
make && sudo make install
# /usr/local/bin/python3.9
```


```shell
# 1. Clone Open3D and Open3D-ML
cd
git clone https://github.com/isl-org/Open3D.git
git clone https://github.com/isl-org/Open3D-ML.git

# Optional: create open3d venv for python
# missing 'yapf' in making wheel
virtualenv -p python3.9 venv/open3d
source venv/open3d/bin/activate
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip3 install yapf

# 2. Config
cd Open3D
./util/install_deps_ubuntu.sh
mkdir build
cd build
cmake -DBUILD_CUDA_MODULE=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DPython3_ROOT=$HOME/venv/open3d/bin/python3 \
    -DCMAKE_INSTALL_PREFIX=$HOME/open3d_install \
    -DGLIBCXX_USE_CXX11_ABI=OFF \
    -DBUILD_PYTORCH_OPS=ON \
    -DBUILD_TENSORFLOW_OPS=OFF \
    -DBUNDLE_OPEN3D_ML=ON \
    -DOPEN3D_ML_ROOT=$HOME/Open3D-ML \
    -DBUILD_LIBREALSENSE=ON \
    -DUSE_SYSTEM_LIBREALSENSE=ON \
    ..


# 3. Make and install
make -j$(nproc) && make install

# 4.a Build python wheel to install open3d-binding
# wheel loc in ~/Open3D/build/lib/python_package/pip_package
make pip-package
cd lib/python_package/pip_package
pip3 install open3d-xxx.whl

# 4.b Install in current env
make install-pip-package

```

# 2. Reconstrcution

```shell
~/venv/open3d/bin/activate
cp -r ~/venv/open3d/lib/python3.9/site-packages/open3d/examples Project\open3d-exp
python reconstruction_system/run_system.py --make --register --refine --integrate --config 'reconstruction_system/config/realsense.json' --device cuda:0
```

