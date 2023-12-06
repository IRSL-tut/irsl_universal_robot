#### import irsl
import irsl_choreonoid.robot_util as ru

class UR5EModel(ru.RobotModelWrapped):
    def __init__(self, robot):
        import irsl_choreonoid.robot_util as ru
        import math
        super().__init__(robot)
        self.registerEndEffector('arm', ## end-effector
                                 'wrist_3_link', ## tip-link
                                 tip_link_to_eef = ru.make_coordinates({'pos': [0, 0, 0.07], 'angle-axis': [0, 1, 0, math.pi]}),
                                 joint_tuples = (('shoulder_pan_joint',  'shoulder-y'),
                                                 ('shoulder_lift_joint', 'shoulder-p'),
                                                 ('elbow_joint',         'elbow-p'),
                                                 ('wrist_1_joint',       'wrist-p'),
                                                 ('wrist_2_joint',       'wrist-r'),
                                                 ('wrist_3_joint',       'wrist-y'),
                                                 )
                                 )
        #self.registerEndEffector('hand', ## end-effector
        #                         'left_hand_palm_link', ## tip-link
        #                         tip_link_to_eef = irsl_choreonoid.robot_util.make_coordinates({'pos': [0, 0, 0.07], 'angle-axis': [0, 1, 0, math.pi]}),
        #                         joint_tuples = (('left_shoulder_yaw',   'shoulder-y'),
        #                                         ('left_shoulder_pitch', 'shoulder-p'),
        #                                         ('left_elbow_pitch',    'elbow-p'),
        #                                         ('left_wrist_yaw',      'wrist-y'),
        #                                         ('left_wrist_pitch',    'wrist-p'),
        #                                         ('left_hand_yaw',       'hand-y'),
        #                                         )
        #                         )
        self.registerNamedPose('initial',
                               [0, 0, 0, 0, 0, 0, ])
        self.registerNamedPose('default',
                               [0, 0, 0, 0, 0, 0, ])
        self.registerNamedPose('manip',
                               [0, 0, 0, 0, 0, 0, ])
        self.setDefaultPose()

    def setManipPose(self):
        self.setNamedPose('manip')

    @property
    def hand(self):
        return self.getLimb('hand')
    @property
    def gripper(self):
        return self.getLimb('hand')
