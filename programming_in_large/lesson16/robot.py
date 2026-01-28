from __future__ import annotations

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, List


class MoveStatus:
    OK = "MOVE_OK"
    BARRIER = "HIT_BARRIER"


class TurnStatus:
    OK = "TURN_OK"


class StateStatus:
    OK = "STATE_OK"
    NO_WATER = "OUT_OF_WATER"
    NO_SOAP = "OUT_OF_SOAP"


WATER = 1
SOAP = 2
BRUSH = 3


@dataclass
class RobotState:
    x: float
    y: float
    angle: float
    mode: int


@dataclass
class MoveResponse:
    distance: float
    status: str


@dataclass
class TurnResponse:
    angle: float
    status: str


@dataclass(frozen=True)
class StateResponse:
    mode: int
    status: str


def _check_position(x: float, y: float) -> tuple[float, float, str]:
    constrained_x = max(0, min(100, x))
    constrained_y = max(0, min(100, y))

    if x == constrained_x and y == constrained_y:
        return (x, y, MoveStatus.OK)
    return (constrained_x, constrained_y, MoveStatus.BARRIER)


def _check_resources(new_mode: int) -> str:
    if new_mode == WATER:
        return StateStatus.NO_WATER
    if new_mode == SOAP:
        return StateStatus.NO_SOAP
    return StateStatus.OK


def _execute_move(dist: float, old_state: RobotState, log: List[str]):
    angle_rads = old_state.angle * (math.pi / 180.0)
    new_x = old_state.x + dist * math.cos(angle_rads)
    new_y = old_state.y + dist * math.sin(angle_rads)

    constrained_x, constrained_y, status = _check_position(new_x, new_y)
    new_state = RobotState(
        constrained_x, constrained_y, old_state.angle, old_state.mode
    )

    moved = math.hypot(constrained_x - old_state.x, constrained_y - old_state.y)
    message = (
        f"POS({int(constrained_x)},{int(constrained_y)})"
        if status == MoveStatus.OK
        else f"HIT_BARRIER at ({int(constrained_x)},{int(constrained_y)})"
    )
    response = MoveResponse(distance=moved, status=status)
    return new_state, log + [message], response


def _execute_turn(angle: float, old_state: RobotState, log: List[str]):
    new_state = RobotState(
        old_state.x, old_state.y, old_state.angle + angle, old_state.mode
    )
    response = TurnResponse(angle=angle, status=TurnStatus.OK)
    return new_state, log + [f"ANGLE {new_state.angle}"], response


def _execute_set_state(new_mode: int, old_state: RobotState, log: List[str]):
    resource_status = _check_resources(new_mode)
    if resource_status != StateStatus.OK:
        response = StateResponse(mode=new_mode, status=resource_status)
        return old_state, log + [f"RESOURCE ERROR: {resource_status}"], response
    new_state = RobotState(old_state.x, old_state.y, old_state.angle, new_mode)
    response = StateResponse(mode=new_mode, status=StateStatus.OK)
    return new_state, log + [f"STATE {new_mode}"], response


class Command(ABC):
    @abstractmethod
    def interpret(self, state: RobotState, log: List[str]):
        pass


class Stop(Command):
    def interpret(self, state: RobotState, log: List[str]):
        return state, log


class Move(Command):
    def __init__(self, distance: float, next_cmd: Callable[[MoveResponse], Command]):
        self.distance = distance
        self.next_cmd = next_cmd

    def interpret(self, state: RobotState, log: List[str]):
        new_state, new_log, response = _execute_move(self.distance, state, log)
        return self.next_cmd(response).interpret(new_state, new_log)


class Turn(Command):
    def __init__(self, angle: float, next_cmd: Callable[[TurnResponse], Command]):
        self.angle = angle
        self.next_cmd = next_cmd

    def interpret(self, state: RobotState, log: List[str]):
        new_state, new_log, response = _execute_turn(self.angle, state, log)
        return self.next_cmd(response).interpret(new_state, new_log)


class SetState(Command):
    def __init__(self, mode: int, next_cmd: Callable[[StateResponse], Command]):
        self.mode = mode
        self.next_cmd = next_cmd

    def interpret(self, state: RobotState, log: List[str]):
        new_state, new_log, response = _execute_set_state(self.mode, state, log)
        return self.next_cmd(response).interpret(new_state, new_log)


def program() -> Command:
    return Move(
        150,
        lambda move_resp: Turn(
            -90,
            lambda turn_resp: SetState(
                SOAP if move_resp.status == MoveStatus.OK else BRUSH,
                lambda state_resp: Move(
                    50 if state_resp.status == StateStatus.OK else 10,
                    lambda _final_resp: Stop(),
                ),
            ),
        ),
    )


if __name__ == "__main__":
    initial = RobotState(0.0, 0.0, 0, WATER)
    final_state, log = program().interpret(initial, [])
    print(f"Final state: {final_state}")
    print(f"Log: {log}")
