import math
from typing import Any, Callable, Dict, List


def create_robot() -> Dict[str, Any]:
    return {
        "x": 0.0,
        "y": 0.0,
        "angle": 0,
        "instrument": "water",
        "state": "idle",
    }


def move(robot: Dict[str, Any], distance: int) -> None:
    rad = math.radians(robot["angle"])

    dx = math.cos(rad) * distance
    dy = math.sin(rad) * distance

    robot["x"] += dx
    robot["y"] += dy

    print(f"POS x={robot['x']:.2f}, y={robot['y']:.2f}")


def turn(robot: Dict[str, Any], angle: int) -> None:
    robot["angle"] += angle
    robot["angle"] %= 360
    print(f"ANGLE {robot['angle']}")


def set_instrument(robot: Dict[str, Any], instrument: str) -> None:
    robot["instrument"] = instrument
    print(f"SET {instrument}")


def start(robot: Dict[str, Any]) -> None:
    robot["state"] = "working"
    print(f"START WITH {robot['instrument']}")


def stop(robot: Dict[str, Any]) -> None:
    robot["state"] = "idle"
    print("STOP")


def parse_commands(commands: str) -> List[Callable]:
    parsed_commands: List[Callable] = []
    splitted_commands = commands.strip().split("\n")

    for raw in splitted_commands:
        line = raw.strip()
        if not line:
            continue

        parts = line.split()
        cmd = parts[0].lower()

        if cmd == "move":
            distance = int(parts[1]) if len(parts) > 1 else 0

            parsed_commands.append(lambda robot, d=distance: move(robot, d))

        elif cmd == "turn":
            angle = int(parts[1]) if len(parts) > 1 else 0

            parsed_commands.append(lambda robot, a=angle: turn(robot, a))

        elif cmd == "set":
            instrument = parts[1].lower()
            parsed_commands.append(
                lambda robot, instr=instrument: set_instrument(robot, instr)
            )

        elif cmd == "start":
            parsed_commands.append(lambda robot: start(robot))

        elif cmd == "stop":
            parsed_commands.append(lambda robot: stop(robot))

    return parsed_commands


def apply_commands(
    robot: Dict[str, Any], commands: List[Callable[[Dict[str, Any]], None]]
) -> None:
    for cmd in commands:
        cmd(robot)


def main():
    incoming_commands = input()
    robot = create_robot()
    commands = parse_commands(incoming_commands)
    apply_commands(robot, commands)


if __name__ == "__main__":
    main()
