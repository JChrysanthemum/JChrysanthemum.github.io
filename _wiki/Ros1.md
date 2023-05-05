---
layout: wiki
title: Ros 1
cate1: Memo
cate2:
description: Ros Common CMD
keywords: Robot
date: [2023-04-20]
type:
link:
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---

## Common Command Table

 Mean | Command
---|---
 wstool update | wstool merge -t src PATH_TO_ROSINSTALL_FILE.rosinstall
 make together | ./src/catkin/bin/catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic install 
 make specific together |  ./src/catkin/bin/catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic --only-pkg-with-deps <package1> install
 make individual | ./src/catkin/bin/catkin_make_isolated  --install-space=/opt/ros/melodic --install
 make specific indivdual | ./src/catkin/bin/catkin_make_isolated  --install-space=/opt/ros/melodic --pkg  <package1>  --install
 rosdep install only apt | rosdep install --from-paths src --ignore-src -r -y --skip-keys python --skip-keys gazebo



