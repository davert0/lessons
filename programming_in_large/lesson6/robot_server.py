from abc import ABC, abstractmethod

import clean_robot


class RobotRepository(ABC):
    @abstractmethod
    def get_state(self) -> clean_robot.RobotState:
        pass

    @abstractmethod
    def set_state(self, state: clean_robot.RobotState):
        pass


class CleanerApi:
    # конструктор
    def __init__(self, repo: RobotRepository):
        self.repo = repo

    # взаимодействие с роботом вынесено в отдельную функцию
    def transfer_to_cleaner(self, message):
        print(message)

    def get_x(self):
        state = self.repo.get_state()
        return state.x

    def get_y(self):
        state = self.repo.get_state()
        return state.y

    def get_angle(self):
        state = self.repo.get_state()
        return state.angle

    def get_state(self):
        return self.repo.get_state()

    def activate_cleaner(self, code):
        for command in code:
            cmd = command.split(" ")
            if cmd[0] == "move":
                self.repo.set_state(
                    clean_robot.move(
                        self.transfer_to_cleaner, int(cmd[1]), self.cleaner_state
                    )
                )
            elif cmd[0] == "turn":
                self.repo.set_state(
                    clean_robot.turn(
                        self.transfer_to_cleaner, int(cmd[1]), self.cleaner_state
                    )
                )
            elif cmd[0] == "set":
                self.repo.set_state(
                    clean_robot.set_state(
                        self.transfer_to_cleaner, cmd[1], self.cleaner_state
                    )
                )
            elif cmd[0] == "start":
                self.repo.set_state(
                    clean_robot.start(self.transfer_to_cleaner, self.cleaner_state)
                )
            elif cmd[0] == "stop":
                self.repo.set_state(
                    clean_robot.stop(self.transfer_to_cleaner, self.cleaner_state)
                )
