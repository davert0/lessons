from __future__ import annotations

from typing import TYPE_CHECKING

from robot.commands.command import Command

if TYPE_CHECKING:
    from robot.robot import Robot


class StartCommand(Command):
    def execute(self, robot: Robot) -> None:
        robot._start()
