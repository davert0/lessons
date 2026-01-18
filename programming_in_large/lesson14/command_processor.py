from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod
from typing import Protocol, List, Dict, Optional, Callable, Type, Any
import math


@dataclass
class RobotState:
    x: float
    y: float
    angle: float
    state: int


class CleaningMode(Enum):
    WATER = 1
    SOAP = 2
    BRUSH = 3



class Event(ABC):


    @abstractmethod
    def get_event_type(self) -> str:
        pass

    def apply(self, state: RobotState) -> RobotState:
        """По умолчанию событие не влияет на состояние (например Requested)."""
        return state


@dataclass
class MoveRequestedEvent(Event):
    distance: float

    def get_event_type(self) -> str:
        return f"MOVE_REQUESTED {self.distance}"


@dataclass
class TurnRequestedEvent(Event):
    angle: float

    def get_event_type(self) -> str:
        return f"TURN_REQUESTED {self.angle}"


@dataclass
class StateChangeRequestedEvent(Event):
    new_state: CleaningMode

    def get_event_type(self) -> str:
        return f"STATE_CHANGE_REQUESTED {self.new_state.name}"


@dataclass
class RobotStartedRequestedEvent(Event):
    def get_event_type(self) -> str:
        return "START_REQUESTED"


@dataclass
class RobotStoppedRequestedEvent(Event):
    def get_event_type(self) -> str:
        return "STOP_REQUESTED"



@dataclass
class RobotMovedEvent(Event):
    distance: float

    def apply(self, state: RobotState) -> RobotState:
        angle_rads = state.angle * (math.pi / 180.0)
        return RobotState(
            x=state.x + self.distance * math.cos(angle_rads),
            y=state.y + self.distance * math.sin(angle_rads),
            angle=state.angle,
            state=state.state,
        )

    def get_event_type(self) -> str:
        return f"ROBOT_MOVED {self.distance}"


@dataclass
class RobotTurnedEvent(Event):
    angle: float

    def apply(self, state: RobotState) -> RobotState:
        return RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle + self.angle,
            state=state.state,
        )

    def get_event_type(self) -> str:
        return f"ROBOT_TURNED {self.angle}"


@dataclass
class RobotStateChangedEvent(Event):
    new_state: CleaningMode

    def apply(self, state: RobotState) -> RobotState:
        return RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle,
            state=self.new_state.value,
        )

    def get_event_type(self) -> str:
        return f"ROBOT_STATE_CHANGED {self.new_state.name}"


@dataclass
class RobotStartedEvent(Event):
    def get_event_type(self) -> str:
        return "ROBOT_STARTED"


@dataclass
class RobotStoppedEvent(Event):
    def get_event_type(self) -> str:
        return "ROBOT_STOPPED"



class Command(Protocol):
    def validate(self) -> None:
        ...
        
    def to_requested_events(self) -> List[Event]:
        ...

    def get_command_type(self) -> str:
        ...


@dataclass
class MoveCommand:
    distance: float

    def validate(self) -> None:
        if not isinstance(self.distance, (int, float)):
            raise ValueError("distance must be a number")
        if self.distance == 0:
            raise ValueError("distance must be non-zero")

    def to_requested_events(self) -> List[Event]:
        return [MoveRequestedEvent(self.distance)]

    def get_command_type(self) -> str:
        return f"MOVE {self.distance}"


@dataclass
class TurnCommand:
    angle: float

    def validate(self) -> None:
        if not isinstance(self.angle, (int, float)):
            raise ValueError("angle must be a number")

    def to_requested_events(self) -> List[Event]:
        return [TurnRequestedEvent(self.angle)]

    def get_command_type(self) -> str:
        return f"TURN {self.angle}"


@dataclass
class SetStateCommand:
    new_state: CleaningMode

    def validate(self) -> None:
        if not isinstance(self.new_state, CleaningMode):
            raise ValueError("new_state must be CleaningMode")

    def to_requested_events(self) -> List[Event]:
        return [StateChangeRequestedEvent(self.new_state)]

    def get_command_type(self) -> str:
        return f"SET_STATE {self.new_state.name}"


@dataclass
class StartCommand:
    def validate(self) -> None:
        return

    def to_requested_events(self) -> List[Event]:
        return [RobotStartedRequestedEvent()]

    def get_command_type(self) -> str:
        return "START"


@dataclass
class StopCommand:
    def validate(self) -> None:
        return

    def to_requested_events(self) -> List[Event]:
        return [RobotStoppedRequestedEvent()]

    def get_command_type(self) -> str:
        return "STOP"



