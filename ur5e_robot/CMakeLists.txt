cmake_minimum_required(VERSION 3.0.2)
cmake_policy(SET CMP0003 NEW)
cmake_policy(SET CMP0057 NEW)

project(ur5e_robot)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY model
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)
