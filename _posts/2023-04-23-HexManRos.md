---
layout: post
title: Ros setup for package of HexMan platform
categories: [Robot]
description: 
keywords: diy
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---


**Preparation**: Nvidia Agx Orin setup, details in [Jetson AGX Orin Set-up](https://jchrysanthemum.github.io/2023/04/21/AgxOrin/)

# 1. XRos (Ros packages for Hexman)

Their packages is not freindly to ros green-hand like me, limited documentation. :(

So, I tried myself to give more explanation.

The structure of XROS
```
├── BASE
│   ├── xpkg_comm
│   └── xpkg_vehicle
├── BRINGUP
│   └── xpkg_bringup
├── URDF
│   ├── xpkg_urdf_echo
│   ├── xpkg_urdf_echo_plus
│   ├── xpkg_urdf_mark1_diff
│   ├── xpkg_urdf_mark1_mcnm
│   ├── xpkg_urdf_mark2_mcnm
│   ├── xpkg_urdf_ray
│   └── xpkg_urdf_york
```

I copy the packages under *BASE* and *BRINGUP* into `catkin/src`, here is the CMD to build them.

```shell
./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release \
 --pkg xpkg_bringup xpkg_comm xpkg_vehicle
```

Files in `URDF` were ignored since there is no need for using gazebo.

# 2. SLAM with realsense

I followed the offcial tutorial [SLAM-with-D435i](https://github.com/IntelRealSense/realsense-ros/wiki/SLAM-with-D435i). First, four packages are required: `realsense2_camera`, `imu_filter_madgwick`, `rtabmap_ros`, `robot_localization`. use `rospack find` to check if they were installed

```shell
rospack find realsense2_camera
rospack find imu_filter_madgwick
rospack find rtabmap_ros
rospack find robot_localization
```

Except for `realsense2_camera`, they throw message like `[rospack] Error: package 'imu_filter_madgwick' not found
`. So I need to install them one by one.

First, `robot_localization`

```shell
export ROS_PACKAGE_PATH=$HOME/ros_catkin_ws/src

rosinstall_generator  robot_localization --rosdistro noetic --deps --exclude RPP \
| vcs import src

sudo apt install libgeographic-dev libbullet-dev -y

./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release \
--merge --pkg geographic_msgs uuid_msgs  robot_localization 
```
Then, `rtabmap_ros` and their dependices.


```shell
rosinstall_generator  rtabmap_ros octomap octomap_msgs octomap_rviz_plugins --rosdistro noetic --deps --exclude RPP \
| vcs import src

./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --merge --pkg \
pcl_conversions pcl_msgs pcl_ros tf2 tf2_eigen tf2_sensor_msgs image_geometry rtabmap \
rtabmap_conversions rtabmap_msgs rtabmap_util octomap octomap_msgs

./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --merge --pkg \
move_base_msgs costmap_2d voxel_grid octomap_rviz_plugins rtabmap_rviz_plugins \
rtabmap_costmap_plugins rtabmap_demos rtabmap_ros rtabmap_examples rtabmap_launch \
rtabmap_legacy rtabmap_odom rtabmap_python rtabmap_slam rtabmap_sync rtabmap_viz   
```

Once, `rtabmap_util` throws that  `octomap_msgs` can not find a head file in `octomap` ('octomap/AbstractOcTree.h'), however, the `src`, `devel_isolated/include/octomap` and `install_isolated/include/octomap` has this file already. Then, I unset the `ROS_PACKAGE_PATH` and other ROS ENV, it works.

`imu_tools`

```shell
rosinstall_generator imu_tools --rosdistro noetic --deps \
--exclude RPP | vcs import src

./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release \
--merge --pkg imu_complementary_filter imu_filter_madgwick rviz_imu_plugin
```

Here we can have a try on realsense's tracking.

```shell
roslaunch realsense2_camera opensource_tracking.launch
```

Only a little fix is needed:
Rviz|Launch File|Value
----|----|----
Image.ImageTopic|rgb_topic|/camera/color/image_raw
DepthCloud.DepthMapTopic|depth_topic|/camera/aligned_depth_to_color/image_raw
DepthCloud.ColorImageTopic|camera_info_topic|/camera/color/camera_info
 
Save before closing. If you want all raw message :

```shell
rosbag record -O my_bagfile_1.bag /camera/aligned_depth_to_color/camera_info \
/camera/aligned_depth_to_color/image_raw /camera/color/camera_info /camera/color/image_raw \
/camera/imu /camera/imu_info /tf_static  /odom
```
/sensor_msgs/PointCloud2

Or, only cloud point .
```shell
rosbag record -O my_bagfile_1.bag /camera/aligned_depth_to_color/camera_info \
/camera/color/camera_info /camera/color/image_raw \
/camera/imu /camera/imu_info /tf_static
```

```shell
roscore >/dev/null 2>&1 &
rosparam set use_sim_time true
rosbag play my_bagfile_1.bag --clock
roslaunch realsense2_camera opensource_tracking.launch offline:=true
```

<!-- rosrun tf static_transform_publisher 0 0 0.07 0 0 0 base_link odom 100 -->
