from typing import Callable

import pure_robot


class RobotApi:
    def setup(self, setup_func):
        self.f_move: Callable
        self.f_turn: Callable
        self.f_set_state: Callable
        self.f_start: Callable
        self.f_stop: Callable
        self.f_transfer: Callable
        setup_func(self)

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

    def __call__(self, command):
        return self.make(command)


def transfer_to_cleaner(message):
    print(message)


def double_move(transfer, dist, state):
    return pure_robot.move(transfer, dist * 2, state)


def setup_api(api: RobotApi):
    api.f_move = pure_robot.move
    api.f_turn = pure_robot.turn
    api.f_set_state = pure_robot.set_state
    api.f_start = pure_robot.start
    api.f_stop = pure_robot.stop
    api.f_transfer = transfer_to_cleaner


api = RobotApi()
api.setup(setup_api)
