class Object:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class OBJECTS:
    PAYLOAD_BOX = Object("Payload box", 0.03)

    # TODO: measure those
    EGG = Object("Egg", 0.03)
    OSMAN = Object("Osman", 0.03)
    BALL = Object("Ball", 0.03)

