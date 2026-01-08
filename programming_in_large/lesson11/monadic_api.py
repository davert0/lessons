import pure_robot


_DEFAULT_STATE = pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER)
_current_state = _DEFAULT_STATE
_transfer = pure_robot.transfer_to_cleaner

WATER = pure_robot.WATER
SOAP = pure_robot.SOAP
BRUSH = pure_robot.BRUSH


class RobotAction:
    def __init__(self, func):
        self._func = func

    def _apply(self):
        global _current_state
        _current_state = self._func(_transfer, _current_state)

    def __rshift__(self, other):
        _apply_action(self)
        return _Chain() >> other


class _Chain:
    def __rshift__(self, other):
        _apply_action(other)
        return self


def _apply_action(action):
    if not isinstance(action, RobotAction):
        raise TypeError("Expected RobotAction to chain with '>>'")
    action._apply()


def _normalize_state(new_state):
    if new_state == WATER:
        return "water"
    if new_state == SOAP:
        return "soap"
    if new_state == BRUSH:
        return "brush"
    return new_state


def move(dist):
    return RobotAction(lambda transfer, state: pure_robot.move(transfer, dist, state))


def turn(angle):
    return RobotAction(lambda transfer, state: pure_robot.turn(transfer, angle, state))


def set_state(new_state):
    normalized = _normalize_state(new_state)
    return RobotAction(
        lambda transfer, state: pure_robot.set_state(transfer, normalized, state)
    )


def start():
    return RobotAction(lambda transfer, state: pure_robot.start(transfer, state))


def stop():
    return RobotAction(lambda transfer, state: pure_robot.stop(transfer, state))


def reset_state(state=None):
    global _current_state
    _current_state = _DEFAULT_STATE if state is None else state


def set_transfer(transfer):
    global _transfer
    _transfer = transfer
