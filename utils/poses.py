import copy

from utils.objects import Object


class POSES:
    # default home setting
    BASE = 0
    SHOULDER = -1.57
    ELBOW = 0
    WRIST_1 = -1.57
    WRIST_2 = 0
    WRIST_3 = 0

    # POSES IN LINEAR SPACE
    HOME = [BASE, SHOULDER, ELBOW, WRIST_1, WRIST_2, WRIST_3]
    # comments from their code - # pi/2, -1.7947, 1.2356, pi -1.033, -pi/2 which is -1.5710, 0.0051
    COMFORTABLE_POSE = [0, -1.9049, 1.9520, -1.6088, -3.14 / 2, 0]
    PICKUP_POSE = [0, -1.57, 1.57, -1.57, -1.57, 0]

    # POSES IN TCP SPACE
    # Z in this positions is fucked up
    COMFORTABLE_TCP_POSE = [-0.347, -0.109, 0.35, 2.22, 2.22, 0]

    ABOVE_PAYLOAD_TCP_POSE_1 = [-0.6, -0.109, 0.35, 2.22, 2.22, 0]
    LOWER_PAYLOAD_TCP_POSE_1 = [-0.6, -0.109, 0.15, 2.22, 2.22, 0]
    ENGAGEMENT_TCP_POSE_1 = [-0.6, -0.109, -0.04, 2.22, 2.22, 0]

    # TODO: add above and engagement poses for second location
    ABOVE_PAYLOAD_TCP_POSE_2 = [-0.6, 0.2, 0.35, 2.22, 2.22, 0]
    LOWER_PAYLOAD_TCP_POSE_2 = [-0.6, 0.2, 0.15, 2.22, 2.22, 0]
    ENGAGEMENT_TCP_POSE_2 = [-0.6, 0.2, -0.04, 2.22, 2.22, 0]

    @staticmethod
    def get_engagement_pose(gripper, obj: Object, pose_number: int):
        if pose_number == 1:
            pose = copy.copy(POSES.ENGAGEMENT_TCP_POSE_1)
        else:
            pose = copy.copy(POSES.ENGAGEMENT_TCP_POSE_2)
        pose[2] += gripper.height + obj.height
        return pose
