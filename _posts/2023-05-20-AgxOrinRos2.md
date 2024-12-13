---
layout: post
title: Jetson AGX Orin ROS 2 Set-up
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

**Preparation**: Nvidia Agx Orin setup, details in [Jetson AGX Orin Set-up](https://jchrysanthemum.github.io/2023/04/21/AgxOrin/).

Official [link](https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html)

# Install development tools and ROS tools

**Optional** : Clean up ros-depended python packages and ros1-depended debian packages. If you have ros1 installed and do not clean up, `dpkg error` will report confict.

```shell
pip3 freeze | grep ros | xargs sudo pip3 uninstall -y
pip3 freeze | grep catkin | xargs sudo  pip3 uninstall -y
sudo apt uninstall python3-rospkg python3-catkin-pkg
sudo rm /etc/ros/rosdep/sources.list.d/20-default.list
```

Install common packages.

```shell
sudo apt update && sudo apt install -y \
  python3-flake8-docstrings \
  python3-pip \
  python3-pytest-cov \
  ros-dev-tools

sudo pip3 install -U \
  flake8-blind-except \
  flake8-builtins \
  flake8-class-newline \
  flake8-comprehensions \
  flake8-deprecated \
  flake8-import-order \
  flake8-quotes \
  "pytest>=5.3" \
  pytest-repeat \
  pytest-rerunfailures
```

Init rosdep and install dependcies.

```shell
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers"
```

Build from colon
```shell
colcon build --symlink-install
```

However, it throws `python_orocos_kdl_vendor Could NOT find Python3 (missing: Python3_LIBRARIES Python3_INCLUDE_DIRS Development)`

So, I rebuild them py passing python3 location:

```shell
colcon build --symlink-install  --cmake-args \
-DPython3_EXECUTABLE=/usr/bin/python3 \
--packages-up-to python_orocos_kdl_vendor
```


```shell
colcon build --symlink-install --cmake-args \
-DPYTHON_INCLUDE_DIR=$(python3 -c "import sysconfig; print(sysconfig.get_path('include'))")  \
-DPYTHON_LIBRARY=$(python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
```