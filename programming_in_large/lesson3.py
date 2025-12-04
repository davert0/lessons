import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List


class Parser(ABC):
    @abstractmethod
    def parse(self, commands: list[str]) -> List["Command"]:
        pass


class Command(ABC):
    @abstractmethod
    def execute(self, robot: "Robot"):
        pass


class MoveCommand(Command):
    def __init__(self, distance: int):
        self.distance = distance

    def execute(self, robot: "Robot"):
        robot._move(self.distance)


class TurnCommand(Command):
    def __init__(self, angle: int):
        self.angle = angle

    def execute(self, robot: "Robot"):
        robot._turn(self.angle)


class SetInstrumentCommand(Command):
    def __init__(self, instrument: "Instrument"):
        self.instrument = instrument

    def execute(self, robot: "Robot"):
        robot._set_instrument(self.instrument)


class StartCommand(Command):
    def __init__(self):
        pass

    def execute(self, robot: "Robot"):
        robot._start()


class StopCommand(Command):
    def __init__(self):
        pass

    def execute(self, robot: "Robot"):
        robot._stop()


@dataclass
class Direction:
    x: int
    y: int


class Instrument(Enum):
    WATER = 0
    SOAP = 1
    BRUSH = 2


class State(Enum):
    IDLE = 0
    WORKING = 1


class DefaultParser(Parser):
    def parse(self, commands: List[str]) -> List[Command]:
        parsed_commands = []
        for command in commands:
            parsed_commands.append(self._parse_command(command))
        return parsed_commands

    @staticmethod
    def _parse_command(command: str) -> Command:
        command_splitted = command.split(" ")

        if command_splitted[0] == "MOVE":
            return MoveCommand(int(command_splitted[1]))

        elif command_splitted[0] == "TURN":
            angle = int(command_splitted[1])
            return TurnCommand(angle)

        elif command_splitted[0] == "SET":
            instrument = Instrument[command_splitted[1]]
            return SetInstrumentCommand(instrument)

        elif command_splitted[0] == "START":
            return StartCommand()

        elif command_splitted[0] == "STOP":
            return StopCommand()

        raise ValueError("Invalid command")


class Robot:
    def __init__(self, parser: Parser):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.instrument = Instrument.WATER
        self.state = State.IDLE
        self.parser = parser

    def input(self, commands: List[str]):
        parsed_commands = self.parser.parse(commands)
        self._execute_commands(parsed_commands)

    def _execute_commands(self, commands: List[Command]) -> None:
        for command in commands:
            command.execute(self)

    def _move(self, distance: int) -> None:
        rad = math.radians(self.angle)

        dx = math.cos(rad) * distance
        dy = math.sin(rad) * distance

        self.x += dx
        self.y += dy

        print(f"POS self.x={self.x}, self.y={self.y}")

    def _turn(self, angle: int) -> None:
        self.angle += angle
        self.angle %= 360
        print(f"ANGLE {self.angle}")

    def _set_instrument(self, instrument: Instrument) -> None:
        self.instrument = instrument
        print(f"SET {instrument}")

    def _start(self) -> None:
        self.state = State.WORKING
        print(f"START WITH {self.instrument}")

    def _stop(self) -> None:
        self.state = State.IDLE
        print("STOP")


def main():
    parser = DefaultParser()
    robot = Robot(parser)
    robot.input(["MOVE 10", "TURN 90", "MOVE 10", "STOP"])
