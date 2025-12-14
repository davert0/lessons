from robot import DefaultParser, Robot


def transfer_to_robot(message: str) -> None:
    print(message)


def main() -> None:
    robot = Robot(parser=DefaultParser(), transfer_to_robot=transfer_to_robot)
    robot.input(["MOVE 10", "TURN 90", "MOVE 10", "STOP"])


if __name__ == "__main__":
    main()