Subscriber = Callable[[str, int, Event], None]


class EventStore:
    def __init__(self):
        self._events: Dict[str, List[Event]] = {}
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)

    def append_events(self, robot_id: str, events: List[Event]) -> None:
        if not events:
            return

        if robot_id not in self._events:
            self._events[robot_id] = []

        for event in events:
            self._events[robot_id].append(event)
            idx = len(self._events[robot_id]) - 1
            for sub in list(self._subscribers):
                sub(robot_id, idx, event)

    def get_events(self, robot_id: str) -> List[Event]:
        return self._events.get(robot_id, [])

    def get_events_from_version(self, robot_id: str, from_version: int) -> List[Event]:
        events = self.get_events(robot_id)
        return events[from_version:] if from_version < len(events) else []



class StateProjector:
    def __init__(self, initial_state: RobotState):
        self._initial_state = initial_state

    def project_state(self, events: List[Event]) -> RobotState:
        current_state = self._initial_state
        for event in events:
            current_state = event.apply(current_state)
        return current_state



class CommandHandler:

    def __init__(self, event_store: EventStore):
        self._event_store = event_store

    def handle_command(self, robot_id: str, command: Command) -> None:
        command.validate()
        requested_events = command.to_requested_events()
        self._event_store.append_events(robot_id, requested_events)



class EventProcessor(ABC):
    def __init__(self, event_store: EventStore, projector: StateProjector):
        self._event_store = event_store
        self._projector = projector

    @abstractmethod
    def on_event(self, robot_id: str, event_index: int, event: Event) -> None:
        pass


class RobotMovementProcessor(EventProcessor):


    def on_event(self, robot_id: str, event_index: int, event: Event) -> None:
        if isinstance(event, MoveRequestedEvent):
            if event.distance < 0:
                self._event_store.append_events(robot_id, [CommandRejectedEvent("negative distance")])
                return
            self._event_store.append_events(robot_id, [RobotMovedEvent(event.distance)])
            return

        if isinstance(event, TurnRequestedEvent):
            self._event_store.append_events(robot_id, [RobotTurnedEvent(event.angle)])
            return


class RobotModeProcessor(EventProcessor):
    def on_event(self, robot_id: str, event_index: int, event: Event) -> None:
        if isinstance(event, StateChangeRequestedEvent):
            self._event_store.append_events(robot_id, [RobotStateChangedEvent(event.new_state)])


class RobotLifecycleProcessor(EventProcessor):
    def on_event(self, robot_id: str, event_index: int, event: Event) -> None:
        if isinstance(event, RobotStartedRequestedEvent):
            self._event_store.append_events(robot_id, [RobotStartedEvent()])
        elif isinstance(event, RobotStoppedRequestedEvent):
            self._event_store.append_events(robot_id, [RobotStoppedEvent()])



class TimeTravel:
    def __init__(self, event_store: EventStore, state_projector: StateProjector):
        self._event_store = event_store
        self._state_projector = state_projector

    def get_state_at_version(self, robot_id: str, version: int) -> Optional[RobotState]:
        events = self._event_store.get_events(robot_id)
        if version < 0 or version > len(events):
            return None
        return self._state_projector.project_state(events[:version])

    def get_current_version(self, robot_id: str) -> int:
        return len(self._event_store.get_events(robot_id))

    def get_current_state(self, robot_id: str) -> RobotState:
        return self._state_projector.project_state(self._event_store.get_events(robot_id))



def main():
    event_store = EventStore()
    initial_state = RobotState(0.0, 0.0, 0.0, CleaningMode.WATER.value)
    projector = StateProjector(initial_state)

    movement = RobotMovementProcessor(event_store, projector)
    mode = RobotModeProcessor(event_store, projector)
    lifecycle = RobotLifecycleProcessor(event_store, projector)

    event_store.subscribe(movement.on_event)
    event_store.subscribe(mode.on_event)
    event_store.subscribe(lifecycle.on_event)

    command_handler = CommandHandler(event_store)
    time_travel = TimeTravel(event_store, projector)

    robot_id = "robot_001"

    commands: List[Command] = [
        MoveCommand(100),
        TurnCommand(-90),
        SetStateCommand(CleaningMode.SOAP),
        StartCommand(),
        MoveCommand(50),
        StopCommand(),
    ]

    for i, cmd in enumerate(commands):
        print(f"Cmd {i + 1}: {cmd.get_command_type()}")
        command_handler.handle_command(robot_id, cmd)

        print(f"State: {time_travel.get_current_state(robot_id)}")