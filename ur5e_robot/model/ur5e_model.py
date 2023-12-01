#### import irsl
import irsl_choreonoid.robot_util
import math

class UR5EModel(irsl_choreonoid.robot_util.RobotModelWrapped):
    def __init__(self, robot):
        super().__init__(robot)
        self.registerEndEffector('arm', ## end-effector
                                 'left_hand_palm_link', ## tip-link
                                 tip_link_to_eef = irsl_choreonoid.robot_util.make_coordinates({'pos': [0, 0, 0.07], 'angle-axis': [0, 1, 0, math.pi]}),
                                 joint_tuples = (('left_shoulder_yaw',   'shoulder-y'),
                                                 ('left_shoulder_pitch', 'shoulder-p'),
                                                 ('left_elbow_pitch',    'elbow-p'),
                                                 ('left_wrist_yaw',      'wrist-y'),
                                                 ('left_wrist_pitch',    'wrist-p'),
                                                 ('left_hand_yaw',       'hand-y'),
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
    @property
    def hand(self):
        return self.getLimb('hand')
    @property
    def gripper(self):
        return self.getLimb('hand')
