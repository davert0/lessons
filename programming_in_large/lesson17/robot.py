import math
from dataclasses import dataclass


@dataclass
class RobotState:
    x: float
    y: float
    angle: float
    state: int


class Robot:
    def __init__(self, transfer, state):
        self.transfer = transfer
        self.state = state

    def move(self, dist) -> "Robot":
        angle_rads = self.state.angle * (math.pi / 180.0)
        new_state = RobotState(
            self.state.x + dist * math.cos(angle_rads),
            self.state.y + dist * math.sin(angle_rads),
            self.state.angle,
            self.state.state,
        )
        self.transfer(("POS(", new_state.x, ",", new_state.y, ")"))
        return Robot(self.transfer, new_state)

    def turn(self, turn_angle) -> "Robot":
        new_state = RobotState(
            self.state.x, self.state.y, self.state.angle + turn_angle, self.state.state
        )
        self.transfer(("ANGLE", new_state.angle))
        return Robot(self.transfer, new_state)

    def set_state(
        self,
        new_state,
    ) -> "Robot":
        new_state = RobotState(self.state.x, self.state.y, self.state.angle, new_state)
        self.transfer(("SET_STATE", new_state))

        return Robot(self.transfer, new_state)

    def get_state(self) -> RobotState:
        return self.state
