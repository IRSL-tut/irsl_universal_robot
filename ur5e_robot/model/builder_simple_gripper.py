# jupyter console --kernel=choreonoid
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

### simple gripper
plate_t=0.005
gripper_t=0.03
default_open=0.03
servo_color=(0.3, 0.3, 0.3)
finger_color=(0.4, 0.8, 0.8)
fixed_color=(0.4, 0.8, 0.8)
rb = RobotBuilder()
#
sv = rb.makeBox(0.0465, 0.034, 0.0285, color=servo_color)
sv.translate(fv(-0.012, -0.017, 0))
sv_cds=coordinates().rotate(PI/2, coordinates.X).rotate(PI/2, coordinates.Y)
sv.transform(sv_cds, coordinates.wrt.world)
##
fp0=rb.makeBox(0.04, plate_t, gripper_t, color=fixed_color)
fp0.translate(fv(0.1 - 0.04/2 + 0.01, -plate_t/2 - default_open, -gripper_t/2))
##
fp1=rb.makeBox(0.04, plate_t, gripper_t, color=fixed_color)
fp1.translate(fv(0.05, -plate_t/2 - default_open, -gripper_t/2))
cds=coordinates(fv(0.07, -default_open, 0))
tr=cds.transformation(fp1)
cds.rotate(0.3, coordinates.Z)
cds.transform(tr)
fp1.newcoords(cds)
##
fp2=rb.makeBox(0.05, plate_t, gripper_t, color=fixed_color)
fp2.translate(fv(0.011, -plate_t/2 - default_open - 0.0115, -gripper_t/2))
l_root = rb.createLinkFromShape(name='ROOT_FRAME', root=True, density=500.0)

## finger
f0=rb.makeBox(0.03, plate_t, gripper_t, color=finger_color)
f0.translate(fv(0.1 - 0.03/2, plate_t/2, -gripper_t/2))
#
f1=rb.makeBox(0.01, plate_t, gripper_t, color=finger_color)
f1.translate(fv(0.1 + 0.01/2, plate_t/2, -gripper_t/2))
# f1.rotate(0.3, coordinates.Z, coordinates(fv(0.1, 0, 0)))
cds=coordinates(fv(0.1, 0, 0))
tr=cds.transformation(f1)
cds.rotate(0.3, coordinates.Z)
cds.transform(tr)
f1.newcoords(cds)
#
f2=rb.makeBox(0.05, plate_t, gripper_t, color=finger_color)
f2.translate(fv(0.02 + 0.05/2, plate_t/2, -gripper_t/2))
cds=coordinates(fv(0.07, 0, 0))
tr=cds.transformation(f2)
cds.rotate(-0.3, coordinates.Z)
cds.transform(tr)
f2.newcoords(cds)
#
j0=rb.createJointShape(jointType=Link.JointType.RevoluteJoint)
j0.transform(sv_cds)
l0=rb.createLinkFromShape(name='FINGER0', parentLink=l_root, density=400.0, JointId=0, JointName='finger_joint0',
                          JointRange=[-PI, PI], JointVelocityRange=[-PI*10, PI*10], JointEffortRange=[-100, 100], EquivalentRotorInertia=0.05)

rb.exportBody('/tmp/simple_gripper.body', modelName='simple_gripper')
