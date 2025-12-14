from __future__ import annotations

from typing import TYPE_CHECKING

from robot.commands.command import Command

if TYPE_CHECKING:
    from robot.robot import Robot


class MoveCommand(Command):
    def __init__(self, distance: int):
        self.distance = distance

    def execute(self, robot: Robot) -> None:
        robot._move(self.distance)
