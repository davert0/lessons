
from monadic_api import SOAP, move, set_state, turn

move(100) >> turn(-90) >> set_state(SOAP)
