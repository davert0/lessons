import math
from collections import namedtuple
from typing import Callable, Dict, List, Tuple


class MoveResponse:
    OK = "MOVE_OK"
    BARRIER = "HIT_BARRIER"


class SetStateResponse:
    OK = "STATE_OK"
    NO_WATER = "OUT_OF_WATER"
    NO_SOAP = "OUT_OF_SOAP"


RobotState = namedtuple("RobotState", "x y angle state")

Capability = Dict[str, Callable]

WATER = 1
SOAP = 2
BRUSH = 3


def check_position(x: float, y: float) -> tuple[float, float, str]:
    constrained_x = max(0, min(100, x))
    constrained_y = max(0, min(100, y))

    if x == constrained_x and y == constrained_y:
        return (x, y, MoveResponse.OK)
    return (constrained_x, constrained_y, MoveResponse.BARRIER)


def check_resources(new_mode: int) -> SetStateResponse:
    if new_mode == WATER:
        # ....
        return SetStateResponse.NO_WATER
    if new_mode == SOAP:
        # ....
        return SetStateResponse.NO_SOAP
    return SetStateResponse.OK


def move(dist, old_state, log):
    angle_rads = old_state.angle * (math.pi / 180.0)
    new_x = old_state.x + dist * math.cos(angle_rads)
    new_y = old_state.y + dist * math.sin(angle_rads)

    constrained_x, constrained_y, move_result = check_position(new_x, new_y)

    new_state = RobotState(
        constrained_x, constrained_y, old_state.angle, old_state.state
    )

    message = (
        f"POS({int(constrained_x)},{int(constrained_y)})"
        if move_result == MoveResponse.OK
        else f"HIT_BARRIER at ({int(constrained_x)},{int(constrained_y)})"
    )

    return new_state, log + [message], move_result


def turn(angle, old_state, log):
    new_state = RobotState(
        old_state.x, old_state.y, old_state.angle + angle, old_state.state
    )
    return new_state, log + [f"ANGLE {new_state.angle}"], MoveResponse.OK


def set_state(new_mode, old_state, log):
    resource_check = check_resources(new_mode)

    if resource_check != SetStateResponse.OK:
        message = f"RESOURCE ERROR: {resource_check} for mode {new_mode}"
        return old_state, log + [message], resource_check

    new_state = RobotState(old_state.x, old_state.y, old_state.angle, new_mode)
    return new_state, log + [f"STATE {new_mode}"], SetStateResponse.OK


def _state_capabilities(
    state: RobotState,
    log: List[str],
    can_move: bool,
) -> Capability:
    def _with_state(
        new_state: RobotState,
        new_log: List[str],
        next_can_move: bool,
    ) -> Capability:
        return _state_capabilities(new_state, new_log, next_can_move)

    def _move(dist: float) -> Tuple[Capability, str]:
        new_state, new_log, move_result = move(dist, state, log)
        next_can_move = move_result == MoveResponse.OK
        return _with_state(new_state, new_log, next_can_move), move_result

    def _turn(angle: float) -> Tuple[Capability, str]:
        new_state, new_log, turn_result = turn(angle, state, log)
        return _with_state(new_state, new_log, True), turn_result

    def _set_mode(new_mode: int) -> Tuple[Capability, str]:
        new_state, new_log, result = set_state(new_mode, state, log)
        return _with_state(new_state, new_log, can_move), result

    def _report() -> Tuple[RobotState, List[str]]:
        return state, list(log)

    caps: Capability = {"turn": _turn, "report": _report}
    if can_move:
        caps["move"] = _move
    if check_resources(WATER) == SetStateResponse.OK:
        caps["set_water"] = lambda: _set_mode(WATER)
    if check_resources(SOAP) == SetStateResponse.OK:
        caps["set_soap"] = lambda: _set_mode(SOAP)
    caps["set_brush"] = lambda: _set_mode(BRUSH)
    return caps


def init(initial_state: RobotState) -> Capability:
    _, _, allowed_move = check_position(initial_state.x, initial_state.y)
    return _state_capabilities(initial_state, [], allowed_move == MoveResponse.OK)


caps = init(RobotState(0.0, 0.0, 0, WATER))

if "move" in caps:
    caps, _ = caps["move"](150)
if "set_soap" in caps:
    caps, _ = caps["set_soap"]()
if "turn" in caps:
    caps, _ = caps["turn"](-90)
if "move" in caps:
    caps, _ = caps["move"](50)
