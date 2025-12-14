from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from robot.commands import Command


class Parser(ABC):
    @abstractmethod
    def parse(self, commands: list[str]) -> List[Command]:
        raise NotImplementedError
