from functools import reduce
from programming_in_large.lesson12.pure_robot import SOAP, WATER, RobotState, move, transfer_to_cleaner, turn, set_state, start, stop


commands = [
    ("move", 100),
    ("turn", -90),
    ("set", SOAP),
    ("start",),
    ("move", 100),
    ("stop",),
]

def apply_command(state: RobotState, command):
    command, args = command

    if command == "move":
        state = move(transfer_to_cleaner, args, state)
    elif command == "turn":
        state = turn(transfer_to_cleaner, args, state)
    elif command == "set":
        state = set_state(transfer_to_cleaner, args, state)
    elif command == "start":
        state = start(transfer_to_cleaner, state)
    elif command == "stop":
        state = stop(transfer_to_cleaner, state)

    return state


def main():
    state = reduce(apply_command, commands, RobotState(0, 0, 0, WATER))
