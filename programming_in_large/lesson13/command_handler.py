from dataclasses import dataclass
from pure_robot import RobotState, move, transfer_to_cleaner, turn, set_state, start, stop

@dataclass
class CommandHandler:
    eventStore: list[str]
    currentState: RobotState

    def handle_command(self, command):
        state = RobotState(0.0, 0.0, 0, 1)
        for command in self.eventStore:
            state = self._handle_conrete_command(command, state)
        self.eventStore.append(command)
        state = self._handle_conrete_command(command)
        self.currentState = state
        return state
    
    def _handle_conrete_command(self, cmd, state):
        cmd = cmd.split(' ')
        if cmd[0] == 'move':
            state = move(transfer_to_cleaner, int(cmd[1]), state)
        elif cmd[0] == 'turn':
            state = turn(transfer_to_cleaner, int(cmd[1]), state)
        elif cmd[0] == 'set':
            state = set_state(transfer_to_cleaner, cmd[1], state)
        elif cmd[0] == 'start':
            state = start(transfer_to_cleaner, state)
        elif cmd[0] == 'stop':
            state = stop(transfer_to_cleaner, state)
        return state