import pure_robot
from functional_cleaner_api import build_cleaner_api, half_move_adapter

api = build_cleaner_api(
    transfer=pure_robot.transfer_to_cleaner,
    move_fn=half_move_adapter(pure_robot.move),
    turn_fn=pure_robot.turn,
    set_state_fn=pure_robot.set_state,
    start_fn=pure_robot.start,
    stop_fn=pure_robot.stop,
)

api["activate_cleaner"]((
    'move 100',
    'turn -90',
    'set soap',
    'start',
    'move 50',
    'stop'
))

print(api["get_x"](), api["get_y"](), api["get_angle"](), api["get_state"]())