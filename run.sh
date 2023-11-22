#!/bin/bash
## ./run.sh -w $(pwd) --image irslrepo/irsl_universal_robot:noetic --ros-setup /ur5e_ws/devel/setup.bash

.irsl_docker/run.sh -w $(pwd) --image irslrepo/irsl_universal_robot:noetic --ros-setup /ur5e_ws/devel/setup.bash $@
