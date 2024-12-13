---
layout: post
title: Complie ros on raspbian for turtle bot
categories: [Robot]
description: 
keywords: ros
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---



# Install all from source (git)

Official [recommend](https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup) use `Ubuntu server` to install ros and other package from `apt`. However, this may cause problem below:

+ 4B+ only with 20.04 LTS, old os will be refused on boot.
+ Install UI (gnome etc) will cause wierd lag, even in opening a simple image sometimes.

So I want to build turtle on Raspbian.

## Prepartion

You need to install Raspbian on Pi4, and install ROS from source.[Official step 1-13]

## Installation

They install these package by `apt`:`rosserial-python`, `tf`,`hls-lfcd-lds-driver`, `turtlebot3-msgs` and `dynamixel-sdk`.

You can check if you have installed one of them by:
```bash
rospack list | grep -e hls-lfcd-lds-driver -e turtlebot3-msgs -e dynamixel-sdk -e rosserial-python 
-e tf
```
Then you can install them from src. A guide about install package from source [here](https://answers.ros.org/question/252478/how-to-build-a-package-from-source-on-ubuntu-mate-1604-lts-and-ros-kinetic/).

And you could install part of package ONLY IF you know you will not use other part in this package. Just like turtle3 on Pi remove three packages. **Not recommend for beginers**

### Git repo list (from melodic branch)

tf (geometry: angles | eigen_conversions | kdl_conversions | **tf** | tf_conversions)
```bash
git clone -b melodic-devel https://github.com/ros/geometry.git
```

rosserial_python (rosserial: rosserial_client | rosserial_msgs | **rosserial_python**)
```bash
git clone -b melodic-devel https://github.com/ros-drivers/rosserial.git
```

hls_lfcd_lds_driver
```bash
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git
```

turtlebot3_msgs
```bash
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
```

dynamixel_sdk
```bash
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/DynamixelSDK.git
```

turtlebot3 (**turtlebot3**: turtlebot3_bringup | turtlebot3_description | turtlebot3_example | turtlebot3_navigation | turtlebot3_slam | turtlebot3_teleop)
```bash
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
cd turtlebot3
```

Note: If you could not access github by xx, 1). Use github mirror like `https://gitclone.com/` 2). V2ray + proxychains4 for HTTP

NoteL: turtlebot3_msgs error 
```bash
CMake Error at /home/pi/ros_catkin_ws/build_isolated/turtlebot3_msgs/cmake/turtlebot3_msgs-genmsg.cmake:3 (message):
  Could not find messages which
  '/home/pi/ros_catkin_ws/src/turtlebot3_msgs/msg/SensorState.msg' depends
  on.  Did you forget to specify generate_messages(DEPENDENCIES ...)?

  Cannot locate message [Header] in package [std_msgs] with paths
  [['/home/pi/ros_catkin_ws/devel_isolated/std_msgs/share/std_msgs/cmake/../msg']]
Call Stack (most recent call first):
  /home/pi/ros_catkin_ws/devel_isolated/genmsg/share/genmsg/cmake/genmsg-extras.cmake:307 (include)
  CMakeLists.txt:29 (generate_messages)
```
I find a simple solution from [Ros Answer](https://answers.ros.org/question/221532/indigo-ros_core-source-compile-error-in-actionlib_msgs/), not create a soft link but copy all folder to dest.

```bash
cp -r src/std_msgs/msg /home/pi/ros_catkin_ws/devel_isolated/std_msgs/share/std_msgs/cmake/../msg
```
