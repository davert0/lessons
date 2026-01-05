import queue
import threading

import pure_robot


class RobotApi:
    def __init__(self):
        self.commands_queue = queue.Queue()

    def setup(self, f_move, f_turn, f_set_state, f_start, f_stop, f_transfer):
        self.f_move = f_move
        self.f_turn = f_turn
        self.f_set_state = f_set_state
        self.f_start = f_start
        self.f_stop = f_stop
        self.f_transfer = f_transfer

    def make(self, command):
        if not hasattr(self, "cleaner_state"):
            self.cleaner_state = pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER)

        cmd = command.split(" ")
        if cmd[0] == "move":
            self.cleaner_state = self.f_move(
                self.f_transfer, int(cmd[1]), self.cleaner_state
            )
        elif cmd[0] == "turn":
            self.cleaner_state = self.f_turn(
                self.f_transfer, int(cmd[1]), self.cleaner_state
            )
        elif cmd[0] == "set":
            self.cleaner_state = self.f_set_state(
                self.f_transfer, cmd[1], self.cleaner_state
            )
        elif cmd[0] == "start":
            self.cleaner_state = self.f_start(self.f_transfer, self.cleaner_state)
        elif cmd[0] == "stop":
            self.cleaner_state = self.f_stop(self.f_transfer, self.cleaner_state)
        return self.cleaner_state

    def __call__(self, stream):
        commands = stream.split(" ")
        for command in commands:
            self.commands_queue.put(command)

    def run(self):
        concat_command = ""

        while True:
            command = self.commands_queue.get()
            if command.isdigit():
                concat_command += command + " "
                continue
            concat_command += command
            self.make(concat_command)
            concat_command = ""


def transfer_to_cleaner(message):
    print(message)


api = RobotApi()
api.setup(
    pure_robot.move,
    pure_robot.turn,
    pure_robot.set_state,
    pure_robot.start,
    pure_robot.stop,
    transfer_to_cleaner,
)

threading.Thread(target=api.run).start()
