from __future__ import annotations

from typing import List

from robot.commands import (
    Command,
    MoveCommand,
    SetInstrumentCommand,
    StartCommand,
    StopCommand,
    TurnCommand,
)
from robot.domain import Instrument
from robot.parsers.parser import Parser


class DefaultParser(Parser):
    def parse(self, commands: list[str]) -> List[Command]:
        return [self._parse_command(cmd) for cmd in commands]

    @staticmethod
    def _parse_command(command: str) -> Command:
        parts = command.split()
        if not parts:
            raise ValueError("Empty command")

        op = parts[0].upper()

        if op == "MOVE":
            if len(parts) != 2:
                raise ValueError(f"Invalid MOVE format: {command}")
            return MoveCommand(int(parts[1]))

        if op == "TURN":
            if len(parts) != 2:
                raise ValueError(f"Invalid TURN format: {command}")
            return TurnCommand(int(parts[1]))

        if op == "SET":
            if len(parts) != 2:
                raise ValueError(f"Invalid SET format: {command}")
            return SetInstrumentCommand(Instrument[parts[1].upper()])

        if op == "START":
            if len(parts) != 1:
                raise ValueError(f"Invalid START format: {command}")
            return StartCommand()

        if op == "STOP":
            if len(parts) != 1:
                raise ValueError(f"Invalid STOP format: {command}")
            return StopCommand()

        raise ValueError(f"Invalid command: {command}")
