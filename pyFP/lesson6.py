from pymonad.tools import curry
from pymonad.state import State




@curry(2)
def hit_by(amount: int, is_alive: bool):
    def health_computation(health_remained):
        return is_alive if not is_alive else health_remained > 0, 0 if not is_alive else health_remained - amount 
    return State(health_computation)

@curry(2)
def heal_by(amount: int, is_alive: bool):
    def health_computation(health_remained):
        return is_alive if not is_alive else health_remained > 0, 0 if not is_alive else health_remained + amount
    return State(health_computation)



player_init = {
    "health": 5,
    "is_alive": True
}

player_state = State.insert(player_init["is_alive"])

# Если игрока убили, вылечить уже не получится
finale = player_state.then(hit_by(5)).then(heal_by(3)).then(heal_by(4)) # False, 0
print(finale.run(player_init['health']))


finale = player_state.then(hit_by(4)).then(heal_by(2)).then(heal_by(1)) # True, 4
print(finale.run(player_init['health']))