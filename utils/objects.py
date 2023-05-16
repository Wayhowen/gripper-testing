class Object:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class OBJECTS:
    PAYLOAD_BOX = Object("Payload box", 0.041)
    GLASS_BALL = Object("Glass ball", 0.055) # value changed from 0.035 to improve soft gripper capabilities
    REPEATABILITY_GLASS_BALL = Object("Glass ball", 0.06)
    HEDGEHOG = Object("Hedgehog", 0.03) # value changed from 0.02 to improve soft gripper capabilities
    MEDIUM_BALL = Object("Hedgehog", 0.04)  # value changed from 0.02 to improve soft gripper capabilities

    # TODO: measure those
    EGG = Object("Egg", 0.03)
    OSMAN = Object("Osman", 0.03)
    BALL = Object("Ball", 0.03)

