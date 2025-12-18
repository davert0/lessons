from clean_robot import RobotState, make, transfer_to_cleaner


def send_to_robot(code):
        initial_state = RobotState(x=0, y=0, angle=0, state=0)
        return make(transfer_to_cleaner, code, initial_state)
