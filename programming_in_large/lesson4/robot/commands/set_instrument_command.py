from __future__ import annotations

from typing import TYPE_CHECKING

from robot.commands.command import Command
from robot.domain import Instrument

if TYPE_CHECKING:
    from robot.robot import Robot


class SetInstrumentCommand(Command):
    def __init__(self, instrument: Instrument):
        self.instrument = instrument

    def execute(self, robot: Robot) -> None:
        robot._set_instrument(self.instrument)
