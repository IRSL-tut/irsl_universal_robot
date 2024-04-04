#!/bin/bash

# this script should be executed inside docker container

source /irsl_entryrc

roslaunch irsl_choreonoid_ros run_sim_with_setup_cnoid.launch \
          python_script:="--python $(rospack find ur5e_robot)/launch/setup_cnoid.py" \
          control_namespace:=/ur5e \
          model_namespace:=ur5e_ros \
          model_file:="$(rospack find ur5e_robot)/model/ur5e.urdf" \
          controllers:='joint_state_controller trajectory_controller gripper_controller'
