#ARG BASE_IMAGE=repo.irsl.eiiris.tut.ac.jp/irsl_system:noetic
ARG BASE_IMAGE=irslrepo/irsl_system:noetic

FROM ${BASE_IMAGE}

LABEL maintainer "IRSL-tut (https://github.com/IRSL-tut) <faculty@irsl.eiiris.tut.ac.jp>"

SHELL ["/bin/bash", "-c"]

WORKDIR /ur5e_ws

RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    wstool init src && \
    wstool set universal_robot https://github.com/ros-industrial/universal_robot.git  -v 1.3.1 -y -t src --git && \
    wstool update -t src

RUN apt update -q -qq && \
    rosdep update -y -q -r && \
    rosdep install -y -q -r --ignore-src --from-path src && \
    apt clean && \
    rm -rf /var/lib/apt/lists/

COPY ur5e_robot /ur5e_ws/src/ur5e_robot

RUN source /choreonoid_ws/install/setup.bash && catkin build ur_description ur5e_robot
