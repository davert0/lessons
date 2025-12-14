from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from robot.robot import Robot


class Command(ABC):
    @abstractmethod
    def execute(self, robot: Robot) -> None:
        raise NotImplementedError
