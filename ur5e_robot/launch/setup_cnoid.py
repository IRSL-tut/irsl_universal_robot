from irsl_choreonoid_ros.setup_cnoid import SetupCnoid

cnoid = SetupCnoid()
cnoid.createCnoidFromYaml('package://ur5e_robot/launch/depot_ros_world.yaml')

### launch spawner??
