from __future__ import annotations

from typing import TYPE_CHECKING

from robot.commands.command import Command

if TYPE_CHECKING:
    from robot.robot import Robot


class StopCommand(Command):
    def execute(self, robot: Robot) -> None:
        robot._stop()
