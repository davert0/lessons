from pure_robot import RobotState, WATER


def build_cleaner_api(
    *,
    transfer,
    move_fn,
    turn_fn,
    set_state_fn,
    start_fn,
    stop_fn
):
    state = RobotState(0.0, 0.0, 0, WATER)

    def activate_cleaner(code):
        nonlocal state
        for command in code:
            cmd = command.split(' ')
            if cmd[0] == 'move':
                state = move_fn(transfer, int(cmd[1]), state)
            elif cmd[0] == 'turn':
                state = turn_fn(transfer, int(cmd[1]), state)
            elif cmd[0] == 'set':
                state = set_state_fn(transfer, cmd[1], state)
            elif cmd[0] == 'start':
                state = start_fn(transfer, state)
            elif cmd[0] == 'stop':
                state = stop_fn(transfer, state)

    def get_x():
        return state.x

    def get_y():
        return state.y

    def get_angle():
        return state.angle

    def get_state():
        return state.state

    return {
        "activate_cleaner": activate_cleaner,
        "get_x": get_x,
        "get_y": get_y,
        "get_angle": get_angle,
        "get_state": get_state,
    }

def half_move_adapter(move_fn):
    def half_move(transfer, dist, state):
        return move_fn(transfer, dist / 2, state)
    return half_move