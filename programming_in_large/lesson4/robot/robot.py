from __future__ import annotations

import math
from typing import Callable, List

from robot.commands import Command
from robot.domain import Instrument, State
from robot.parsers import Parser

TransferToRobot = Callable[[str], None]


class Robot:
    def __init__(self, parser: Parser, transfer_to_robot: TransferToRobot):
        self.x: float = 0.0
        self.y: float = 0.0
        self.angle: int = 0
        self.instrument: Instrument = Instrument.WATER
        self.state: State = State.IDLE

        self.parser = parser
        self.transfer_to_robot = transfer_to_robot

    def input(self, commands: List[str]) -> None:
        parsed = self.parser.parse(commands)
        self._execute_commands(parsed)

    def _execute_commands(self, commands: List[Command]) -> None:
        for command in commands:
            command.execute(self)

    def _move(self, distance: int) -> None:
        rad = math.radians(self.angle)
        dx = math.cos(rad) * distance
        dy = math.sin(rad) * distance

        self.x += dx
        self.y += dy
        self.transfer_to_robot(f"POS x={self.x}, y={self.y}")

    def _turn(self, angle: int) -> None:
        self.angle = (self.angle + angle) % 360
        self.transfer_to_robot(f"ANGLE {self.angle}")

    def _set_instrument(self, instrument: Instrument) -> None:
        self.instrument = instrument
        self.transfer_to_robot(f"SET {instrument.name}")

    def _start(self) -> None:
        self.state = State.WORKING
        self.transfer_to_robot(f"START WITH {self.instrument.name}")

    def _stop(self) -> None:
        self.state = State.IDLE
        self.transfer_to_robot("STOP")
