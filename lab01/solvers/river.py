from .search import bfs

# 定义0，1 以及action
START=(0,0,0,0)
GOAL=(1,1,1,1)
PASSENGERS=((None,"独自"),(1,"带狼"),(2,"带羊"),(3,"带菜"))

def is_safe(state):
    farmer,wolf,sheep,cabbage=state

    wolf_eat_sheep=(wolf==sheep and farmer !=sheep)
    sheep_eat_cabbage=(sheep==cabbage and farmer!=sheep)

    return not (wolf_eat_sheep or sheep_eat_cabbage)


def moves(state):
    farmer_bank=state[0]
    destination=1-farmer_bank

    direction ="去右岸" if destination==1 else "回左岸"
    for passenger, label in PASSENGERS:
        if passenger is not None and state[passenger]!=farmer_bank:
            continue

        next_state=list(state)
        next_state[0]=destination
        if passenger is not None:
            next_state[passenger]=destination

        next_state=tuple(next_state)
        if is_safe(next_state):
            yield label+direction,next_state

def solve():
    return bfs(START,lambda state:state==GOAL,moves)